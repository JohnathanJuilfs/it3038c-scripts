from PIL import Image
from PIL import ImageFilter
#Takes image and outputs 3 edits of that image, one image is blurred, one is turned into a thumbnail,and one is embossed

OrgImage = Image.open("fox.jpg")

blurImage = OrgImage.filter(ImageFilter.BLUR)
blurImage.show()
blurImage.save("blur.jpg")


def thumbnails():
    try:
        image = Image.open("fox.jpg")
        image.thumbnail((90,90))
        image.save("thumbnail.jpg")
        image1 = Image.open("thumbnail.jpg")
        image1.show()
    except IOError:
        pass


thumbnails()


im = Image.open("fox.jpg")

im1 = im.filter(ImageFilter.EMBOSS)
im1.show()
im1.save("Emboss.jpg")