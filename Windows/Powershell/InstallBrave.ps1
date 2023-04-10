$url = "https://laptop-updates.brave.com/latest/winx64"
$output = "C:\brave_installer.exe"
Invoke-WebRequest -Uri $url -OutFile $output

$installer = "C:\brave_installer.exe"
Start-Process -FilePath $installer
