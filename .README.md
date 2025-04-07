# ADF Metadata Ingestion Pipeline 🚀

This project uploads local files to Azure Blob Storage with versioning,
and automatically triggers an Azure Data Factory pipeline to extract and store metadata.

## ✅ Features

- Uploads files to Azure Blob with timestamped filenames
- Triggers ADF pipeline immediately after upload
- Extracts both folder and per-file metadata
- Combines metadata into a single .json and stores in a metadata container

## 🛠️ Technologies Used

- Python
- Azure Blob Storage
- Azure Data Factory
- GitHub

## 🚀 Getting Started

1. Configure `raw_ingestion.py` with your Azure Storage + ADF details
2. Run:

```bash
python raw_ingestion.py