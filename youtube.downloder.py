from yt_dlp import YoutubeDL
import tkinter as tk
from tkinter import filedialog

def youtube_downloader(url, save_path, use_ffmpeg=True):
    try:
        # Configure options based on whether ffmpeg is installed
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        }
        
        if use_ffmpeg:
            ydl_opts.update({
                'format': 'bestvideo+bestaudio/best',  # Best video + audio streams
                'merge_output_format': 'mp4',         # Merge to MP4
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',          # Ensure output is MP4
                }]
            })
        else:
            ydl_opts.update({
                'format': 'best',  # Fallback to a single combined stream
            })
        
        # Download video
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input URL
url = "https://www.youtube.com/watch?v=ilcsiVdT5uI&ab_channel=IndiaTV".replace('/shorts/', '/watch?v=')

# Get the save path using a dialog
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory(title="Select Download Folder")

if path:
    # Ask the user if they have ffmpeg installed
    use_ffmpeg = input("Do you have ffmpeg installed? (yes/no): ").strip().lower() == "yes"
    youtube_downloader(url, path, use_ffmpeg)
else:
    print("Download folder not selected!")

