

import shutil


def check_disk_space( threshold = 80 ):
    total, used, free = shutil.disk_usage("/")
    usage = (used / total) * 100
    
    if usage > threshold:
        print(f"Warning: Disk usage is {usage:.2f}% which is over the threshold of {threshold}%")
        return False
    else:
        print(f"Disk usage is {usage:.2f}% which is under the threshold of {threshold}%")
        return True
    

check_disk_space()