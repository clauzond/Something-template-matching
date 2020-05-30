import numpy as np
from matplotlib import pyplot, image

from skimage import data
from skimage.feature import match_template
from skimage.color import rgb2gray

from random import randint





def luma_pattern_matching(image_dir, pattern_name, image_name="", _type="normal"):

    if _type == "normal":
        image_name = image_name

    elif _type == "random":
        r = randint(1, 6)
        image_name = f"{r}.jpg"
        print(f"Image {r} sélectionnée")

    elif _type == "input":
        image_name = str(
            input("Entrez le nom de l'image (si autre que .jpg, préciser l'extension) :\n> "))
        if len(image_name.split('.'))==1:
            image_name = f"{image_name}.jpg"

    my_image_rgb = image.imread(f"{image_dir}/{image_name}")
    pix = np.array(my_image_rgb, dtype=np.uint8)
    # On met les images en gray pour éviter les problèmes de trop grosses images
    my_image = rgb2gray(pix)

    my_pattern_image_rgb = image.imread(f"{image_dir}/{pattern_name}")
    pix = np.array(my_pattern_image_rgb, dtype=np.uint8)
    my_pattern_image = rgb2gray(pix)

    # Result renvoie une image avec des coefficients de corrélation en guise de couleur
    result = match_template(image=my_image, template=my_pattern_image)

    # Pour trouver les coordonnées où le pattern a été trouvé
    # np.argmax renvoie l'indice (dans l'array applati en 1D) où se trouve le (premier) maximum
    # np.unravel_index permet, à partir de l'indice dans l'array applati en 1D, de retrouver l'indice dans l'array en dimension normale
    ij = np.unravel_index(np.argmax(result), result.shape)
    x, y = ij[::-1]  # ::-1 pour renverser, ij = (col,ligne)

    # result[y,x] est le coefficient de corrélation maximum trouvé
    my_max = result[y, x]

    if my_max > 0.4:
        print(f"Le pattern a été trouvé, avec un coefficient maximum : {my_max}")
        my_color = 'r'
    else:
        print(f"Le pattern n'a pas été trouvé, avec un coefficient maximum : {my_max}")
        my_color = 'y'

    fig = pyplot.figure(figsize=(8, 3))
    ax1 = pyplot.subplot(1, 3, 1)
    ax2 = pyplot.subplot(1, 3, 2)
    ax3 = pyplot.subplot(1, 3, 3, sharex=ax2, sharey=ax2)

    ax1.imshow(my_pattern_image, cmap=pyplot.cm.gray)
    ax1.set_axis_off()
    ax1.set_title('Pattern à trouver')

    ax2.imshow(my_image, cmap=pyplot.cm.gray)
    ax2.set_axis_off()
    ax2.set_title('Image à analyser')

    height_pattern, width_pattern = my_pattern_image.shape

    rectangle = pyplot.Rectangle(
        (x, y), width_pattern, height_pattern, edgecolor=my_color, facecolor="none")
    ax2.add_patch(rectangle)

    ax3.imshow(result)
    ax3.set_axis_off()
    ax3.set_title("Résultat")
    ax3.autoscale(False)
    rectangle2 = pyplot.Rectangle(
        (x, y), width_pattern, height_pattern, edgecolor=my_color, facecolor="none")
    ax3.add_patch(rectangle2)
    ax3.plot(x, y, 'o', markeredgecolor='b',
             markerfacecolor="none", markersize=10)
    pyplot.show()


if __name__ == "__main__":
    image_dir = "C:/Users/Utilisateur/Desktop/Python/-- GITKRAKEN/Some image template matching/images"
    pattern_name = "luma_pattern.jpg"

    luma_pattern_matching(image_dir = image_dir, pattern_name=pattern_name, _type="input")