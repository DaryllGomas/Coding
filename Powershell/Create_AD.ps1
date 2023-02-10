Import-Module ServerManager

# Add the Active Directory Domain Services role
Add-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# Promote the server to a domain controller
Import-Module ADDSDeployment
Install-ADDSForest `
  -CreateDnsDelegation:$false `
  -DatabasePath "C:\Windows\NTDS" `
  -DomainMode "Win2012R2" `
  -DomainName "contoso.com" `
  -DomainNetbiosName "CONTOSO" `
  -ForestMode "Win2012R2" `
  -InstallDns:$true `
  -LogPath "C:\Windows\NTDS" `
  -NoRebootOnCompletion:$false `
  -SysvolPath "C:\Windows\SYSVOL" `
  -Force:$true
