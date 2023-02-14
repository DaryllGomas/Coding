#Powershell script for initial Server Setup

#Install Brave Browser
$url = "https://laptop-updates.brave.com/latest/winx64"
$output = "C:\brave_installer.exe"
Invoke-WebRequest -Uri $url -OutFile $output

$installer = "C:\brave_installer.exe"
Start-Process -FilePath $installer

#Create Local User with limited privilages
$username = "Admin"
$fullName = "Admin User"

$localUser = Get-LocalUser -Name $username -ErrorAction SilentlyContinue
if($localUser -eq $null) {
    $password = Read-Host -AsSecureString -Prompt "Enter the password for the local user account"
    New-LocalUser $username -Password $password -FullName $fullName -Description "local user"
    Add-LocalGroupMember -Group "Users" -Member $username
} else {
    Write-Host "The local user account already exists"
}

#Configure Network Adapters, Rename Server and Reboot
# Get all network adapters
$networkAdapters = Get-NetAdapter
Write-Host "List of Network Adapters:"
foreach ($adapter in $networkAdapters) {
  Write-Host "Name: $($adapter.Name), Index: $($adapter.ifIndex)"
}

# Loop through the network adapters and prompt the user for the IP address, gateway, and DNS settings
foreach ($adapter in $networkAdapters) {
    # Get current IP address of the adapter
    $currentIPAddress = (Get-NetIPAddress -InterfaceIndex $adapter.InterfaceIndex).IPAddress

    # Prompt for IP address
    $ipAddress = Read-Host "Enter the IP address for $($adapter.Name):"
    # If IP address is the same, skip it
    if ($ipAddress -eq $currentIPAddress) {
        Write-Host "$($adapter.Name) already has IP address $ipAddress, skipping."
        continue
    }
    
    # Prompt for Prefix
    $prefixLength = Read-Host "Enter the prefix length for $($adapter.Name):"

    # Prompt for gateway
    $defaultGateway = Read-Host "Enter the default gateway for $($adapter.Name):"
    
    # Prompt for DNS
    $useDefaultDNS = Read-Host "Do you want to use 8.8.8.8 and 8.8.4.4 as DNS servers for $($adapter.Name)? (Y/N):"
    if ($useDefaultDNS -eq "Y") {
        $dnsServers = "8.8.8.8", "8.8.4.4"
    }
    else {
        $dnsServers = Read-Host "Enter the DNS servers for $($adapter.Name), separated by a comma:"
    }
    
    # Remove the existing IP configuration for the adapter
    Remove-NetIPAddress -InterfaceIndex $adapter.InterfaceIndex -Confirm:$false
    
    # Set IP address, gateway, and DNS for the adapter
    New-NetIPAddress -InterfaceIndex $adapter.InterfaceIndex -IPAddress $ipAddress -PrefixLength $prefixLength -DefaultGateway $defaultGateway
    Set-DnsClientServerAddress -InterfaceIndex $adapter.InterfaceIndex -ServerAddresses $dnsServers
}

# Prompt the user to disable IPv6 for the adapters
$disableIPv6 = Read-Host "Do you want to disable IPv6 for all adapters? (Y/N):"
if ($disableIPv6 -eq "Y") {
    Get-NetAdapter | Set-NetAdapterBinding -ComponentID ms_tcpip6 -Enabled $false
}

#Rename computer
$newName = "Knox01"
Rename-Computer -NewName $newName -Force -Restart





