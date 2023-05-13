import tkinter as tk
from tkinter.font import Font
import datetime
import os
import time

os.chdir(os.path.dirname(os.path.realpath(__file__)))


tssl = 1000
tsslh = 1000
timesh = "%H:%M:%S"
current_time = datetime.datetime.now().strftime(timesh)
current_date = datetime.datetime.now().strftime("%d.%m.%y")
seed = "H_M_S"

local_tz_offset = datetime.datetime.now(datetime.timezone.utc).astimezone().utcoffset()
offset_hours = local_tz_offset // datetime.timedelta(hours=1)
offset_minutes = local_tz_offset // datetime.timedelta(minutes=1) % 60
if offset_hours >= 0:
    offset_str = "+{:02d}:{:02d}".format(offset_hours, offset_minutes)
else:
    offset_str = "-{:02d}:{:02d}".format(abs(offset_hours), offset_minutes)



GTM_list = ["-12:00", "-11:00", "-10:00", "-09:30", "-09:00", "-08:00", "-07:00",
            "-06:00", "-05:00", "-04:30", "-04:00", "-03:30", "-03:00", "-02:00",
            "-01:00", "+00:00", "+01:00", "+02:00", "+03:00", "+03:30", "+04:00",
            "+04:30", "+05:00", "+05:30", "+05:45", "+06:00", "+06:30", "+07:00",
            "+08:00", "+08:45", "+09:00", "+09:30", "+10:00", "+10:30", "+11:00",
            "+12:00", "+12:45", "+13:00", "+14:00"]


dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'data', 'background.txt')
dir_path1 = os.path.dirname(os.path.realpath(__file__))
file_path1 = "icon.png"
dir_path3 = os.path.dirname(os.path.realpath(__file__))
file_path3 = os.path.join(dir_path, 'data', 'gmt.txt')
dir_path5 = os.path.dirname(os.path.realpath(__file__))
file_path5 = os.path.join(dir_path, 'data', 'info(py).txt')

def overwrite_to_none():
    with open(file_path, "r+") as f:
        f.seek(0)
        f.truncate()
        f.write("None")
        print("Closed")


def uufts():
    global tsslh
    global tssl
    tsslh = 1
    tssl = 1

def ufts():
    global tsslh
    global tssl
    tsslh = 100
    tssl = 100

def fts():
    global tsslh
    global tssl
    tsslh = 1000
    tssl = 1000

def sts():
    global tsslh
    global tssl
    tsslh = 5000
    tssl = 5000
    

def sh_m():
    global umo
    global timesh
    global seed
    seed="H_M"
    timesh = "%H:%M"
    if umo == 1:
        rmumo()
def sh_m_s():
    global umo
    global timesh
    global seed
    timesh = "%H:%M:%S"
    seed = "H_M_S"
    if umo == 1:
        rmumo()
def sh_m_s_ms():
    global umo
    global seed
    global timesh
    seed = "H_M_S_MS"
    timesh = "%H:%M:%S.%f"
    if umo == 1:
        rmumo()
    

# Funkce, které změní velikost textu
def set_font_size(font_size):
    clock_font.configure(size=font_size)
    date_font.configure(size=int(font_size/2))
    if font_size == 25:
        root.minsize(200, 100)
    elif font_size == 50:
        pass
    elif font_size == 75:
        root.minsize(480, 280)
    else:
        root.minsize(300, 200)
        global glfont_size
        glfont_size = font_size



def update_labels_when_umo():
    current_time = datetime.datetime.now().strftime(timesh)
    clock_label.config(text=current_time)
    root.after(tssl, update_labels_when_umo) 



umo = 0

def rumo():
    global umo
    global seed
    global glfont_size
    if umo == 0:
        set_font_size(25)
        current_date = ""
        if seed == "H_M_S":
            root.minsize(200, 80)
            root.maxsize(200, 80)
        elif seed == "H_M":
            root.minsize(200, 80)
            root.maxsize(200, 80)
        elif seed == "H_M_S_MS":
            root.minsize(300, 80)
            root.maxsize(300, 80)
        umo = 1
        update_labels_when_umo()
    elif umo == 1:
        set_font_size(50)
        root.minsize(300, 200)
        root.geometry("400x300")
        root.maxsize(5000, 5000)
        umo = 0
        update_labels()
        if glfont_size == 25:
            root.minsize(200, 100)
        elif glfont_size == 50:
            root.minsize(300, 200)
        elif glfont_size == 75:
            root.minsize(480, 280)
        else:
            root.minsize(300, 200)
        

    else:
        print("UMT není dostupné")

