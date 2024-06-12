import os
from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the context to be prepended to the prompt
context = "This is for senior residents living in a care home"
prompt = "volleyball"

def generate_image_from_text(prompt):
    full_prompt = f"{context}: {prompt}"
    response = client.images.generate(
        model="dall-e-3",
        prompt=full_prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    
    image_url = response.data[0].url
    return image_url

def save_image_from_url(image_url, prompt):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img = img.convert("RGB")
    
    # Center crop the image to 1280x800
    target_width, target_height = 1280, 800
    width, height = img.size
    left = (width - target_width) / 2
    top = (height - target_height) / 2
    right = (width + target_width) / 2
    bottom = (height + target_height) / 2
    img = img.crop((left, top, right, bottom))
    
    # Create a valid filename from the prompt
    valid_filename = "".join([c if c.isalnum() or c in " ._" else "_" for c in prompt])
    file_name = f"{valid_filename}.jpg"
    
    img.save(file_name, format="JPEG")
    return file_name

# Example usage
image_url = generate_image_from_text(prompt)
saved_file = save_image_from_url(image_url, prompt)

print(f"Image saved as '{saved_file}'")
