## Video Downloader

A very simple wrapper for yt-dlp that works by looping input

1. Download files in a loop untill Control-C is used to break the loop (All videos are saved in the Videos directory)
2. Play a video or file from the Videos directory
3. Exit

### Example Usage - Listing Video files
```
PS C:\Users\user\Documents\Python> python .\video_downloader.py

    Video Downloader (yt-dlp)  
    1. Download a new video    
    2. Play a video [16 Videos]
    3. Exit (or Ctrl+C)        

? 2
0       C:\Users\user\Documents\Python\Videos\2500 HTTP Requests with Async & Await.mp4
1       C:\Users\user\Documents\Python\Videos\Arcade Station 80s 👾️ Synthwave # Retrowave # Cyberpunk [SUPERWAVE] 🚗 Vaporwave Music Mix.mp4
? 1
```

### Example Usage - Downloading Videos
```
PS C:\Users\user\Documents\Python> python .\video_downloader.py

    Video Downloader (yt-dlp)  
    1. Download a new video    
    2. Play a video [16 Videos]
    3. Exit (or Ctrl+C)        

? 1
Url: https://www.youtube.com/watch?v=nFn4_nA_yk8
Filename: Python - Async & Requests
Download Complete
Url:
```

