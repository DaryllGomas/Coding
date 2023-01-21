$IPAddress = "192.168.1.x"
$SubnetMask = 24
$DefaultGateway = "192.168.1.1"
$DNSServers = "8.8.8.8","8.8.4.4"

$nic = Get-NetAdapter | Where-Object {$_.Status -eq "Up"}
New-NetIPAddress -InterfaceIndex $nic.ifIndex -IPAddress $IPAddress -PrefixLength $SubnetMask -DefaultGateway $DefaultGateway
Set-DnsClientServerAddress -InterfaceIndex $nic.ifIndex -ServerAddresses $DNSServers


$newName = "vmserver"
Rename-Computer -NewName $newName -Force -Restart
