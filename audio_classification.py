import requests

API_URL = "https://api-inference.huggingface.co/models/MIT/ast-finetuned-audioset-10-10-0.4593"
headers = {"Authorization": "Bearer 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"}


def audio_classification(filename):
    with open(filename, "rb") as f:
        data = f.read()  # Read the file content as binary data
    # Send the POST request with the audio data
    response = requests.post(API_URL, headers=headers, data=data)
    # Return the JSON response from the API
    return response.json()
