from PIL import Image

def image2array(filename):

    img = Image.open(filename)
    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

    return pixels

def array2image(array):

    image = Image.fromarray(array) 

    return image

def getinfo(filename):

    img = Image.open(filename)
    width,height = img.size

    return (width, height)
