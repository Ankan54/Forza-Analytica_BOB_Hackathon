import requests
import json

#url = 'https://{}/speechtotext/v3.0/transcriptions'.format('eastus.api.cognitive.microsoft.com')
url= "https://eastus.api.cognitive.microsoft.com/speechtotext/v3.0/transcriptions/"

headers = {"Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": "<<Enter Key>>"}

json_data = {
    "contentContainerUrl": 
    "<<Enter SAS URI of the source container>>"
    ,
  "properties": {
    "diarizationEnabled": "true",
    "wordLevelTimestampsEnabled": "false",
    "punctuationMode": "DictatedAndAutomatic",
    "profanityFilterMode": "Masked",
    "destinationContainerUrl": "<<Enter SAS URI of the destination container>>" 
  },
  "locale": "en-US",
  "displayName": "transcripting test audio files and store them in destination container"
}

response = requests.post(url, headers=headers, json=json_data)
#response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
