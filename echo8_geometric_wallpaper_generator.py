from PIL import Image, ImageDraw, ImageFilter
import random

# Set the size of the image
width, height = 1280, 800

# Create a blank image with a black background
image = Image.new("RGBA", (width, height), (10, 10, 10, 255))
draw = ImageDraw.Draw(image)

# Function to add blurry circles
def add_blurry_circle(draw, center, radius, color, blur_radius):
    # Create a circle image
    circle_image = Image.new("RGBA", (radius*2, radius*2), (0, 0, 0, 0))
    circle_draw = ImageDraw.Draw(circle_image)
    circle_draw.ellipse((0, 0, radius*2, radius*2), fill=color)
    circle_image = circle_image.filter(ImageFilter.GaussianBlur(blur_radius))

    # Paste the circle image onto the main image
    image.paste(circle_image, (center[0]-radius, center[1]-radius), circle_image)

# Parameters for the circles
num_circles = 200
blur_strength = 2  # Adjust this value to control the blur strength
random.seed(0)
for _ in range(num_circles):
    center = (random.randint(0, width), random.randint(0, height))
    radius = random.randint(50, 250)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), int(random.uniform(50, 150)))
    add_blurry_circle(draw, center, radius, color, blur_strength)

# Convert the image to RGB (required for saving as JPG)
rgb_image = image.convert("RGB")

# Save the image as a JPG file
rgb_image.save("soothing_blurry_circles.jpg", "JPEG")

print("Image saved as soothing_blurry_circles.jpg")

