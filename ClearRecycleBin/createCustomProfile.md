Um einen benutzerdefinierten PowerShell-Befehl namens "clear-trash" zu erstellen, der die Datei "C:\ClearRecycleBin\clearRecycleBin.ps1" aufruft, kannst du die folgenden Schritte befolgen:

1. **PowerShell-Profil überprüfen oder erstellen (falls nicht vorhanden):**
   Stelle sicher, dass dein PowerShell-Profil existiert. Das Profil ist eine Skriptdatei, die beim Start von PowerShell geladen wird. Überprüfe, ob du bereits ein Profil hast:

   ```powershell
   Test-Path $profile
   ```

   Wenn dies `False` ergibt, erstelle ein neues Profil mit:

   ```powershell
   New-Item -Type File -Force $profile
   ```

2. **Öffne das PowerShell-Profil mit einem Texteditor:**

   ```powershell
   notepad $profile
   ```

   Falls das Profil neu erstellt wurde, kann dieser Befehl auch eine neue leere Datei öffnen.

3. **Füge den folgenden Code hinzu:**

   ```powershell
   function Clear-Trash {
       $scriptPath = "C:\ClearRecycleBin\clearRecycleBin.ps1"
       
       if (Test-Path $scriptPath) {
           & $scriptPath
       } else {
           Write-Host "Die Datei $scriptPath wurde nicht gefunden."
       }
   }
   ```

   Speichere und schliesse den Texteditor.

4. **Lade das aktualisierte Profil:**

   ```powershell
   . $profile
   ```

   Dadurch wird das aktualisierte Profil sofort geladen.

Nun kannst du den Befehl `Clear-Trash` in deiner PowerShell-Umgebung verwenden, um das Skript "clearRecycleBin.ps1" aufzurufen. Bitte beachte, dass du möglicherweise die Ausführungsrichtlinie für PowerShell-Skripte ändern musst, um das Skript erfolgreich auszuführen. Du kannst dies mit dem Befehl `Set-ExecutionPolicy` tun, wenn du entsprechende Berechtigungen hast.