import telebot
import config
import subprocess
import os

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Welcome, {0.username}!\nSend me a voice message!".format(message.from_user))


def saving_file(df):
    f = open('file.ogg', 'wb')
    f.write(df)
    f.close()


def sanding_file(message):
    audio_file = open('file.mp3', 'rb')
    bot.send_audio(message.chat.id, audio_file)
    audio_file.close()


def removing_files():
    os.remove('./file.ogg')
    os.remove('./file.mp3')


@bot.message_handler(content_types=['voice'])
def audio_handler(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    saving_file(downloaded_file)
    subprocess.call(['ffmpeg', '-i', 'file.ogg', 'file.mp3'])
    sanding_file(message)
    removing_files()


bot.polling(none_stop=True)
