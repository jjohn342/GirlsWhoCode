from PIL import Image

def load_img(pic):
    im = Image.open(pic)
    return im

def show_img(pic):
    pic.show()

def save_img(im, mulan):
    pic.save(mulan)


im = load_img("mulan.jpg")
show_img(im)
save_img(im, "mulan.jpg")
