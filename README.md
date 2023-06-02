# VM Migration to Google Cloud Platform (GCP)

This repository contains a Python script that facilitates the migration of a virtual machine (VM) to Google Cloud Platform (GCP). The script allows you to create a GCP bucket, copy the VM files to the bucket, and import the VM into GCP.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed
- The `gcloud` command-line tool installed and authenticated with your GCP account
- The `gsutil` command-line tool installed (part of the Google Cloud SDK)

## Usage

1. Clone the repository and navigate to the project directory.

```bash
git clone <repository-url>
cd <repository-name>
```

2. Run the migration script.

```bash
python create_machine.py
```

### Contributing

Contributions are welcome! If you find any issues or want to add enhancements to the script, feel free to open an issue or submit a pull request.
