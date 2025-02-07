import datetime
import shutil
import os


def backup_files(file_path):
    """
    Create a backup copy of the specified file with timestamp.
    
    Args:
        file_path (str): Path to the file to backup
        
    Returns:
        str: Path to the backup file or None if backup failed
    """
    try:
        # Validate input file exists
        print(f"Current working directory: {os.getcwd()}")
        print(f"Validating source file: {os.path.exists(file_path)}")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Source file not found: {file_path}")

        print("Backing up files")
        
        # Create backup filename with timestamp
        backup_name = f"{file_path}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.bak"
        
        # Create backup copy
        shutil.copy2(file_path, backup_name)
        
        print(f"Backup created: {backup_name}")
        print("Done")
        
        return backup_name

    except (OSError, shutil.Error) as e:
        print(f"Error creating backup: {str(e)}")
        return None


if __name__ == '__main__':
    backup_files("scripts/python/test/template.yaml")

