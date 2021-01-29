
#$Hello = "Hello, PowerShell!"
#write-Host($Hello)
function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

write-host(getIP)
$IP = getIP
$Date = ""
$Body = "This machine's IP is $IP. User is $env:username. Hostname is $. PowerShell version . Today's date is $Date"

write-host($Body)

#Send-MailMessage -To "juilfsjc@mail.uc.edu" -From "juilfsjc@mail.uc.edu" -Subject "IT3038C Windows SysINfO" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)