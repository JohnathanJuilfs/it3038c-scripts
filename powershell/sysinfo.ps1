#$Hello = "Hello, PowerShell!"
#write-Host($Hello)
#Display Computer Name, Date & Time, IP, and PowerShell Version.
#Email Self Sysinfo.
function GetDate {
    (Get-Date -Format "dddd MM/dd/yyyy HH:mm K")
}

function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

function GetVersion {
    (Get-Host) | Select-Object Version
}

write-host(getIP)
$Version = GetVersion
$IP = getIP
$Date = GetDate
$Body = "This machine's IP is $IP. User is $env:username. Hostname is $env:COMPUTERNAME. PowerShell version $Version. Today's date is $Date"

write-host($Body)

#Send-MailMessage -To "juilfsjc@mail.uc.edu" -From "juilfsjc@mail.uc.edu" -Subject "IT3038C Windows SysInfo" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)