import os
import base64
import logging
import chardet
from bs4 import BeautifulSoup
from mimetypes import guess_type

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def img_to_base64(img_path):
    """Convert image to base64, supporting multiple formats."""
    try:
        mime_type, _ = guess_type(img_path)  # Guess the MIME type based on file extension
        if not mime_type or not mime_type.startswith('image/'):
            logger.warning(f"Unsupported file type: {img_path}")
            return None

        with open(img_path, "rb") as img_file:
            base64_encoded = base64.b64encode(img_file.read()).decode('utf-8')
            return f"data:{mime_type};base64,{base64_encoded}"
    except Exception as e:
        logger.error(f"Error converting image to base64: {e}")
        return None

def process_html(file_path, exclude_images=None, supported_exts=None):
    """Update image sources to base64, excluding specified images and supporting multiple extensions."""
    if exclude_images is None:
        exclude_images = []
    if supported_exts is None:
        supported_exts = ['.png', '.jpg', '.jpeg', '.gif']  # Add or remove extensions as needed

    logger.info(f"Processing file: {file_path}")

    try:
        with open(file_path, 'rb') as f:
            rawdata = f.read()
            result = chardet.detect(rawdata)
            char_encoding = result['encoding']

        with open(file_path, 'r', encoding=char_encoding) as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            
            for img_tag in soup.find_all('img'):
                img_src = img_tag.get('src', '')
                
                if img_src in exclude_images or not any(img_src.endswith(ext) for ext in supported_exts):
                    logger.info(f"Skipping image: {img_src}")
                    continue
                
                img_abs_path = os.path.join(os.path.dirname(file_path), img_src)
                if os.path.exists(img_abs_path):
                    logger.info(f"Found image: {img_src}")
                    img_base64 = img_to_base64(img_abs_path)
                    if img_base64:
                        img_tag['src'] = img_base64
                else:
                    logger.warning(f"Image not found: {img_src}")
                        
        with open(file_path, 'w', encoding=char_encoding) as file:
            file.write(str(soup))
    except Exception as e:
        logger.error(f"Error processing HTML file {file_path}: {e}")

def main():
    exclusions = ['barcode.png', 'qrcode.png']
    supported_extensions = ['.png', '.jpg', '.jpeg', '.gif']  # Update this list based on the image types you want to support

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                process_html(os.path.join(root, file), exclude_images=exclusions, supported_exts=supported_extensions)

if __name__ == "__main__":
    main()
