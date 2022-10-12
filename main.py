import sys
import telebot;
Vowels = "аоуэыяёюеи"
Consonants = "бвгджзйклмнпрстфхцчшщ"

def CheckDoubledLettersType(word1,word2):
    if (word1[1] in Consonants and word1[2] in Consonants) or
       (word2[1] in Consonants and word2[2] in Consonants) or
       (word1[1] in Vowels and word1[2] in Vowels) or
       (word2[1] in Vowels and word2[2] in Vowels):
        result = true
    else:
        result = false
    return result
    

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
    
def Bukvoput(words):
    words = changeFirstLetters(words)
    if CheckDoubledLettersType(words[0],words[1]):
        return "Получается не смэшно"
    else:
        return words
    
bot = telebot.TeleBot('5519104894:AAGw3YLcJfC3uzg4UMeCnXwiWDmRUIFLkgY');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    words = message.text.split()
    try:
        bot.send_message(message.chat.id, Bukvoput(words))
    except:
        bot.send_message(message.from_user.id, Bukvoput(words))



def test():
    print(changeFirstLetters(sys.argv[1:]))

def main():
    print()



bot.polling(none_stop=True, interval=0)
