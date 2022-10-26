import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    #print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here
    connect_str = "DefaultEndpointsProtocol=https;AccountName=<<Storage account name>>;AccountKey=<<Storage account key>>;EndpointSuffix=core.windows.net"
    
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    #### create storage container
    # container_name = 'testcontainer'
    # container_client = blob_service_client.create_container(container_name)
    
    ### get list of files in a container
    container_client=  blob_service_client.get_container_client('raw')
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print(blob.name)

    ### download files from a container
    # download_file_path= ''
    # with open(download_file_path, "wb") as download_file:
    #     download_file.write(container_client.download_blob(blob.name).readall())

except Exception as ex:
    print('Exception:')
    print(ex)