def rmumo():
    global seed
    set_font_size(25)
    current_date = ""
    if seed == "H_M_S":
        root.minsize(200, 80)
        root.maxsize(200, 80)
    elif seed == "H_M":
        root.minsize(200, 80)
        root.maxsize(200, 80)
    elif seed == "H_M_S_MS":
        root.minsize(300, 80)
        root.maxsize(300, 80)
    update_labels_when_umo()
   

def close_app():
    root.destroy()
    
def copy_time():
    root.clipboard_clear()
    if seed == "H_M_S":
        root.clipboard_append(datetime.datetime.now().strftime("%H:%M:%S"))
    elif seed == "H_M":
        root.clipboard_append(datetime.datetime.now().strftime("%H:%M"))
    elif seed == "H_M_S_MS":
        root.clipboard_append(datetime.datetime.now().strftime("%H:%M:%S.%f"))
    else:
        root.clipboard_append(datetime.datetime.now().strftime("%H:%M:%S"))
        

def copy_date():
    root.clipboard_clear()
    root.clipboard_append(datetime.datetime.now().strftime("%d.%m.%Y"))

def set_window_topmost():
    root.attributes("-topmost", True)

def set_window_not_topmost():
    root.attributes("-topmost", False)


        


def show_GTM_menu():
    global GTM_var
    global GTM_menu    
    global GTM_window
    GTM_window = tk.Toplevel(root)
    GTM_window.minsize(80, 80)
    GTM_window.geometry("200x100")
    GTM_window.maxsize(500, 500)
    GTM_window.title("Nastavení GTM pásem")
    clock_label = tk.Label(GTM_window, text="Nastav tvé časové pásmo")
    GTM_var = tk.StringVar(value=offset_str)
    GTM_menu = tk.OptionMenu(GTM_window, GTM_var, *GTM_list)
    clock_label.pack()
    GTM_menu.pack()
    GTM_window.protocol('WM_DELETE_WINDOW', write_gmt)
    #hisrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    
def write_gmt():
    with open(file_path3, "r+") as f:
        f.seek(0)
        f.truncate()
        f.write(GTM_var.get())
        GTM_window.destroy()

def changeto_none():
    global backc
    backc = None
    with open(file_path, "r+") as f:
        f.seek(0)
        f.truncate()
        f.write("None")
    root.config(bg="white")
    clock_label.config(bg="white")
    date_label.config(bg="white")

def changeto_blue():
    global backc
    backc = "#87CEFA"
    with open(file_path, "r+") as f:
        f.seek(0)
        f.truncate()
        f.write("#87CEFA")
    root.config(bg="#87CEFA")
    clock_label.config(bg="#87CEFA")
    date_label.config(bg="#87CEFA")

def changeto_pink():
    global backc
    backc = "pink"
    with open(file_path, "r+") as f:
        f.seek(0)
        f.truncate()
        f.write("pink")
    root.config(bg="pink")
    clock_label.config(bg="pink")
    date_label.config(bg="pink")

def changeto_green():
    global backc
    backc = "#90ee90"
    with open(file_path, "r+") as f:
        f.seek(0)
        f.truncate()
        f.write("#90ee90")
    root.config(bg="#90ee90")
    clock_label.config(bg="#90ee90")
    date_label.config(bg="#90ee90")
    


