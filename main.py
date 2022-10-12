import sys
import telebot;
VOWELS = "аоуэыяёюеи"
CONSONANTS = "бвгджзйклмнпрстфхцчшщ"

def checkWord(word):
    if word[1] in CONSONANTS and word[2] in CONSONANTS or
       word[1] in VOWELS and word[2] in VOWELS:
        return True
    else:
        return False

def checkDoubledLettersType(word1,word2):
    if checkWord(word1) or checkWord(word2):
        return True
    else:
        return False
    
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
    
def bukvoput(words):
    words = changeFirstLetters(words)
    if checkDoubledLettersType(words[0],words[1]):
        return "Получается не смэшно"
    else:
        return words
    
bot = telebot.TeleBot('5519104894:AAGw3YLcJfC3uzg4UMeCnXwiWDmRUIFLkgY');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    words = message.text.split()
    try:
        bot.send_message(message.chat.id, bukvoput(words))
    except:
        bot.send_message(message.from_user.id, bukvoput(words))



def test():
    print(changeFirstLetters(sys.argv[1:]))

def main():
    print()



bot.polling(none_stop=True, interval=0)
