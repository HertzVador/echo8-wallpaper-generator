import os
from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the context to be prepended to the prompt
context = "This is for senior residents living in a care home"

def generate_image_from_text(prompt):
    full_prompt = f"{context}: {prompt}"
    response = client.images.generate(
        model="dall-e-3",
        prompt=full_prompt,
        n=1,
        size="1024x1024"  # Use a supported size
    )
    
    image_url = response.data[0].url
    return image_url

def save_image_from_url(image_url, prompt):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img = img.convert("RGB")
    
    # Resize image to 1280x800
    img = img.resize((1280, 800), Image.LANCZOS)
    
    # Create a valid filename from the prompt
    valid_filename = "".join([c if c.isalnum() or c in " ._" else "_" for c in prompt])
    file_name = f"{valid_filename}.jpg"
    
    img.save(file_name, format="JPEG")
    return file_name

# Example usage
prompt = "happy fathers day"
image_url = generate_image_from_text(prompt)
saved_file = save_image_from_url(image_url, prompt)

print(f"Image saved as '{saved_file}'")

