; Definiere die Tastenkombination Alt+Shift+R
!+R:: 
    ; Run PowerShell script
    Run, PowerShell.exe -ExecutionPolicy Bypass -File "C:\QualityOfLife-Scripts\ClearRecycleBin\clearRecycleBin.ps1"
    ; Wait for the PowerShell window to become active
    WinWaitActive, ahk_exe powershell.exe
    ; Save the PowerShell window ID
    WinGet, PowerShellWindow, ID, A
return

; Hotkey to close the PowerShell window
^+R:: 
    ; Find PowerShell-Window by ID and close it
    WinClose, %PowerShellWindow%
return