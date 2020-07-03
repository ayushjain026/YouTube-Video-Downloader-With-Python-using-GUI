import pafy
import youtube_dl
from functools import partial
from tkinter import messagebox as msg
from pytube import YouTube
from tkinter.filedialog import *
import tkinter as tk

root = tk.Tk()


width = 500
height = 400
root.geometry(f"{width}x{height}")
root.minsize(490, 380)
root.maxsize(510, 550)
root.title(f"Youtube Video Downloader   {os.getcwd()}")
filename = os.getcwd()


video_ls = []
aa = []
temp = []


def download_selected(video_ls):
    Label(root, text="Download in Progress 👍", bg='orange red', font = "Algerian 12 bold", fg = "white").grid(row=20, columnspan=6)
    a = root.grid_slaves(row=19)
    for l in a:
        l.destroy()
    display.insert(INSERT, 'Getting video details \nInitializing your download sequence')
    ok = msg.askokcancel('Dear User','Once you start Download you can not pause it\nWant to continue?')
    print(var.get())
    b = var.get()
    if ok:
        display.insert(INSERT, '\nWe are downloading your file in background to achieve \nMAX Download Speed\n')

        try:
            print(video_ls[b], type(video_ls))
            video_ls[b].download()
            msg.showinfo("Thank You","Your download is Complete😁")
            display.insert(INSERT, "video downloaded Sucessfully\n")
            a = root.grid_slaves(row=19)
            for l in a:
                l.destroy()
            clr()
        except:
            msg.showwarning('Error occured','Please re-try after some time\n Or try with some different Resolution')
    else:
        display.insert(INSERT, 'Progress cancelled\n')


def download():
    Label(root, text="Compiling your video Please Wait*", font = "Algerian 12 bold", fg = "white", bg='orange red').grid(row=20, columnspan=6, pady=3)
    a = root.grid_slaves(row=19)
    for l in a:
        l.destroy()

    msg.showinfo('Wait',"Getting Video Information!!")
    display.insert(INSERT, "Getting Video Information!!\n")
    a = link_url.get()
    try:
        myVideo = YouTube(a)
    except:
        clr()
    myVideo = YouTube(a)
    video = pafy.new(a)
    display.insert(INSERT, f"Title: {myVideo.title}\n")
    display.insert(INSERT, f"Rating: {myVideo.rating}\n")

    for i in myVideo.streams.filter(mime_type="video/mp4"):
        ii = str(i)
        if ii.find('res="240p" fps="30fps"') > 1 or ii.find('res="360p" fps="30fps"') > 1 or ii.find('res="720p" fps="30fps"') > 1 or ii.find('res="1080p" fps="30fps"') > 1:
            if ii not in video_ls:
                video_ls.append(i)

    for i in video_ls:
        i = str(i)
        b = i.split()
        aa.append(b)

    for i in range(len(video_ls)):
        temp.append(aa[i][3])

    for i in range(len(aa)):
        for j in range(i + 1, len(aa)):
            if i < len(aa) and j < len(aa):
                if aa[i][3] == aa[j][3]:
                    aa.remove(aa[j])
                    temp.pop(j)
                    video_ls.pop(j)

    global c, radio
    c = 1
    # radio = Radiobutton()
    for i in video_ls:
        i = str(i)
        if i.find('res="144p"') > 1:
            radio = Radiobutton(root, text=f'Resolution = 144px ()', value=c, variable = var)
            print(f"144 {c}")
            radio.grid(row=8, columnspan=6)
            c = c + 1

        elif i.find('res="240p"') > 1:
            radio = Radiobutton(root, text=f'Resolution = 240px', value=c, variable = var)
            radio.grid(row=9, columnspan=6)
            print(f'240 {c}')
            c = c + 1

        elif i.find('res="360p"') > 1:
            radio = Radiobutton(root, text=f'Resolution = 360px', value=c, variable = var)
            radio.grid(row=10, columnspan=6)
            print(f'360 {c}')
            c = c + 1

        elif i.find('res="720p"') > 1:
            radio = Radiobutton(root, text=f'Resolution = 720px', value=c, variable = var)
            radio.grid(row=11, columnspan=6)
            print(f'720 {c}')
            c = c + 1

        elif i.find('res="1080p"') > 1:
            radio = Radiobutton(root, text=f'Resolution = 1080px', value=c, variable = var)
            radio.grid(row=12, columnspan=6)
            print(f'1080 {c}')
            c = c + 1
        radio.deselect()
    width1 = 500
    height1 = 550
    root.geometry(f'{width1}x{height1}')

    stream = video.streams
    no=13
    for i in stream:
        no = no + 1
        size = int(i.get_filesize()) / (1024)
        size = round(size, 2)
        if size < 1024:
            Label(root, text=f"{i.resolution}, {size}Kb").grid(row=no, columnspan=6)
        else:
            size = size / 1024
            size = round(size, 3)
            Label(root, text=f"{i.resolution}, {size}Mb").grid(row=no, columnspan=6)
        Label(root, text=f'Video duration: {video.duration}Sec').grid(row=5,columnspan=6)
    l = [19, 20]
    for ls in l:
        a = root.grid_slaves(row=ls)
        for l in a:
            l.destroy()

    a = Label(root, text="In which quality u want to Download?").grid(row=18, columnspan=6)
    Button(root, text="Download", command=partial(download_selected, video_ls)).grid(row=19, column=2)


def save():
    file = askdirectory()
    os.chdir(file)
    a = root.grid_slaves(row=3)
    for l in a:
        l.destroy()
    Label(root, text=f"Your default download location is \n{file}").grid(row=3, columnspan=6)


def clr():
    print(filename)
    link_url.delete(0,END)
    video_ls.clear()
    temp.clear()
    aa.clear()
    lis = [5,8,9,10,11,12,14,15,16,18,20]
    for i in lis:
        a = root.grid_slaves(row=i)
        for l in a:
            l.destroy()
    Button(root, text="Download", command=download).grid(row=20, column=2, pady=3)
    root.geometry('500x400')


Label(root, text="This application is made by Ayush Jain to download youtube videos",font ="comicsansms 10 bold").grid(row=0, columnspan=5, pady=15, padx= 30)
Label(root, text="Copy and past your Youtube link here 👇").grid(row=1, columnspan=6)
link=StringVar
link_url = Entry(root, textvariable="link", width=30)
link_url.grid(row=2, columnspan=6, pady=15)
var = IntVar()
display = tk.Text(root, height=9, width=55, font = "Georgia 8 bold")
display.grid(row=25, columnspan=6, pady = 5)
s=Scrollbar(root,orient='vertical')
s.place(x=470,y=224,height=135)

display.config(yscrollcommand=s.set)
s.config(command=display.yview)
s.set(0,0)

display.insert(INSERT, "Your Statue:\n")

location = Label(root, text=f"Your default download location is \n{filename}").grid(row=3, columnspan=6)

Button(root, text="Change", command=save).grid(row=4, column=2, pady=2)
Button(root, text="Download", command=download).grid(row=19, column=2, pady=3)

# vsbar = Scrollbar(display, orient="vertical")
# vsbar.grid(row=26, column=7)


root.mainloop()
