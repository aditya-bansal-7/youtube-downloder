from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def downloader(url , save_path):
    try:
        data = YouTube(url)
        stram = data.streams.filter(progressive=True , file_extension="mp4").get_highest_resolution()
        stram.download(save_path)
        print("Video downloaded Sucessfully!")
    except:
        print("Invalid URL")


def open_filedialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder : {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    video_url = input("Please enter a Youtube url : ")
    save_dir = open_filedialog()
    if save_dir:
        downloader(video_url,save_dir)
