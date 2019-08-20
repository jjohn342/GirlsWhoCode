from filter import *

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

    new_image2 = Image.new("RGB", (1000, 669), p)
    new_image2.putdata(color)
    return new_image2
