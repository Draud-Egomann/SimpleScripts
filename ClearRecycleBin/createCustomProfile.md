# Create a Custom PowerShell Command

To create a custom PowerShell command called "Clear-Trash" that invokes the script `"C:\ClearRecycleBin\clearRecycleBin.ps1"`, you can follow the steps below:

1. **Check or create the PowerShell profile (if not already present):**
   Ensure your PowerShell profile exists. The profile is a script file loaded when PowerShell starts. Check if you already have a profile:

   ```powershell
   Test-Path $profile
   ```

   If this returns `False`, create a new profile with:

   ```powershell
   New-Item -Type File -Force $profile
   ```

2. **Open the PowerShell profile with a text editor:**

   ```powershell
   notepad $profile
   ```

   If the profile was newly created, this command can also open a new empty file.

3. **Add the following code:**

   ```powershell
   function Clear-Trash {
       $scriptPath = "C:\ClearRecycleBin\clearRecycleBin.ps1"
       
       if (Test-Path $scriptPath) {
           & $scriptPath
       } else {
           Write-Host "The file $scriptPath was not found."
       }
   }
   ```

   Save and close the text editor.

4. **Reload the updated profile:**

   ```powershell
   . $profile
   ```

   This will immediately load the updated profile.

Now you can use the command `Clear-Trash` in your PowerShell environment to invoke the script "clearRecycleBin.ps1". Please note that you may need to change the PowerShell script execution policy to successfully run the script. You can do this using the `Set-ExecutionPolicy` command if you have the appropriate permissions
