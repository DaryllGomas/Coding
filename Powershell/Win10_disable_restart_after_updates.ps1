$regKey = 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\'
New-Item -Path $regKey -Force | Out-Null
New-ItemProperty -Path $regKey -Name "AutoRestartWithLoggedOnUsers" -Value 0 -PropertyType "DWord" -Force | Out-Null
