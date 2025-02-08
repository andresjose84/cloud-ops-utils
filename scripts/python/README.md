# Cloud Ops Utils - Python Scripts

This directory contains various Python scripts designed to assist with cloud operations tasks. Each script is documented below with its purpose, usage scenarios, and provided solutions.

## Table of Contents

- [Overview](#cloud-ops-utils---python-scripts)
- [Available Scripts](#available-scripts)
- [Disk Space Monitoring](#real-devops-scenario-disk-space-monitoring)
  - [check_disk_space.py](#check_disk_spacepy)
- [File Backup Management](#real-devops-scenario-file-backup-management)
  - [backup_files.py](#backup_filespy)
- [Log Rotation](#real-devops-scenario-automate-log-rotation)
  - [rotate_logs.py](#rotate_logspy)
- [Service Monitoring](#real-devops-scenario-service-status-monitoring)
  - [check_service_status.py](#check_service_statuspy)
- [Contributing](#contributing)

## Available Scripts

Here's a list of the currently available scripts in this directory:

| Script Name | Description | Primary Use Case |
|-------------|-------------|------------------|
| check_disk_space.py | Monitors disk space usage and alerts on threshold breach | Server space monitoring |
| backup_files.py | Creates timestamped backup copies of files | File backup before modifications |
| rotate_logs.py | Validates the log folder and moves logs older than the retention period | Moves old log files|
| check_service_status.py | Checks the status of specified services | Service status monitoring |

## Real DevOps Scenario: Disk Space Monitoring

### check_disk_space.py

**Problem Statement:**  
Server performance degradation due to disk space issues requires proactive monitoring and alerting.

**Key Features:**

- Monitors disk space usage in real-time
- Configurable alert thresholds
- Email notifications when space is critical
- Detailed space usage reporting

**Technical Implementation:**

- Utilizes Python's `shutil` library for disk metrics
- Implements alert system for threshold breaches
- Generates formatted reports of disk usage

## Real DevOps Scenario: File Backup Management

### backup_files.py

**Problem Statement:**  
When making changes to critical configuration files or scripts, it's essential to maintain backup copies to prevent data loss and enable quick rollback if needed.

**Key Features:**

- Creates timestamped backup copies of files
- Validates source file existence
- Preserves file metadata
- Returns the path to the backup file
- Includes error handling and logging

**Technical Implementation:**

- Uses Python's `shutil` library for file operations
- Implements datetime stamping for unique backup names
- Maintains original file permissions and timestamps
- Provides detailed operation logging

**Usage Example:**

```python
from backup_files import backup_files

# Create a backup of a configuration file
backup_path = backup_files("text/template.yaml")
if backup_path:
    print(f"Backup created successfully at: {backup_path}")
```

## Usage

Execute scripts as follows:

```bash
git clone https://github.com/andresjose84/cloud-ops-utils.git 
cd cloud-ops-utils/scripts/python
python backup_files.py
```

## Real DevOps Scenario: Automate Log Rotation

### rotate_logs.py

**Problem Statement:**  
Logs are critical, but they shouldn't fill your disk. Automate log cleanup and archiving with Python.

**Scenario:**

- Your server generates logs daily, and older logs are consuming space
- You need a solution to move or delete logs older than a specific number of days

## Usage

Execute scripts as follows:

```bash
git clone https://github.com/andresjose84/cloud-ops-utils.git 
cd cloud-ops-utils/scripts/python
python rotate_logs.py
```

## Real DevOps Scenario: Service Status Monitoring

### check_service_status.py

**Problem Statement:**  
Ensuring that critical services are running is essential for maintaining system health and availability.

**Key Features:**

- Checks the status of specified services
- Provides clear output on service status
- Handles errors gracefully

**Technical Implementation:**

- Uses Python's subprocess library to interact with system services
- Checks the status of services using systemctl
- Prints the status of each service

**Usage Example:**

```python
from check_service_status import check_service_status

# Check the status of multiple services
check_service_status("nginx")
check_service_status("apache2")
check_service_status("mysql")
check_service_status("docker")
```

**Usage**
Execute scripts as follows:

```bash
git clone https://github.com/andresjose84/cloud-ops-utils.git 
cd cloud-ops-utils/scripts/python
python check_service_status.py
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create your feature branch
3. Submit a pull request
