from grandfilters import *

def main():
    #change "file_name_here with your image link"
    myImg = load_img("panda.jpg")
    #pick one of the filters here
    newImg = cathy_grayscale(myImg)

    newImg.show()

main()
