import sys
import telebot;

def changeFirstLetters(words):
    if len(words) < 2:
        return "Введи два любых слова"
    word1 = words[0]
    word2 = words[1]
    letter1 = word1[0]
    letter2 = word2[0]
    word1 = letter2 + word1[1:]
    word2 = letter1 + word2[1:]
return word1 + " " + word2

bot = telebot.TeleBot('5519104894:AAGw3YLcJfC3uzg4UMeCnXwiWDmRUIFLkgY');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    words = message.text.split()
    try:
        bot.send_message(message.chat.id, changeFirstLetters(words))
    except:
        bot.send_message(message.from_user.id, changeFirstLetters(words))



def test():
    print(changeFirstLetters(sys.argv[1:]))

def main():
    print()



bot.polling(none_stop=True, interval=0)
