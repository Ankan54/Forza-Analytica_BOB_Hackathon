import requests
import json

#url = 'https://{}/speechtotext/v3.0/transcriptions'.format('eastus.api.cognitive.microsoft.com')
url= "https://eastus.api.cognitive.microsoft.com/speechtotext/v3.0/transcriptions/"

headers = {"Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": "<<Enter Key>>"}

json_data = {
    "contentContainerUrl": 
    "https://bobhackathonstorage.blob.core.windows.net/raw?sp=rl&st=2022-10-22T08:29:15Z&se=2022-10-22T13:29:15Z&spr=https&sv=2021-06-08&sr=c&sig=fTP4QtASquXU44WKaWbDYaCMjUdJhZbGsO4zkBCwMyU%3D"
    ,
  "properties": {
    "diarizationEnabled": "true",
    "wordLevelTimestampsEnabled": "false",
    "punctuationMode": "DictatedAndAutomatic",
    "profanityFilterMode": "Masked",
    "destinationContainerUrl": "https://bobhackathonstorage.blob.core.windows.net/processed?sp=wl&st=2022-10-22T08:35:19Z&se=2022-10-22T12:35:19Z&spr=https&sv=2021-06-08&sr=c&sig=U5E4fBe%2BnPdrHT68hiDx1WOSwPw482D5TfH120uPDf8%3D" 
  },
  "locale": "en-US",
  "displayName": "transcripting test audio files and store them in destination container"
}

response = requests.post(url, headers=headers, json=json_data)
#response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
 
