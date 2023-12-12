# clearRecycleBin.ps1

# Empty the Recycle Bin
Clear-RecycleBin -Force -Confirm:$false

# Display a message indicating success
Write-Host "Recycle Bin cleared successfully."