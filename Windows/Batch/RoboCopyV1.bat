@echo off
set "source=\\IPofNAS\Share"
set "destination=G:\BackUpFolder"

echo Starting the backup process...
echo Source: %source%
echo Destination: %destination%

set timestamp=%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set timestamp=%timestamp: =0%

robocopy "%source%" "%destination%" /MIR /Z /W:5 /R:5 /MT:8 /V /ETA /TEE /LOG+:"G:\BackUpFolder\backup_log_%timestamp%.txt"

if %ERRORLEVEL% LEQ 1 (
    echo Backup completed successfully!
) else (
    echo Backup encountered some errors. Please check the log file for details.
)
pause
