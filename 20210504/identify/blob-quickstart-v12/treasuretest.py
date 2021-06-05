import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    print(blob_service_client)
    # container name
    container_name = "treasurecontainer"
    print(container_name)
    # get the container
    container_client = blob_service_client.get_container_client(container_name)
    print(container_client)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="fuck.txt")
    print(blob_client)


    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)

    # Download the blob to a local file
    local_path = "./data"
    download_file_path = os.path.join(local_path,"fuck.txt")
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)


#參考網址:
# https://docs.microsoft.com/zh-tw/azure/storage/blobs/storage-quickstart-blobs-python
# https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient?view=azure-python