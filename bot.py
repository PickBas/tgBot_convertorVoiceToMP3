import telebot
import config
import soundfile as sf

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Welcome, {0.username}!\nSend me a voice message!".format(message.from_user))


@bot.message_handler(content_types=['voice'])
def audio_handler(message):
    print(message)
    file_info = bot.get_file(message.voice.file_id)
    print(file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    f = open('file.ogg', 'wb')
    f.write(downloaded_file)
    f.close()
    # data, samplerate = sf.read(downloaded_file)
    # sf.write('new_file.wav', data, samplerate)
    bot.send_voice(message.chat.id, downloaded_file)


bot.polling(none_stop=True)
