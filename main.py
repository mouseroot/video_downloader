#Simple interface for yt-dlp
import subprocess
import os

def main():
    while 1:
        try:
            url = input("Url: ")
            fname = input("Filename: ")
            status = download_video(url, fname)
            if status == True:
                print("Download Complete")
            else:
                print(status)
        except KeyboardInterrupt:
            break
    print("Program End!")
    

def download_video(url, pathname):
    vid_path = os.getcwd()
    vid_path = os.path.join(vid_path,"Videos")
    vid_path = os.path.join(vid_path,pathname)
    # -q for quiet
    cmd = f'yt-dlp {url} -q -o "{vid_path}.mp4"'
    # getstatusoutput returns the exit code and the stdout
    status,text = subprocess.getstatusoutput(cmd)
    if status == 0:
        return True
    else:
        return text




def list_files():
    cwd = os.getcwd()
    path = os.path.join(cwd,"Videos")
    files_txt = os.listdir(path)
    files = []
    for file in files_txt:
        files.append(os.path.join(path,file))
    for i,vid in enumerate(files):
        print(f"{i}\t{vid}")
    try:
        sel = int(input("Play Which? "))
        if sel in range(0,len(files)):
            vpath = os.path.join(path,files[sel])
            os.system(f'"{vpath}"')
        else:
            list_files()
    except KeyboardInterrupt:
        return
        


def menu():
    files = os.listdir(os.path.join(os.getcwd(),"Videos"))
    display = f"""
    Video Downloader (yt-dlp)
    1. Download a new video
    2. Play a video [{len(files)} Videos]
    3. Exit (or Ctrl+C)
"""
    while 1:
        print(display)
        try:
            sel = int(input("? "))
            if sel in range(0,4):
                if sel == 1:
                    main()
                elif sel == 2:
                    list_files()
                elif sel == 3:
                    return
        except KeyboardInterrupt:
            return



menu()
