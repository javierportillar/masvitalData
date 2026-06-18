' MasVitalRefresh runner — 100% invisible, no console window
Set WshShell = CreateObject("WScript.Shell")
Const HIDE = 0
Const WAIT = True
psScript = "C:\Users\ProDesk\Documents\javdevmasv\masvitalData\infra\refresh.ps1"
cmd = "powershell.exe -ExecutionPolicy Bypass -File """ & psScript & """"
WshShell.Run cmd, HIDE, WAIT
