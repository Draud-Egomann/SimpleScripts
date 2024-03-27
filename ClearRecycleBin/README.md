# clearRecycleBin PowerShell Script

## Overview

This README provides a step-by-step guide on how to create a custom profile using PowerShell and automate the process using AutoHotKey. The custom profile, in this case, focuses on clearing the Recycle Bin with a designated keyboard shortcut.

## Prerequisites

Before you begin, ensure that you have the following installed on your system:

1. **PowerShell**: Make sure PowerShell is installed on your machine.

2. **AutoHotKey V2.0**: Install AutoHotKey to set up keyboard shortcuts for script execution.

## Instructions

### 1. PowerShell Script

Create a PowerShell script named `clearRecycleBin.ps1` with the following content:

```powershell
# clearRecycleBin.ps1

# Empty the Recycle Bin
Clear-RecycleBin -Force -Confirm:$false

# Display a message indicating success
Write-Host "Recycle Bin cleared successfully."
```

Save this script in a directory of your choice. In this example, we'll use `C:\QualityOfLife-Scripts\ClearRecycleBin\`.

### 2. AutoHotKey Script

Create an AutoHotKey script to execute the PowerShell script with a specified keyboard shortcut. Save the following script in a file with a `.ahk` extension, e.g., `clearRecycleBin.ahk`:

```autohotkey
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
```

### 3. Execute the Script

Double-click on the AutoHotKey script (`clearRecycleBin.ahk`) to run it. This script sets up the specified keyboard shortcut (`Shift+R`) to clear the Recycle Bin and close the PowerShell window.

## Additional Information
Additionaly, you can put the AutoHotKey script in the startup folder.

For more details on creating custom profiles, using AutoHotKey, and implementing custom PowerShell commands, refer to the `createCustomProfile.md` markdown file in this repository.