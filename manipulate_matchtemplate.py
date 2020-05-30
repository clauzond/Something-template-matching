import numpy as np
from matplotlib import pyplot, image

from skimage.feature import match_template
from skimage.color import rgb2gray

"""
http://devdoc.net/python/scikit-image-doc-0.13.1/auto_examples/features_detection/plot_template.html
"""


def pattern_matching_withplot(searchimage, patternimage):
    """
    Effectue un pattern_matching avec affichage matplotlib

    searchimage : PIL image
    patternimage : PIL image
    """

    pix = np.array(searchimage, dtype=np.uint8)
    # On met les images en gray pour éviter les problèmes de trop grosses images
    my_image = rgb2gray(pix)

    pix = np.array(patternimage, dtype=np.uint8)
    my_pattern_image = rgb2gray(pix)

    # Result renvoie une image avec des coefficients de corrélation en guise de couleur
    result = match_template(image=my_image, template=my_pattern_image)

    # Pour trouver les coordonnées où le pattern a été trouvé
    # np.argmax renvoie l'indice (dans l'array applati en 1D) où se trouve le (premier) maximum
    # np.unravel_index permet, à partir de l'indice dans l'array applati en 1D, de retrouver l'indice dans l'array en dimension normale
    my_tuple = np.unravel_index(np.argmax(result), result.shape)
    x, y = my_tuple[::-1]  # ::-1 pour renverser, ij = (col,ligne)

    # result[y,x] est le coefficient de corrélation maximum trouvé
    my_max = result[y, x]

    if my_max > 0.4:
        print(
            f"Le pattern a été trouvé, avec un coefficient maximum : {my_max}")
        my_color = 'r'
    else:
        print(
            f"Le pattern n'a pas été trouvé, avec un coefficient maximum : {my_max}")
        my_color = 'r'

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
    if my_max > 0.4:
        ax3.set_title("Pattern trouvé")
    else:
        ax3.set_title("Pattern non trouvé")
    ax3.imshow(result)
    ax3.set_axis_off()

    ax3.autoscale(False)
    rectangle2 = pyplot.Rectangle(
        (x, y), width_pattern, height_pattern, edgecolor=my_color, facecolor="none")
    ax3.add_patch(rectangle2)
    ax3.plot(x, y, 'o', markeredgecolor='r',
             markerfacecolor="none", markersize=10)
    pyplot.show()
