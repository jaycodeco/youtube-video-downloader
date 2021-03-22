try:
    from logging import exception
    from tkinter import filedialog
    from pytube import YouTube
    import os
    from pytube.cli import on_progress
except Exception as e:
    print(e," not found")


savePath = "C:/Users/ACER/Downloads"
options = ["MP4(720P)","MP4(140P)","MP3"]
file_size =0

def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
    percent = (100*(file_size-remaining))/file_size
    print("{:00.0f}%  downloaded".format(percent))



def choose_path(part):
    global savePath;
    savePath = filedialog.askdirectory()
    part.config(text=savePath, font=(10))

def dwnVid(ch,urlv,log):
    choice = ch.get()
    url = urlv.get()
    mp3 = 0
    try:
        data = YouTube(url, on_progress_callback=on_progress)
        if(choice == options[0]):
            dwn = data.streams.filter(progressive=True).order_by('resolution').desc().first()
            mp3=0
        elif(choice == options[1]):
            dwn = data.streams.filter(progressive=True).order_by('resolution').desc().last()
            mp3=0
        elif(choice == options[2]):
            dwn = data.streams.filter(only_audio=True).first()
            mp3=1
            
        global file_size
        file_size = dwn.filesize   
        
        
        out_file = dwn.download(output_path=savePath)
        
        if(mp3==1):
            # save the file 
            base, ext = os.path.splitext(out_file) 
            new_file = base + '.mp3'
            os.rename(out_file, new_file) 
        
        log.config(text="Download Complete", font=(10), fg="green")
    except Exception as e:
        print("error: ",e)
        log.config(text="incorrect URL", font=(10))
        
        

file_size = 0