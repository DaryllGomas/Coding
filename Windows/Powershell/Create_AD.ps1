# Import the ServerManager module
Import-Module ServerManager

# Install the Active Directory Domain Services and DNS features
Add-WindowsFeature -Name AD-Domain-Services, DNS

# Import the ADDSDeployment module
Import-Module ADDSDeployment

# Install the Active Directory forest with the following configuration options:
Install-ADDSForest `
 # Do not create a DNS delegation
 -CreateDnsDelegation:$false `
 # Specify the path to the database files
 -DatabasePath "C:\Windows\NTDS" `
 # Specify the domain functional level as Windows Server 2012 R2
 -DomainMode "Win2012R2" `
 # Specify the fully-qualified domain name (FQDN) as BigPic.com
 -DomainName "BigPic.com" `
 # Specify the NetBIOS name as BIGPIC
 -DomainNetbiosName "BIGPIC" `
 # Specify the forest functional level as Windows Server 2012 R2
 -ForestMode "Win2012R2" `
 # Install the DNS server role as well
 -InstallDns:$true `
 # Specify the path for the log files
 -LogPath "C:\Windows\NTDS" `
 # Do not reboot the server after installation is complete
 -NoRebootOnCompletion:$false `
 # Specify the path for the SYSVOL files
 -SysvolPath "C:\Windows\SYSVOL" `
 # Force the installation even if warnings are generated
 -Force:$true
