from matplotlib import pyplot, image
from PIL import Image


def open_image_and_resize(filename, size):
    """
    filename: full filename (C:/.../image.jpg)
    size: tuple (size1,size2)

    return: PIL image (manipulable avec matplotlib)
    """
    img = Image.open(filename)
    img = img.resize((size[0], size[1]), Image.ANTIALIAS)
    return(img)


def open_image(filename):
    img = Image.open(filename)
    return(img)


if __name__ == "__main__":
    filename = "C:/Users/Utilisateur/Desktop/Python/-- GITKRAKEN/Something template matching/images/luma_pattern_full.jpg"
    img = open_image_and_resize(filename, size=(36, 36))
    pyplot.imshow(img)
    pyplot.show()
