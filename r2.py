from tkinter import filedialog
    
def readFile():
    savePath = filedialog.askopenfilename()
    rd = open(savePath, "r")
    out = rd.readlines()
    rd.close()
    return out

links = readFile()

for link in links:
    print("##--> ",link.replace('\n','.')," <--##\n")