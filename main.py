import os
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET'),
    secure=True
)

def upload_image(file):
    if not os.getenv('API_KEY'):
        raise Exception("Cloudinary credentials are not configured.")
    
    result = cloudinary.uploader.upload(file)
    return result["secure_url"]
