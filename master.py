import tkinter as tk
import os
from tkinter import filedialog
import subprocess
import argparse
from PIL import Image, ImageTk
# Source - https://stackoverflow.com/a
# Posted by Rainer Niemann, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-07, License - CC BY-SA 4.0
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
####################################################################################################
root = tk.Tk()
root.iconbitmap(resource_path("ico.ico"))
root.title("konverti")
root.geometry("400x400")
dark_bg = "#1e1e1e"
dark_bar = "#0f0f0f"
dark_fg = "#ffffff"
accent = "#3a3a3a"
root.configure(bg=dark_bg)
parser = argparse.ArgumentParser(description="vecor")
parser.add_argument("--file", help="preselect a file")
menu_frame = tk.Frame(root, bg=dark_bar, width=200, height=400)
menu_frame.pack(side="left", fill="y")

      
container = tk.Frame(root, bg=dark_bg)
container.pack(pady=20)
sup_format = ['mp4','webm','mov','mkv','mp3','ogg','wav','flac','m4a','png','jpeg','jpg','avif','webp',"ico"]
pic = ['png','jpeg','jpg','avif','webp',"ico"]
vid = ['mp4','webm','mov','mkv','gif','mp3','ogg','wav']
audio = ['mp3','ogg','wav','flac','m4a']
tkvar = tk.StringVar()
current_widgets = {}  
args = parser.parse_args()



def browseFiles():
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    file_name = filedialog.askopenfilename(
        initialdir=downloads_path,
        title="Select a File",
        filetypes=(("All Files", "*.*"),)
    )
    if not file_name:
        return

    for w in current_widgets.values():
        w.destroy()
    current_widgets.clear()
 
    base = os.path.basename(file_name)
    ext = os.path.splitext(base)[1][1:]  
    name = os.path.splitext(base)[0][0:]  
    full = name
    if len(name + ext) >= 7:
        print(len(name+ext))
        half = (7 - 3) // 2
        name = name[:half] + "..." + name[-half:]
    name = name + f".{ext}"
    calculatefile(ext, name, file_name, full)

def calculatefile(format, filename, loc, fullname):
    if format in sup_format: 
        if format in pic:
            selfile = tk.Label(container, text=filename, bg=dark_bg, fg=dark_fg)
            selfile.pack(side="left", padx=5)
            current_widgets['label'] = selfile
            tkvar.set(pic[0])
            dah = tk.OptionMenu(container, tkvar, *pic)
            dah.config(bg=dark_bg, fg=dark_fg, activebackground=accent, activeforeground=dark_fg)
            dah.pack(side="left", padx=5)
            current_widgets['dropdown'] = dah
            choice = tkvar.get()
            convert = tk.Button(container, text="Convert", bg=accent, fg=dark_fg, command=lambda: clickoncal(loc,tkvar.get(),fullname))
            convert.pack(side="left", padx=5)
            current_widgets['button'] = convert
            current_widgets['label'].config(font=("Helvetica", 12, "bold"))
        elif format in audio:
            selfile = tk.Label(container, text=filename, bg=dark_bg, fg=dark_fg)
            selfile.pack(side="left", padx=5)
            current_widgets['label'] = selfile
            tkvar.set(audio[0])
            dah = tk.OptionMenu(container, tkvar, *audio)
            dah.config(bg=dark_bg, fg=dark_fg, activebackground=accent, activeforeground=dark_fg)
            dah.pack(side="left", padx=5)
            current_widgets['dropdown'] = dah
            current_widgets['label'].config(font=("Helvetica", 12, "bold"))

            choice = tkvar.get()
            convert = tk.Button(container, text="Convert", bg=accent, fg=dark_fg, command=lambda: clickoncal(loc,tkvar.get(),fullname))
            convert.pack(side="left", padx=5)
            current_widgets['button'] = convert
        elif format in vid:
            selfile = tk.Label(container, text=filename, bg=dark_bg, fg=dark_fg)
            selfile.pack(side="left", padx=5)
            current_widgets['label'] = selfile
            current_widgets['label'].config(font=("Helvetica", 12, "bold"))
            tkvar.set(vid[0])
            dah = tk.OptionMenu(container, tkvar, *vid)
            dah.config(bg=dark_bg, fg=dark_fg, activebackground=accent, activeforeground=dark_fg)
            dah.pack(side="left", padx=5)
            current_widgets['dropdown'] = dah
            choice = tkvar.get()
            convert = tk.Button(container, text="Convert", bg=accent, fg=dark_fg, command=lambda: clickoncal(loc,tkvar.get(),fullname))
            convert.pack(side="left", padx=5)
            current_widgets['button'] = convert
def clickoncal(loc, format, name):
    try:
        folder = os.path.dirname(loc)
        output_path = os.path.join(folder, f"{name}.{format}")
        process = subprocess.Popen(
            ["ffmpeg", "-i", loc, output_path],
            creationflags=subprocess.CREATE_NO_WINDOW
        )
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
def predef(file_name):

    if not file_name:
        return

    for w in current_widgets.values():
        w.destroy()
    current_widgets.clear()

 
    base = os.path.basename(file_name)
    ext = os.path.splitext(base)[1][1:]  
    name = os.path.splitext(base)[0][0:]  
    full = name

    calculatefile(ext, base, file_name,name)
if args.file:
    predef(args.file)
menu_frame.grid_columnconfigure(0, weight=0)
menu_frame.grid_rowconfigure(0, weight=0)

file_btn = tk.Button(menu_frame, text="File", bg=dark_bar, fg=dark_fg, activebackground=accent, activeforeground=dark_fg, bd=0, padx=10, pady=5, command=browseFiles, height=4,width=5)

file_btn.grid(row=0, column=0, sticky="w")

root.mainloop()
