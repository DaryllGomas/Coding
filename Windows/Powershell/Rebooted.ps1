# Reboot-Diagnose.ps1 — find why the last reboot happened
$ErrorActionPreference = 'SilentlyContinue'

function Get-LastBoot {
  $bootEvt = Get-WinEvent -FilterHashtable @{LogName='System'; Id=12; ProviderName='Microsoft-Windows-Kernel-General'} -MaxEvents 1
  if ($bootEvt) { return $bootEvt.TimeCreated } else { return (Get-CimInstance Win32_OperatingSystem).LastBootUpTime }
}

$boot = Get-LastBoot
$windowStart = $boot.AddMinutes(-30)
$windowEnd   = $boot.AddMinutes(5)

# Events that explain restarts
$interestingIds = 41,42,1,1074,1076,6008,6006,6005,109,1001
$providers = 'Microsoft-Windows-Kernel-Power','Microsoft-Windows-Kernel-General','User32','EventLog','Microsoft-Windows-WER-SystemErrorReporting','BugCheck','Microsoft-Windows-WindowsUpdateClient','Microsoft-Windows-WHEA-Logger','Service Control Manager','Display'

$nearBoot = Get-WinEvent -FilterHashtable @{LogName='System'; StartTime=$windowStart; EndTime=$windowEnd} |
  Where-Object { ($interestingIds -contains $_.Id) -or ($providers -contains $_.ProviderName) } |
  Sort-Object TimeCreated

# Categorize
$planned   = $nearBoot | Where-Object { $_.ProviderName -eq 'User32' -and $_.Id -eq 1074 }
$unexpected= $nearBoot | Where-Object { $_.ProviderName -eq 'Microsoft-Windows-Kernel-Power' -and $_.Id -eq 41 }
$bugcheck  = Get-WinEvent -FilterHashtable @{LogName='System'; Id=1001; StartTime=$windowStart; EndTime=$windowEnd} | Where-Object { $_.ProviderName -in @('BugCheck','Microsoft-Windows-WER-SystemErrorReporting') }
$wheaFatal = Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WHEA-Logger'; Id=1; StartTime=$windowStart; EndTime=$windowEnd }
$wheaCorr  = Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WHEA-Logger'; Id=18; StartTime=$windowStart; EndTime=$windowEnd }

# Windows Update activity in the last 24h (often triggers planned restarts)
$wu = Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WindowsUpdateClient'; StartTime=$boot.AddHours(-24); EndTime=$boot.AddMinutes(5) } | Sort-Object TimeCreated

# Recent hotfixes (another hint of update-driven reboot)
$recentHotfix = Get-HotFix | Where-Object { $_.InstalledOn -gt (Get-Date).AddDays(-7) } | Sort-Object InstalledOn

# Decide likely cause
$reason = 'Unknown'
if ($planned) { $reason = 'Planned restart (user/service requested — often Windows Update).' }
elseif ($bugcheck) { $reason = 'Crash/BSOD (bugcheck) caused reboot.' }
elseif ($wheaFatal) { $reason = 'Fatal hardware error (WHEA) triggered reboot (CPU/RAM/board/PSU possible).' }
elseif ($unexpected) { $reason = 'Unclean restart — power loss or crash (Kernel-Power 41).' }

# Build summary & timeline
$result = [PSCustomObject]@{
  'Boot time'                           = $boot
  'Likely cause'                        = $reason
  'Planned restart (1074) near boot'    = ($planned.Count -gt 0)
  'Kernel-Power 41 near boot'           = ($unexpected.Count -gt 0)
  'Bugcheck (1001) near boot'           = ($bugcheck.Count -gt 0)
  'WHEA fatal (1) near boot'            = ($wheaFatal.Count -gt 0)
  'WU activity in last 24h'             = ($wu.Count -gt 0)
}

$timeline = $nearBoot | Select-Object TimeCreated, Id, ProviderName, @{n='Message';e={$_.FormatDescription()}}

$path = "$env:PUBLIC\RebootReport.txt"
"==== Reboot Report $(Get-Date) ====" | Out-File -FilePath $path -Encoding UTF8
$result | Format-Table -AutoSize | Out-String | Add-Content $path
"`n-- Events within 30 min around boot ($($windowStart) to $($windowEnd)) --`n" | Add-Content $path
$timeline | Format-Table -Wrap -AutoSize | Out-String | Add-Content $path
"`n-- Windows Update Client activity (last 24h) --`n" | Add-Content $path
($wu | Select-Object TimeCreated, Id, @{n='Message';e={$_.FormatDescription()}} | Format-Table -Wrap -AutoSize | Out-String) | Add-Content $path
"`n-- Hotfixes installed in last 7 days --`n" | Add-Content $path
($recentHotfix | Format-Table -AutoSize | Out-String) | Add-Content $path

Write-Host "Boot time: $boot"
Write-Host "Likely cause: $reason"
Write-Host "Full report saved to: $path"
if (Test-Path "C:\Windows\Minidump") { 
  $dumps = Get-ChildItem "C:\Windows\Minidump" -File -ErrorAction SilentlyContinue
  if ($dumps) { Write-Host "Crash dumps found in C:\Windows\Minidump (send newest .dmp for deeper analysis)." }
}
