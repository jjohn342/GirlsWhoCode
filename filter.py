# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(pic):
    im = Image.open(pic)
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(pic):
    pic.show()

# Define your save_img() function here.
#      2 Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(pic, panda):
    pic.save(panda)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
# def obamicon(pic):
im = load_img("panda.jpg")
show_img(im)
save_img(im, "panda.jpg")
