import datetime
import os
import shutil


def rotate_logs(log_dir, archive_dir, days_to_retain=7):
    """
    Rotate log files from source directory to archive directory based on age.
    
    Args:
        log_dir (str): Source directory containing log files
        archive_dir (str): Target directory for archived logs
        days_to_retain (int): Number of days to keep logs before archiving
    """
    if not os.path.exists(log_dir):
        raise ValueError(f"Log directory does not exist: {log_dir}")
    
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
        
    now = datetime.datetime.now()
    
    for log_file in os.listdir(log_dir):
        file_path = os.path.join(log_dir, log_file)
        if os.path.isfile(file_path):
            try:
                modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                
                if (now - modified_time).days > days_to_retain:
                    timestamp = now.strftime("%Y%m%d_%H%M%S")
                    archive_name = f"{os.path.splitext(log_file)[0]}_{timestamp}{os.path.splitext(log_file)[1]}"
                    archive_path = os.path.join(archive_dir, archive_name)
                    
                    shutil.move(file_path, archive_path)
                    print(f"Archived log file: {log_file} -> {archive_name}")
            except OSError as e:
                print(f"Error processing file {log_file}: {str(e)}")


rotate_logs("logs", "archive", 1)