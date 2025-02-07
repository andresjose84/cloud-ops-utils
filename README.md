# 🌥️ cloud-ops-utils

## 📋 Table of Contents

- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
- [Requirements](#-requirements)
- [Contributing](#-contributing)
- [License](#-license)

A collection of useful scripts and configurations for DevOps and cloud operations.  
This repository contains Bash scripts, Python scripts, Docker deployments, Kubernetes configurations, Terraform templates, and more.

## 📂 Repository Structure

```
cloud-ops-utils/
│── scripts/
│   ├── bash/       # Bash scripts for automation
│   ├── python/     # Python scripts for cloud operations
│── deployments/
│   ├── docker/     # Docker configurations and deployments
│   ├── k8s/        # Kubernetes manifests and Helm charts
│── terraform/      # Infrastructure as Code (IaC) templates
│── README.md       # Project documentation
```

## 🚀 Getting Started

1. **Clone the repository**

    ```sh
    git clone https://github.com/andresjose84/cloud-ops-utils.git
    cd cloud-ops-utils
    ```

2. **Explore and use the scripts**

    ```sh
    # Bash scripts
    cd scripts/bash && ./your-script.sh

    # Python scripts
    cd scripts/python && python your-script.py

    # Docker deployments
    cd deployments/docker && docker-compose up

    # Kubernetes
    cd deployments/k8s && kubectl apply -f your-manifest.yaml

    # Terraform
    cd terraform && terraform init && terraform apply
    ```

## 🛠️ Requirements

- Docker
- Kubernetes
- Terraform
- Python 3
- Bash

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
