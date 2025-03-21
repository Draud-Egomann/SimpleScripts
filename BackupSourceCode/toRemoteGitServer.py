import os
import subprocess
import logging
import sys

# Configuration variables 
FOLDER_NAME = "<folder>"  # Name of the folder containing the git repo
REMOTE_SSH = "git@github.com:<user>/<repo>.git"
REMOTE_HTTPS = "https://github.com/<user>/<repo>.git"
REMOTE_TYPE = "ssh"  # ssh / https
BACKUP_REMOTE_NAME = "backup"  # Name of the temporary remote

def run_command(cmd, cwd=None):
    """
    Executes a shell command and returns stdout.
    If an error occurs, it is logged immediately and the script is terminated.
    """
    try:
        result = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error("Fehler bei Befehl '%s': %s. Stderr: %s", " ".join(cmd), e, e.stderr)
        sys.exit(1)

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    current_dir = os.getcwd()
    target_path = os.path.join(current_dir, FOLDER_NAME)
    
    if not os.path.isdir(target_path):
        logging.error("Das Verzeichnis '%s' existiert nicht.", FOLDER_NAME)
        sys.exit(1)
    
    logging.info("Wechsle in das Verzeichnis '%s'.", target_path)
    
    # Check if the directory has a git repo
    if not os.path.isdir(os.path.join(target_path, ".git")):
        logging.error("Das Verzeichnis '%s' ist kein Git-Repository.", FOLDER_NAME)
        sys.exit(1)
    
    # Determine the remote URL using the remote type
    if REMOTE_TYPE.lower() == "ssh":
        preferred_remote = REMOTE_SSH
    else:
        preferred_remote = REMOTE_HTTPS
    
    logging.info("Bevorzugte Remote-URL: '%s'.", preferred_remote)
    
    # If a remote with the given name already exists, remove it
    try:
        existing_backup = run_command(["git", "remote", "get-url", BACKUP_REMOTE_NAME], cwd=target_path)
        logging.info("Remote '%s' existiert bereits mit URL: '%s'. Es wird entfernt.", BACKUP_REMOTE_NAME, existing_backup)
        run_command(["git", "remote", "remove", BACKUP_REMOTE_NAME], cwd=target_path)
    except:
        logging.info("Kein existierender Remote '%s' gefunden.", BACKUP_REMOTE_NAME)
    
    # add the temporary remote
    logging.info("Fuege temporären Remote '%s' mit URL '%s' hinzu.", BACKUP_REMOTE_NAME, preferred_remote)
    run_command(["git", "remote", "add", BACKUP_REMOTE_NAME, preferred_remote], cwd=target_path)
    
    # Get the current branch
    current_branch = run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=target_path)
    logging.info("Aktueller Branch: '%s'.", current_branch)
    
    # push branch to the temporary
    logging.info("Pushe Branch '%s' zu Remote '%s'.", current_branch, BACKUP_REMOTE_NAME)
    run_command(["git", "push", BACKUP_REMOTE_NAME, current_branch], cwd=target_path)
    logging.info("Push scheint erfolgreich gewesen zu sein.")
    
    # remove remote
    logging.info("Entferne temporären Remote '%s'.", BACKUP_REMOTE_NAME)
    run_command(["git", "remote", "remove", BACKUP_REMOTE_NAME], cwd=target_path)
    logging.info("Remote '%s' wurde entfernt.", BACKUP_REMOTE_NAME)

if __name__ == "__main__":
    main()
