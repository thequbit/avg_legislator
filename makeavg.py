import sys
import glob

from image2array import image2array,array2image, getinfo

def get_image_list(directory):
    
    filelist = glob.glob("{0}/*.jpg".format(directory))

    return filelist

def togray(pixel):

    try:
        r,g,b = pixel
        val = int((r * .33) + (g * .34) + (b * .33))
    except:
        val = pixel

    if val > 255:
        val = 255

    return val

def main(argv):

    if len(argv) != 2:
        print "Usage:\n\tpython makeavg.py <dir_name>\n"
        return

    print "Starting ..."

    directory = argv[1]

    filelist = get_image_list(directory)

    width,height = getinfo(filelist[0])

    sums = {}
    for i in range(0,(width*height)):
        sums[i] = 0

    for imgfile in filelist[0:10]:
        array = image2array(imgfile)

        print "\tWorking on {0} ...".format(imgfile)
#        print getinfo(imgfile)

        count = 0
        for yarr in array:
            for xarr in yarr:
                sums[count] += togray(xarr)
                count += 1

        print "\tDone.\n"

    for i in range(0, (width*height)):
        sums[i] = sums[i]/(width*height)

    img = array2image(sums)

    print "Done."

if __name__ == '__main__': sys.exit(main(sys.argv))
