# Remove Active Directory Domain Services role
Uninstall-WindowsFeature -Name AD-Domain-Services

# Demote the server from a domain controller
Import-Module ADDSDeployment
Uninstall-ADDSForest -Confirm:$false

