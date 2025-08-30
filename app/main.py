from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.utils import upload_image_to_host

app = FastAPI(title="Custom Image Uploader")

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    """
    Upload an image and return the direct link
    """
    try:
        content = await file.read()
        direct_url = upload_image_to_host(content, file.filename)
        return JSONResponse({"direct_url": direct_url})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
