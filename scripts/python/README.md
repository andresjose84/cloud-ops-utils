# Cloud Ops Utils - Python Scripts

This directory contains various Python scripts designed to assist with cloud operations tasks. Each script is documented below with its purpose, usage scenarios, and provided solutions.

## Available Scripts

Here's a list of the currently available scripts in this directory:

| Script Name | Description | Primary Use Case |
|-------------|-------------|------------------|
| check_disk_space.py | Monitors disk space usage and alerts on threshold breach | Server space monitoring |

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

## Usage

Execute scripts as follows:

```bash
git clone https://github.com/andresjose84/cloud-ops-utils.git 
cd cloud-ops-utils/scripts/python
python check_disk_space.py
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create your feature branch
3. Submit a pull request
