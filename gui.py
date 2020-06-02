from tkinter import *
from tkinter import messagebox
import keyboard
import time
from manipulate_screenshot import get_screenshot
from manipulate_image import open_image_and_resize
from manipulate_window import search_for_window_coords, get_foregrounds_coords
from manipulate_matchtemplate import pattern_matching_maxcoeff
from matplotlib import pyplot, image

"""
https://github.com/boppreh/keyboard
"""

def get_int(entry):
    try:
        return(int(entry.get()))
    except:
        entry.set("0")
        return(0)

def only_two_sides(haut,bas,gauche,droite):
    if (haut != 0 or bas !=0) and (gauche != 0 or droite != 0):
        var_haut.set("0")
        var_bas.set("0")
        var_gauche.set("0")
        var_droite.set("0")

        label_error.config(text="Seulement haut/bas ou gauche/droite !")

        return(0,0,0,0)
    else:
        label_error.config(text="")
        return(haut,bas,gauche,droite)


def check_entries(*args):
    haut = get_int(var_haut)
    bas = get_int(var_bas)
    gauche = get_int(var_gauche)
    droite = get_int(var_droite)

    haut,bas,gauche,droite = only_two_sides(haut,bas,gauche,droite)

# Options
dirname = "C:/Users/Utilisateur/Desktop/Python/-- GITKRAKEN/Something template matching/images"
pattern_full = "luma_pattern_full.jpg"
patternname = f"{dirname}/{pattern_full}"
name_to_search = "Lumas"
pattern_width = 36
pattern_height = 36


def searching_loop():
    # Take a screenshot
    coords = search_for_window_coords(name_to_search=name_to_search, offset=0)
    if coords is None:
        coords = get_foregrounds_coords(offset=0)
    x1, y1, x2, y2 = coords
    width = x2 - x1
    height = y2 - y1
    ratio_w = 1920 / width
    ratio_h = 1080 / height
    size = (int(pattern_width/ratio_w),int(pattern_height/ratio_h))

    patternimage = open_image_and_resize(filename=patternname,size=size)
    screenimage = get_screenshot(x1=x1,y1=y1,x2=x2,y2=y2)

    maximum = pattern_matching_maxcoeff(searchimage=screenimage, patternimage=patternimage)
    print(maximum)



_state = "menu"
def start_automatic_movement():
    global _state
    _state = "searching"



def stop_automatic_movement():
    global _state
    _state = "menu"
    return


def press_button(*args):
    if action_button['state'] != 'normal':
        return

    txt = action_button['text']
    if txt == "START":
        result = messagebox.askokcancel("Confirmation","Commencer le déplacement automatique ?")
        if result:
            action_button.config(text="STOP")

            start_automatic_movement()
        else:
            return
    else:
        result = messagebox.askokcancel("Annulation","Arrêter le déplacement automatique ?")
        if result:
            action_button.config(text="START")
            stop_automatic_movement()
        else:
            return
    
def add_shortcut(hotkey,function,args=()):
    keyboard.add_hotkey(hotkey=hotkey, callback=function, args=args)

def long_press(hotkey,_time):
    def loop_press(hotkey,time_max,time_current=0,t=None):
        if time_current < time_max:
            new_t = time.time()
            dt = new_t - t
            time_current += dt
            keyboard.press_and_release(hotkey=hotkey)

            keyboard.call_later(fn=loop_press,args=(hotkey,time_max,time_current,new_t), delay=0.2)
        else:
            return

    t = time.time()
    loop_press(hotkey=hotkey,time_max=_time,time_current=0,t=t)
    #keyboard.call_later(keyboard.release,args=(hotkey),delay=time)



    


print("Shortcut pour START/STOP ?")
_shortcut = keyboard.read_hotkey()
print(_shortcut)
add_shortcut(hotkey=_shortcut,function=press_button,args=())

add_shortcut(hotkey="a",function=long_press,args=("b",5))


main_window = Tk()

main_window.title("Pattern matching with Lumas")
main_window.resizable(False, False)
# main_window.iconbitmap("img/icone.ico")

main_window.option_add('*Font', 'Constantia 12')
main_window.option_add('*Button.relief', 'groove')
main_window.option_add('*Button.overRelief', 'flat')
main_window.option_add('*justify', 'center')
backgroundcolor = "#292826"
foregroundcolor = "#F9D342"

main_window.option_add('*background', backgroundcolor)
main_window.option_add('*foreground', foregroundcolor)
main_window.option_add('*compound', 'left')
main_window.configure(background=backgroundcolor)

c_width = 600
c_height = 200
main_canvas = Canvas(main_window, width=c_width, height=c_height)
main_canvas.pack(expand=True, fill='both', padx=10, pady=10)
main_canvas.update()
frame = Frame(main_canvas, width=c_width, height=c_height)
frame.grid(row=0, column=0, rowspan=999, columnspan=999)

_row = 2
_column = 2

label_info_text = "Entrer le nombre de blocs (haut/bas ou gauche/droite)"
label_info = Label(main_canvas, text=label_info_text)
label_info.grid(row=0, column=0, columnspan = 10)

label_error_text = ""
label_error = Label(main_canvas, text=label_error_text, fg="red")
label_error.grid(row=1, column=0, columnspan = 10)

var_haut = StringVar()
var_haut.set("0")
entry_haut = Entry(main_canvas, textvariable=var_haut)
entry_haut.grid(row=_row + 0, column=_column + 1, padx=10, pady=10)
# texte = var_haut.get()

var_bas = StringVar()
var_bas.set("0")
entry_bas = Entry(main_canvas, textvariable=var_bas)
entry_bas.grid(row=_row + 2, column=_column + 1, padx=10, pady=10)

var_gauche = StringVar()
var_gauche.set("0")
entry_gauche = Entry(main_canvas, textvariable=var_gauche)
entry_gauche.grid(row=_row + 1, column=_column + 0, padx=10, pady=10)

var_droite = StringVar()
var_droite.set("0")
entry_droite = Entry(main_canvas, textvariable=var_droite)
entry_droite.grid(row=_row + 1, column=_column + 2, padx=10, pady=10)

action_button = Button(main_canvas, text="START")
action_button.grid(row=_row + 1, column=_column + 1, padx=10, pady=10)

main_window.bind('<Button-1>',check_entries)
action_button.bind('<Button-1>',press_button)

main_window.mainloop()
