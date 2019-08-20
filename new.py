from filter import *

def pancon(panda):
    grey = (208, 211, 212)
    darkyellow = (110, 44, 0)
    lightgreen = (115, 198, 182)
    darkblue = (93, 173, 226)

    color = list(im.getdata())
    list_len = len(color)

    for i in range(list_len // 2):
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
            color [i] = darkblue

    sunpanda = im.putdata(color)
    def save_img(im, sunpanda):
        im.save(sunpanda)
    save_img(im, "newchristmas.jpg")
    newpic = load_img("newchristmas.jpg")
    show_img(newpic)

im = load_img("christmas.jpg")
show_img(im)
pancon(im)
