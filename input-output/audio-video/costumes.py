import sys 

# from pillow library import Image
from PIL import Image

# a new empty array called image
images = []

# for loop to create a new image
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
# save the images to a new file called costumes.gif    
output_file = "costumes.gif"
images[0].save(output_file, save_all=True, append_images=images[1:], loop=2, duration=200)