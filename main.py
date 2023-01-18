import tkinter as tk
from tkinter import filedialog
from yt_dlp import YoutubeDL
import os


def open_popup(texto, names):
    top = tk.Toplevel(app)
    top.geometry("200x30")
    top.title(names)
    tk.Label(top, text=texto).place(x=0, y=0)


def download_video():
    link = link_entry.get()
    output_path = filedialog.asksaveasfilename(defaultextension=".webm")

    if output_path == "":
        return

    filename = "tempo.webm"
    args = {'ignoreerrors': True,
            'outtmpl': filename}

    with YoutubeDL(args) as ydl:
        ydl.download(link)

    input_path = "tempo.webm"

    if output_path.endswith(".webm"):
        os.rename(input_path, output_path)
    else:
        os.system(f'ffmpeg.exe -y -i "{input_path}" "{output_path}"')
        os.remove(input_path)

    open_popup("Done!", "process finished")


app = tk.Tk()
app.title("YouTube downloader")
app.geometry("280x100")

link_label = tk.Label(text="YT link:")
link_label.pack()
link_entry = tk.Entry()
link_entry.pack()

download_button = tk.Button(text="Download Videos", command=download_video)
download_button.pack()

app.mainloop()
