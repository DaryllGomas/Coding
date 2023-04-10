# Disable backup reminder
$RegKey = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting"
New-Item -Path $RegKey -Force | Out-Null
Set-ItemProperty -Path $RegKey -Name "Disabled" -Value 1
