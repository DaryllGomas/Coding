Get-AppxPackage -AllUsers | Remove-AppxPackage

$registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System"
New-ItemProperty -Path $registryPath -Name "EnableLUA" -PropertyType DWORD -Value 0 -Force
