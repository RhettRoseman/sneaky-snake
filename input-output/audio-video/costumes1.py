
# This script takes multiple images as command-line arguments and creates a new GIF file called costumes.gif 
# this is my own version of the script that includes error handling and a more detailed output message

import sys
from PIL import Image

# Create a new empty list called images
images = []

# Check if there are any command-line arguments
if len(sys.argv) < 2:
    print("Usage: python script.py image1.jpg image2.png ...")
    sys.exit(1)

# For loop to create a new image and append to the images list
for arg in sys.argv[1:]:
    try:
        image = Image.open(arg)
        images.append(image)
    except Exception as e:
        print(f"Error opening {arg}: {e}")

# Check if there are any images in the list
if not images:
    print("No valid images to process")
    sys.exit(1)

# Save the images to a new file called costumes.gif
images[0].save(
    "costumes.gif", save_all=True, append_images=images[1:], loop=0, duration=200
)

print("costumes.gif created successfully")
   