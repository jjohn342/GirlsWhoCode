from filter import *

def obamicon(sun):

    darkblue = (0, 51, 76)
    red = (217, 26, 33)
    lightblue = (112, 150, 158)
    yellow = (252, 227, 166)

    color = list(im.getdata())
    list_len = len(color)

    for i in range(list_len // 2):
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

    happypanda = im.putdata(color)
    def save_img(im, happypanda):
        im.save(happypanda)
    save_img(im, "happypanda.jpg")
    finalpic = load_img("happypanda.jpg")
    show_img(finalpic)

im = load_img("panda.jpg")
show_img(im)
obamicon(im)

def pancon(panda):
    grey = (208, 211, 212)
    darkyellow = (110, 44, 0)
    lightgreen = (115, 198, 182)
    darkorange = (125, 102, 8)

    color = list(im.getdata())
    list_len = len(color)

    for i in range(list_len):
        Grey1 = color[i][0]
        darkyellow1 = color[i][1]
        Lightorange1 = color[i][2]
        sum = Grey1 + darkyellow1 + Lightorange1

        if sum < 182:
            color [i] = grey
        elif sum > 182 and sum < 364:
            color [i] = darkyellow
        elif sum > 364 and sum < 546:
            color [i] = lightgreen
        elif sum > 546:
            color [i] = darkorange

    sunpanda = im.putdata(color)
    def save_img(im, sunpanda):
        im.save(sunpanda)
    save_img(im, "sunpanda.jpg")
    newpic = load_img("sunpanda.jpg")
    show_img(newpic)

im = load_img("panda.jpg")
show_img(im)
pancon(im)
