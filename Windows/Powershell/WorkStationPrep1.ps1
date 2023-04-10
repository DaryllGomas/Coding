#Powershell script for initial Workstation Setup

#Install Brave Browser
$url = "https://laptop-updates.brave.com/latest/winx64"
$output = "C:\brave_installer.exe"
Invoke-WebRequest -Uri $url -OutFile $output

$installer = "C:\brave_installer.exe"
Start-Process -FilePath $installer

#Remove Start Menu items
Get-AppxPackage -AllUsers | Remove-AppxPackage

$registryPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System"
New-ItemProperty -Path $registryPath -Name "EnableLUA" -PropertyType DWORD -Value 0 -Force

# Ask for the new computer name
$newName = Read-Host "Enter the new computer name"

# Rename the computer
Rename-Computer -NewName $newName -Force

# Get the current network adapter name
$adapter = Get-NetAdapter | Select-Object -ExpandProperty Name

# Ask for the new IP address
$ipAddress = Read-Host "Enter the new IP address for the $adapter network adapter"

# Ask for the subnet mask
$subnetMask = Read-Host "Enter the subnet mask for the $adapter network adapter"

# Ask for the default gateway
$defaultGateway = Read-Host "Enter the default gateway for the $adapter network adapter"

# Set the IP address, subnet mask, and default gateway
New-NetIPAddress -InterfaceAlias $adapter -IPAddress $ipAddress -PrefixLength $subnetMask -DefaultGateway $defaultGateway

# Ask for the DNS server address
$dnsServer = Read-Host "Enter the DNS server address for the $adapter network adapter"

# Set the DNS server address
Set-DnsClientServerAddress -InterfaceAlias $adapter -ServerAddresses $dnsServer

# Ask for the domain name
$domainName = Read-Host "Enter the domain name to join"

# Ask for the administrator username
$adminUsername = Read-Host "Enter the domain administrator username"

# Ask for the administrator password
$adminPassword = Read-Host "Enter the domain administrator password" -AsSecureString

# Join the computer to the domain
Add-Computer -DomainName $domainName -Credential (New-Object System.Management.Automation.PSCredential -ArgumentList $adminUsername, $adminPassword)
