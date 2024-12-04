import time
import requests

# replace your vercel domain
base_url = 'https://music-api-two-delta.vercel.app'


def custom_generate_audio(payload):
    url = f"{base_url}/api/custom_generate"
    response = requests.post(url, json=payload, headers={
                             'Content-Type': 'application/json'})
    return response.json()


output = custom_generate_audio({
    "prompt": "Create an uplifting, energetic track that blends electronic dance music (EDM) with traditional Vietnamese instruments. The song should start with a serene melody played on a đàn tranh (Vietnamese zither), gradually building up with layers of electronic beats and synths. Incorporate a catchy, upbeat chorus that makes listeners want to dance, and add a bridge that features a soulful đàn bầu (Vietnamese monochord) solo. The track should evoke feelings of joy, celebration, and cultural fusion.",
    "make_instrumental": False,
    "wait_audio": False
})
print(output)