def backgrnd():
    back_window = tk.Toplevel(root)
    back_window.minsize(300, 250)
    back_window.title("Nastavení pozadí")
    clock_label = tk.Label(back_window, text="Nastav si pozadí", font=Font(size=30))
    clock_label.pack()
    button = tk.Button(back_window, text="Žádné",command=lambda: changeto_none())
    button.pack()
    nl1 = tk.Label(back_window, text="")
    button2 = tk.Button(back_window, text="Světle Modrá Obloha",bg="#87CEFA", command=lambda: changeto_blue())
    button2.pack()
    nl2 = tk.Label(back_window, text="")
    button3 = tk.Button(back_window, text="Světlá Růžová", bg="pink", command=lambda: changeto_pink())
    button3.pack()
    nl3 = tk.Label(back_window, text="")
    button4 = tk.Button(back_window, text="Limetková Zelená", bg="#90ee90", command=lambda: changeto_green())
    button4.pack()
   

def openupd():
    roott.destroy()
    os.system("python upd.py")


def openiu():
    root.destroy()
    os.system("python upd.py")

#def use_local():
#    with open(file_path3, "r+") as f:
#        f.seek(0)
#        f.truncate()
#        f.write(offset_str)
#    neshodujese.destroy()
#    
#    
#def keep_saved():
#    global offset_str
#    with open(file_path3, "r+") as f:
#        ojoj = f.read()
#        offset_str = ojoj
#    neshodujese.destroy()


def more_info():
    mi_window = tk.Toplevel(root)
    mi_window.minsize(300, 250)
    mi_window.title("Informace o aplicakci")
    with open(file_path5, "r+") as f:
        info = f.read()
        mi_label = tk.Label(mi_window, text=info, font=Font(size=12))
        mi_label.pack()



def show_work():
    work_window = tk.Toplevel(root)
    work_window.minsize(300, 250)
    work_window.title("Aplikace ve vývoji")
    cllock_label = tk.Label(work_window, text="Aplikace je teprve ve vývoji,\nnachází se zde proto spousta chyb a nedokončených funkcí, budume proto rádi, když budete trpěliví.\n\n Váš tým 'Hodiny'\n\n\n", font=Font(size=8))
    cllock_label.pack()
    button4 = tk.Button(work_window, text="Více informací", command=lambda: more_info())
    button4.pack()


with open(file_path, "r+") as f:
    backc = f.read()
    
if backc == "None":
    backc = None
    
#green "#90ee90"
#None
#pink
#blue "#87CEFA"

known_colors = ["pink", "None", "#90ee90", "#87CEFA"]

with open(file_path, "r+") as f:
    reade = f.read()
    if reade in known_colors:
        backc = reade
        if reade == "None":
            backc = None
    else:
        backc = None
        roott = tk.Tk()
        roott.geometry("400x300")
        roott.title("HODINY")
        roott.minsize(350, 200)
        label = tk.Label(roott, text="Barva v souboru background.txt není správně zapsána!\nBuď byla změněna uživatelem či programem. Zavři toto okno a zkus to znova.", font=Font(size=10))
        label.pack()
        label2 = tk.Label(roott, text="\n",)
        label2.pack()
        button = tk.Button(roott, text="Přenastavit", command=openupd)
        button.pack()
        with open(file_path, "r+") as f:
            f.seek(0)
            f.truncate()
            f.write("None")
        roott.mainloop()

def resandload():
    root.quit()
    root.mainloop()

# Vytvoření okna
root = tk.Tk()
root.geometry("400x300")
root.title("HODINY")
root.minsize(300, 200)
root.config(bg=backc)
GTM_var = tk.StringVar(value="+02:00")
root.config(root.iconphoto(True, tk.PhotoImage(file="icon.png")))


# Vytvoření menu
menu = tk.Menu(root)
root.config(menu=menu)


file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Soubor", menu=file_menu)

copy_menu = tk.Menu(file_menu, tearoff=False)
file_menu.add_cascade(label="Zkopírovat", menu=copy_menu)

copy_menu.add_command(label="Čas", command=copy_time)
copy_menu.add_command(label="Datum", command=copy_date)

file_menu.add_command(label="Restartovat", command=openiu)
file_menu.add_command(label="Zavřít", command=close_app)


display_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Zobrazení", menu=display_menu)

font_size_menu = tk.Menu(display_menu, tearoff=False)
display_menu.add_cascade(label="Velikost písma", menu=font_size_menu)

font_size_menu.add_command(label="Malé", command=lambda: set_font_size(25))
font_size_menu.add_command(label="Střední", command=lambda: set_font_size(50))
font_size_menu.add_command(label="Velké", command=lambda: set_font_size(75))


