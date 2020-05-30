if __name__ == "__main__":
    from manipulate_screenshot import get_screenshot
    from manipulate_image import open_image_and_resize
    from manipulate_window import search_for_window_coords, get_foregrounds_coords
    from manipulate_matchtemplate import pattern_matching_withplot
    from matplotlib import pyplot, image

    dirname = "C:/Users/Utilisateur/Desktop/Python/-- GITKRAKEN/Something template matching/images"
    pattern_full = "luma_pattern_full.jpg"
    name_to_search = "Photos"

    # Pour le jeu en 1920x1080, pattern_full doit être resize en (36,36)
    coords = search_for_window_coords(name_to_search=name_to_search, offset=0)
    if coords is None:
        coords = get_foregrounds_coords(offset=0)
    x1, y1, x2, y2 = coords
    print(coords)
    width = x2 - x1
    height = y2 - y1

    ratio = 1920 / width

    print("ratio w :", 1920 / width, "ratio h:", 1080 / height)

    patternsize = int(36 / ratio)

    patternname = f"{dirname}/{pattern_full}"
    patternimage = open_image_and_resize(
        filename=patternname, size=(patternsize, patternsize))

    screenimage = get_screenshot(x1=x1, y1=y1, x2=x2, y2=y2)

    pattern_matching_withplot(searchimage=screenimage,
                              patternimage=patternimage)
