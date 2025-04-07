from azure.storage.blob import BlobServiceClient # type: ignore
import os

# Configuration
STORAGE_ACCOUNT_NAME = "candidatedata1"
STORAGE_ACCOUNT_KEY = os.getenv("AZURE_STORAGE_KEY")
CONTAINER_NAME = "raw"
LOCAL_FOLDER_PATH = "/Users/vysalidevabhaktuni/Desktop/algebra_it/projects/input_files/"

# Build connection string
connection_string = (
    f"DefaultEndpointsProtocol=https;"
    f"AccountName={STORAGE_ACCOUNT_NAME};"
    f"AccountKey={STORAGE_ACCOUNT_KEY};"
    f"EndpointSuffix=core.windows.net"
)

# Connect to blob service
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Upload all files in the folder
for filename in os.listdir(LOCAL_FOLDER_PATH):

    local_file_path = os.path.join(LOCAL_FOLDER_PATH, filename)

    if os.path.isfile(local_file_path):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        versioned_filename = f"{os.path.splitext(filename)[0]}_{timestamp}{os.path.splitext(filename)[1]}"
        blob_client = container_client.get_blob_client(versioned_filename)
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"✅ Uploaded '{filename}' to container '{CONTAINER_NAME}'.")
    else:
        print(f"🚫 Skipped '{filename}' (not a file)")

print("🚀 All files uploaded successfully.")