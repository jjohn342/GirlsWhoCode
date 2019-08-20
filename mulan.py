from filter import *

def obamicon(mulan):

    rose = (217, 136, 128)
    purple = (210, 180, 222)
    blue = (174, 214, 241)
    green = (171, 235, 198)


    color = list(im.getdata())
    list_len = len(color)


    for i in range(list_len // 2):
        Rose1 = color[i][0]
        Purple1 = color[i][1]
        Blue1 = color[i][2]
        sum = Rose1 + Purple1 + Blue1

        if sum < 160:
            color [i] = rose
        elif sum > 160 and sum < 250:
            color [i] = purple
        elif sum > 250 and sum < 360:
            color [i] = blue
        elif sum > 360 and sum < 456:
            color [i] = green


    happymulan = im.putdata(color)
    def save_img(im, happymulan):
        im.save(happymulan)
    save_img(im, "happymulan.jpg")
    finalpicture = load_img("happymulan.jpg")
    show_img(finalpicture)

im = load_img("mulan.jpg")
show_img(im)
obamicon(im)
