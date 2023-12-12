; Definiere die Tastenkombination Alt+Shift+R
!+R:: 
    ; Führe das PowerShell-Skript aus
    Run, PowerShell.exe -ExecutionPolicy Bypass -File "C:\QualityOfLife-Scripts\ClearRecycleBin\clearRecycleBin.ps1"
    ; Warte auf das Ende des PowerShell-Skripts
    WinWaitActive, ahk_exe powershell.exe
    ; Merke dir den Titel des PowerShell-Fensters
    WinGet, PowerShellWindow, ID, A
return

; Tastenkombination zum Schliessen des aktuellen PowerShell-Fensters
^+R:: 
    ; Finde das PowerShell-Fenster nach seinem gespeicherten ID
    WinClose, %PowerShellWindow%
return