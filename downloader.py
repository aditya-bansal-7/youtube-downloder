from pytube import YouTube
import telebot
import uuid
import os

bot = telebot.TeleBot("6926359359:AAHthiiSibxSzDRSEZpXaZW7fdUCP7rOMAE")

@bot.message_handler(commands=['start'])
def start_message_sender(message):
    bot.send_message(message.chat.id,"This bot is created by @bnsl_boy , send me any Youtube url you want to dwonload !!")


@bot.message_handler(func=lambda message: True)
def all_message_handler(message):
    if message.text.startswith("https://youtu.be/"):
        downloader(message.text,message.chat.id)

def downloader(url,chat_id):
    try:
        bot.send_message(chat_id,"🔎")
        data = YouTube(url)
        stram = data.streams.filter(progressive=True , file_extension="mp4").get_highest_resolution()
        ms = bot.send_message(chat_id,"Processing 🔎....")
        file_path = stram.download()
        with open(file_path, 'rb') as video:
            bot.send_message(chat_id,"Sending Your Video !!")
            bot.send_chat_action(chat_id , "upload_video")
            bot.send_video(chat_id, video)
        os.remove(file_path)
    except Exception as e:
        bot.send_message(f"Got an Error : {e}")
        print("Invalid URL",   e)


if __name__ == "__main__":
    bot.polling()

# import tkinter as tk
# from tkinter import filedialog

# def open_filedialog():
#     folder = filedialog.askdirectory()
#     if folder:
#         print(f"Selected Folder : {folder}")
#     return folder

# if __name__ == "__main__":
    # root = tk.Tk()
    # root.withdraw()
    # video_url = input("Please enter a Youtube url : ")
    # save_dir = open_filedialog()
    # if save_dir:
    #     downloader(video_url,save_dir)
