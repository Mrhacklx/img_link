import requests

# Example using ImgBB (replace with adult-friendly API if needed)
API_KEY = "YOUR_API_KEY"
UPLOAD_URL = "https://api.imgbb.com/1/upload"

def upload_image_to_host(image_bytes, filename):
    """
    Upload image bytes to hosting service and return direct URL
    """
    payload = {
        "key": API_KEY,
        "image": image_bytes
    }
    response = requests.post(UPLOAD_URL, files={"image": image_bytes})
    if response.status_code == 200:
        data = response.json()
        return data['data']['url']
    else:
        raise Exception(f"Upload failed: {response.status_code} {response.text}")
