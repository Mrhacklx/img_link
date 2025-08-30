# Custom Image Uploader

This is a simple Python FastAPI app to upload images and return a direct URL.

## Deploy on Render

1. Push this repo to GitHub.
2. Go to Render Dashboard → New → Web Service.
3. Connect your GitHub repo.
4. Environment: Python 3
5. Build Command: `pip install -r app/requirements.txt`
6. Start Command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
7. Deploy!