clock_menu = tk.Menu(display_menu, tearoff=False)
display_menu.add_cascade(label="Čas", menu=clock_menu)

clock_menu.add_command(label="Hodiny a minuty", command=lambda: sh_m())
clock_menu.add_command(label="Hodiny, minuty a sekundy", command=lambda: sh_m_s())
clock_menu.add_command(label="Hodiny, minuty, sekundy a milisekundy", command=lambda: sh_m_s_ms())

#image1_path = "images/bac1.png"
#image2_path = "images/bac2.png"
#image3_path = "images/bac3.png"
#image4_path = "images/bac4.png"
#icon_path = "images/icon.png"
#
#image1 = tk.PhotoImage(file=image1_path)
#image2 = tk.PhotoImage(file=image2_path)
#image3 = tk.PhotoImage(file=image3_path)
#image4 = tk.PhotoImage(file=image4_path)
#icon = tk.PhotoImage(file=icon_path)

timezone_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Nastavení", menu=timezone_menu)

timezone_menu.add_command(label="Časová pásma", command=show_GTM_menu)

topmost_menu = tk.Menu(timezone_menu, tearoff=False)
timezone_menu.add_cascade(label="Překrytí", menu=topmost_menu)

topmost_menu.add_command(label="Překrýt všechna okna", command=set_window_topmost)
topmost_menu.add_command(label="Nepřekrývat všechna okna", command=set_window_not_topmost)

update_menu = tk.Menu(timezone_menu, tearoff=False)
timezone_menu.add_cascade(label="Aktualizace", menu=update_menu)

update_menu.add_command(label="Ultra rychlá", command=lambda: uufts())
update_menu.add_command(label="Rychlá", command=lambda: ufts())
update_menu.add_command(label="Normální", command=lambda: fts())
update_menu.add_command(label="Pomalá", command=lambda: sts())


timezone_menu.add_command(label="Přepnout UMO", command=rumo)
timezone_menu.add_command(label="Nastavení pozadí", command=backgrnd)#bckgrnd


pomoc_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Pomoc", menu=pomoc_menu)
pomoc_menu.add_command(label="Info", command=more_info)


# Vytvoření labelů pro hodiny a datum
clock_font = tk.font.Font(family="Helvetica", size=50)
date_font = tk.font.Font(family="Helvetica", size=25)

clock_label = tk.Label(root, font=clock_font)
date_label = tk.Label(root, font=date_font)

clock_label.pack(pady=10)
date_label.pack(pady=10)

clock_label.configure(bg=backc)
date_label.configure(bg=backc)

# Funkce, která aktualizuje labely
def update_labels():
    global GTM_var
    global GTM_menu
    GTM_offset = datetime.timedelta(hours=int(GTM_var.get()[:3]), minutes=int(GTM_var.get()[4:]))
    current_time = datetime.datetime.now(datetime.timezone(GTM_offset)).strftime(timesh)
    current_date = datetime.datetime.now().strftime("%d.%m.%y")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(tssl, update_labels) # spustí funkci každou tssl

update_labels()

root.after(2000, show_work)

#
#with open(file_path3, "r+") as f:
#    ojojoj = f.read()
#    if ojojoj == offset_str:
#        pass
#    else:
#        neshodujese = tk.Toplevel(root)
#        neshodujese.minsize(250, 250)
#        neshodujese.geometry("500x300")
#        neshodujese.maxsize(500, 500)
#        neshodujese.config(bg=backc)
#        laabel = tk.Label(neshodujese, text="Uložené časové pásmo se neshoduje s aktuálním pásmem", font=Font(size=12), bg=backc)
#        laabel.pack()
#
#        button1 = tk.Button(neshodujese, text="Ponechat uložené", width=18, command=neshodujese.destroy)
#        button2 = tk.Button(neshodujese, text="Použít lokální", width=18, command=neshodujese.destroy)
#
#        button1.place(relx=0.5, rely=0.5, anchor=tk.E)
#        button2.place(relx=0.5, rely=0.5, anchor=tk.W)
        


root.mainloop()