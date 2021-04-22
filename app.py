from tkinter import *
from tkinter import ttk
from functions import *


def save_file():
    choose_file()

def save_directory():
    choose_path(pathLbl)
    
def download_file():
    go(qlyBox.get(),urlEty.get(),logLbl)

root =Tk()
root.title("U-Down")
root.geometry("600x250")
root.iconbitmap("./favicon.ico")
root.columnconfigure(0,weight=1)
#root.overrideredirect(True) 


####_URL_####
urlLbl = Label(root,width=100, text="Enter the video URL",font=("jost",25))
urlLbl.grid(row=0,column=0, pady = 10, padx = 25)

urlValue = StringVar()
urlEty = Entry(root, width=100, textvariable=urlValue)
urlEty.grid(row=1,column=0, pady = 10, padx = 15)
####_end_###


####_Path selection_####
pathLbl = Label(root,text=savePath,font=("jost",10))
pathLbl.grid(column=0,row=3)

pathBtn = Button(root,text="Browse",font=("jost",15), command=save_directory)
pathBtn.grid(column=1,row=3)
####_end_###


####_Quqlity selection_####
qlyLbl = Label(root,text="choose the video quality",font=("jost",20))
qlyLbl.grid(column=0,row=4)

qlyBox = ttk.Combobox(root, value=options,font=("jost",15),width=10)
qlyBox.grid(column=1,row=4)
####_end_###


####_Download and errorStatus_####
dwnBtn = Button(root,text="download",font=("jost",15, 'bold', 'underline'),fg="green", command=download_file)
dwnBtn.grid(column=1,row=5)

fileBtn = Button(root,text="urls in file",font=("jost",10, 'bold'),fg="blue", command=save_file)
fileBtn.grid(column=1,row=0)

logLbl = Label(root,text="",font=("jost",15),fg="red")
logLbl.grid()
####_end_###


root.mainloop()