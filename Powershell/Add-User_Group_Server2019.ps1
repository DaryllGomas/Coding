$username = "Admin"
$password = Read-Host -Prompt "Enter password for $username" -AsSecureString
$password = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($password))

$user = New-Object System.Management.Automation.PSCredential ($username, (ConvertTo-SecureString $password -AsPlainText -Force))
New-LocalUser -Name $username -Password $user.Password

$user = Get-LocalUser -Name $username
$user | Set-LocalUser -PasswordNeverExpires $true

Add-LocalGroupMember -Group "Administrators" -Member $username
