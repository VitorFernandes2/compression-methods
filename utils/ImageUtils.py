from PIL import Image
import io
import base64

def image_to_string(image_path, format):
    with open(image_path, "rb") as img_file:
        # Open the image using PIL
        img = Image.open(img_file)
        
        # Convert the image to bytes
        img_bytes = io.BytesIO()
        img.save(img_bytes, format)  # Convert the image to PNG format (you can use other formats as needed)
        img_bytes = img_bytes.getvalue()
        
        # Encode the image bytes to a Base64 string
        img_string = base64.b64encode(img_bytes).decode('utf-8')
        
        return img_string

# Path to your image file
image_path = '/home/vfernandes/Pictures/bg.jpg'  # Replace this with your image file path

# Convert the image to a string
image_string = image_to_string(image_path, "PNG")

# Print the encoded string
print("Encoded image string:", image_string)
