from PIL import ImageGrab

def get_screenshot(x1=None, y1=None, x2=None, y2=None):
    """
    Renvoie l'image contenue dans le rectangle [(x1,y1), (x2,y2)]
    return: image manipulable avec le module "image" de matplotlib
    """
    if y2 is None:
        return(ImageGrab.grab())
    else:
        return(ImageGrab.grab(bbox=(x1, y1, x2, y2)))


if __name__ == "__main__":
    from matplotlib import pyplot, image

    my_screenshot = get_screenshot(x1=80, y1=80, x2=1807, y2=1000)

    pyplot.imshow(my_screenshot)
    pyplot.show()
