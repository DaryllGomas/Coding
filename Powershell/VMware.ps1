# Import the VMware PowerCLI module
Import-Module VMware.PowerCLI

# Connect to the local VMware Workstation instance
Connect-VIServer localhost

# Define the virtual machine configuration
$VMName = "Win10Client"
$GuestOS = "Windows10_64"
$MemoryMB = 4096
$NumCpu = 2
$DiskGB = 30

# Create a new virtual machine
New-VM -Name $VMName -GuestId $GuestOS -MemoryMB $MemoryMB -NumCpu $NumCpu -DiskGB $DiskGB -NetworkName "Bridged"

# Remove the floppy drive
Get-VM $VMName | Get-FloppyDrive | Remove-FloppyDrive

# Disable audio
Set-VM $VMName -ExtensionProperty @{"config.defaultSoundEnabled" = "false"}

# Disable the side channel feature
Set-VM $VMName -ExtensionProperty @{"config.hardware.featureMask.sideChannel" = "false"}

# Start the virtual machine
Start-VM $VMName
