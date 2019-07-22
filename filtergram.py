from filter import *

def obamicon(sun):

    darkblue = (0, 51, 76)
    red = (217, 26, 33)
    lightblue = (112, 150, 158)
    yellow = (252, 227, 166)

    color = list(im.getdata())
    list_len = len(color)

    for i in range(list_len):
        Red1 = color[i][0]
        Green1 = color[i][1]
        Blue1 = color[i][2]
        sum = Red1 + Green1 + Blue1

        if sum < 182:
            color [i] = darkblue
        elif sum > 182 and sum < 364:
            color [i] = red
        elif sum > 364 and sum < 546:
            color [i] = lightblue
        elif sum > 546:
            color [i] = yellow

    happysummer = im.putdata(color)
    def save_img(im, happysummer):
        im.save(happysummer)
    save_img(im, "happypanda.jpg")
    finalpic = load_img("happypanda.jpg")
    show_img(finalpic)

im = load_img("panda.jpg")
show_img(im)
obamicon(im)
