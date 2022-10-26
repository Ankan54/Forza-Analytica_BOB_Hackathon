from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import os, json

connect_str = "<<Enter connection string>>"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_name = '<<Container name>>'
container_client=  blob_service_client.get_container_client(container_name)
blob_list = container_client.list_blobs(name_starts_with="<<>>")

text_data_list= []
for blob in blob_list:
        #print(blob.name)
    download_file_path= os.path.join(r"<<local_file_path>>", blob.name.split('/')[-1])
    with open(download_file_path, "wb") as download_file:
        download_file.write(container_client.download_blob(blob.name).readall())

    with open(download_file_path, "r") as json_file:
        json_dict = json.load(json_file)
    
    text_data_list.append(json_dict['combinedRecognizedPhrases'][0]['lexical'])

