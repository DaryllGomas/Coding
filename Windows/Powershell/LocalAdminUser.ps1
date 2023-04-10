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
