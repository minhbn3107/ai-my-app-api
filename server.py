from flask import Flask, request, jsonify
from download_audio import download_audio
from gender_recognition import gender_recognition
from language_identification import language_identification
from audio_classification import audio_classification
import uuid
import os

app = Flask(__name__)

# Create the 'music-download' folder if it doesn't exist
DOWNLOAD_FOLDER = "music-download"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

print("Server is running...")


@app.route("/api/gender-recognition", methods=["POST"])
def take_gender():
    url = request.json.get("url")
    filename = os.path.join(DOWNLOAD_FOLDER, uuid.uuid4().hex + ".mp3")
    downloaded_file = download_audio(url, filename)
    if downloaded_file:
        output = gender_recognition(downloaded_file)
        print(output)
        return jsonify(output), 200
    else:
        return jsonify({"error": "Failed to download the audio file."}), 500


@app.route("/api/language-identification", methods=["POST"])
def take_language():
    url = request.json.get("url")
    filename = os.path.join(DOWNLOAD_FOLDER, uuid.uuid4().hex + ".mp3")
    downloaded_file = download_audio(url, filename)
    if downloaded_file:
        output = language_identification(downloaded_file)
        print(output)
        return jsonify(output), 200
    else:
        return jsonify({"error": "Failed to download the audio file."}), 500


@app.route("/api/audio-classification", methods=["POST"])
def tale_classification():
    url = request.json.get("url")
    filename = os.path.join(DOWNLOAD_FOLDER, uuid.uuid4().hex + ".mp3")
    downloaded_file = download_audio(url, filename)
    if downloaded_file:
        output = audio_classification(downloaded_file)
        print(output)
        return jsonify(output), 200
    else:
        return jsonify({"error": "Failed to download the audio file."}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
