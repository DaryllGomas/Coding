# Define the path to the registry key where the Windows Update policy will be set
$regKey = 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\'

# Create the registry key if it doesn't already exist
New-Item -Path $regKey -Force | Out-Null

# Create a new registry property to control the Windows Update behavior
New-ItemProperty -Path $regKey -Name "AutoRestartWithLoggedOnUsers" -Value 0 -PropertyType "DWord" -Force | Out-Null
