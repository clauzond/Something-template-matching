import win32gui as wg

"""
http://timgolden.me.uk/pywin32-docs/contents.html
"""

def get_all_windows():

    def call(hwnd, param):
        if wg.IsWindowVisible(hwnd):
            param.append(hwnd)
    winds = []
    wg.EnumWindows(call, winds)
    return(winds)


def get_window_name(hwnd):
    return(wg.GetWindowText(hwnd))


def search_for_window(name_to_search):
    all_windows = get_all_windows()

    for hwnd in all_windows:
        if name_to_search in get_window_name(hwnd):
            return(True, hwnd)
    return(False, None)


def get_window_coords(hwnd, offset=8):
    """
    hwnd : Handle de fenêtre
    :return (x1, y1, x2, y2) coordonnées de la fenêtre
    """
    rect = wg.GetWindowRect(hwnd)
    x1, y1, x2, y2 = rect[0] + offset, rect[1] + offset, rect[2] + offset, rect[3] + offset

    return(x1, y1, x2, y2)


def search_for_window_coords(name_to_search, offset=8):
    """
    name_to_search : string concernant le nom de la fenêtre à chercher
    :return (x1, y1, x2, y2) coordonnées de la fenêtre en question, si elle est trouvée
    :return None si la fenêtre n'est pas trouvée
    """
    _bool, _hwnd = search_for_window(name_to_search)
    if _bool:
        return(get_window_coords(_hwnd, offset=offset))
    else:
        return(None)

def get_foregrounds_coords(offset=8):
    hwnd = wg.GetForegroundWindow()
    return(get_window_coords(hwnd = hwnd, offset=offset))


if __name__ == "__main__":
    #coords = search_for_window_coords(name_to_search="Photos")
    #print(coords)

    hwnd = wg.FindWindow(None,"Photos")
    print(get_window_coords(hwnd))