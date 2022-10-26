import json, os, requests, uuid

key= "<<Enter key>>"
endpoint = "https://api.cognitive.microsofttranslator.com/"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "eastus"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'hi',
    'to': ['en']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

file_path= '<<local file path>>'
with open(file_path, "r", encoding='utf-8') as json_file:
        json_dict = json.load(json_file)
    
input_text= json_dict['combinedRecognizedPhrases'][0]['lexical']

# You can pass more than one object in body.
body = [{
    'text': f'{input_text}'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(request.status_code)
print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
