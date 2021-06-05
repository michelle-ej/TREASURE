import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Retrieve the connection string for use with the application. The storage
    # connection string is stored in an environment variable on the machine
    # running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
    # created after the application is launched in a console or with Visual Studio,
    # the shell or application needs to be closed and reloaded to take the
    # environment variable into account.
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = str(uuid.uuid4())

    # Create the container
    container_client = blob_service_client.create_container(container_name)

    print("------")
    print(container_client)
    print(type(container_client))
    print("------")

    # Quick start code goes here
    # Create a local directory to hold blob data
    local_path = "./data"
    os.mkdir(local_path)

    # Create a file in the local data directory to upload and download
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file
    file = open(upload_file_path, 'w')
    file.write("Hello, World!")
    file.close()

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)
    
    # print("\nListing blobs...")

    # # List the blobs in the container
    # blob_list = container_client.list_blobs()
    # for blob in blob_list:
    #     print("\t" + blob.name)

    # # Download the blob to a local file
    # # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
    # download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
    # print("\nDownloading blob to \n\t" + download_file_path)

    # with open(download_file_path, "wb") as download_file:
    #     download_file.write(blob_client.download_blob().readall())

    # # Clean up
    # print("\nPress the Enter key to begin clean up")
    # input()

    # print("Deleting blob container...")
    # container_client.delete_container()

    # print("Deleting the local source and downloaded files...")
    # os.remove(upload_file_path)
    # os.remove(download_file_path)
    # os.rmdir(local_path)

    print("Done")


except Exception as ex:
    print('Exception:')
    print(ex)

#參考網址:https://docs.microsoft.com/zh-tw/azure/storage/blobs/storage-quickstart-blobs-python