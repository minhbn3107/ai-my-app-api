import requests

API_URL = "https://api-inference.huggingface.co/models/audeering/wav2vec2-large-robust-24-ft-age-gender"
headers = {"Authorization": "Bearer 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"}


def gender_recognition(filename):
    with open(filename, "rb") as f:
        data = f.read()  # Read the file content as binary data
    # Send the POST request with the audio data
    response = requests.post(API_URL, headers=headers, data=data)
    # Return the JSON response from the API
    return response.json()
