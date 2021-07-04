from base64 import b64encode
from pathlib import Path
import json
import googleapiclient.discovery
from oauth2client.client import GoogleCredentials

# Settings
IMAGE_FILE = 'starbucks_01.jpg'
CREDENTILS_FILE = 'credentials.json'

# Connect to the Google Cloud-ML Service
credentials = GoogleCredentials.from_stream(CREDENTILS_FILE)
service = googleapiclient.discovery.build('vision', 'v1', credentials=credentials)

# Read file and convert it to a base64 encoding
with open(IMAGE_FILE, "rb") as f:
    image_data = f.read()
    encoded_image_data = b64encode(image_data).decode('UTF-8')

# Create the request object for the Google Vision API
batch_request = [{
    'image':{
        'content': encoded_image_data
    },
    'features':[
        {
            'type': 'LABEL_DETECTION'
        }
    ]
}]

request = service.images().annotate(body={'requests': batch_request})

# Send the request to Google
response = request.execute()

# Check for errors
if 'error' in response:
    raise RuntimeError(response['error'])

# Print the results
labels = response['responses'][0]['labelAnnotations']


# Save the response
json_object = json.dumps({"img": IMAGE_FILE, "labels": labels}, indent =4)
f = Path("google-cloud-vision-api-response.json")
f.write_text(json_object)

for label in labels:
    # print(label['description'], label['score'])
    print("likelihood that this image contains {} is {}%".format(label['description'], int(label['score']*100)))

