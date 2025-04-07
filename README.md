# 📦 ADF Metadata Pipeline

This project is an end-to-end solution that:
- 🗃 Uploads files to Azure Blob Storage (`raw/` container)
- 🧠 Extracts metadata for each file (size, schema, timestamp)
- 🔁 Loops through files and combines metadata
- 🌐 Sends the metadata as JSON to a `metadata/` container using Web activity in ADF

---

## 📂 Folder Structure

- `raw_ingestion.py` → Script to upload all files from local to Azure
- `.env` (ignored) → Stores sensitive keys
- `.gitignore` → Ensures sensitive/system files aren’t pushed

---

## 🚀 How to Use

1. Configure your `.env` file with Azure Storage credentials
2. Upload your CSV files into `raw/` container
3. Trigger the pipeline manually or on upload
4. Metadata JSON will be generated in the `metadata/` container

---

## 🛠 Technologies

- Azure Data Factory (ADF)
- Azure Blob Storage
- Python (BlobServiceClient)
- Git & GitHub

---

