import logging
import telebot
import http.client
import json
bot = telebot.TeleBot(config.TOKEN)
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
res = conn.getresponse()
data = res.read()
corona = data.decode("utf-8")
json = json.loads(corona)
def conZ():
   text1=""
   for i in range(9,10):
            text1=list(json[i].items())[14]
            text1+=list(json[i].items())[12]
            text1+=list(json[i].items())[10]
            text1+=list(json[i].items())[2]
   return text1
def conT():
   text2=""
   for i in range(1,2):
            text2=list(json[i].items())[14]
            text2+=list(json[i].items())[12]
            text2+=list(json[i].items())[10]
            text2+=list(json[i].items())[2]
   return text2
def conTT():
   text3=""
   for i in range(8,9):
            text3=list(json[i].items())[14]
            text3+=list(json[i].items())[12]
            text3+=list(json[i].items())[10]
            text3+=list(json[i].items())[2]
   return text3
def conF():
   text4=""
   for i in range(0,1):
            text4=list(json[i].items())[14]
            text4+=list(json[i].items())[12]
            text4+=list(json[i].items())[10]
            text4+=list(json[i].items())[2]
   return text4
def conFF():
   text5=""
   for i in range(7,8):
            text5=list(json[i].items())[14]
            text5+=list(json[i].items())[12]
            text5+=list(json[i].items())[10]
            text5+=list(json[i].items())[2]
   return text5
@bot.message_handler(commands=['start'])
def lala(message):
    text1 = conZ()
    text2 = conT()
    text3 = conTT()
    text4 = conF()
    text5 = conFF()

    bot.send_message(message.chat.id, text1[6])
    bot.send_message(message.chat.id, text1[7])
    bot.send_message(message.chat.id, text1[0])
    bot.send_message(message.chat.id, text1[1])
    bot.send_message(message.chat.id, text1[2])
    bot.send_message(message.chat.id, text1[3])
    bot.send_message(message.chat.id, text1[4])
    bot.send_message(message.chat.id, text1[5])

    bot.send_message(message.chat.id, text2[6])
    bot.send_message(message.chat.id, text2[7])
    bot.send_message(message.chat.id, text2[0])
    bot.send_message(message.chat.id, text2[1])
    bot.send_message(message.chat.id, text2[2])
    bot.send_message(message.chat.id, text2[3])
    bot.send_message(message.chat.id, text2[4])
    bot.send_message(message.chat.id, text2[5])

    bot.send_message(message.chat.id, text3[6])
    bot.send_message(message.chat.id, text3[7])
    bot.send_message(message.chat.id, text3[0])
    bot.send_message(message.chat.id, text3[1])
    bot.send_message(message.chat.id, text3[2])
    bot.send_message(message.chat.id, text3[3])
    bot.send_message(message.chat.id, text3[4])
    bot.send_message(message.chat.id, text3[5])

    bot.send_message(message.chat.id, text4[6])
    bot.send_message(message.chat.id, text4[7])
    bot.send_message(message.chat.id, text4[0])
    bot.send_message(message.chat.id, text4[1])
    bot.send_message(message.chat.id, text4[2])
    bot.send_message(message.chat.id, text4[3])
    bot.send_message(message.chat.id, text4[4])
    bot.send_message(message.chat.id, text4[5])

    bot.send_message(message.chat.id, text5[6])
    bot.send_message(message.chat.id, text5[7])
    bot.send_message(message.chat.id, text5[0])
    bot.send_message(message.chat.id, text5[1])
    bot.send_message(message.chat.id, text5[2])
    bot.send_message(message.chat.id, text5[3])
    bot.send_message(message.chat.id, text5[4])
    bot.send_message(message.chat.id, text5[5])
@bot.message_handler(commands=['help'])
def lala(message):
    bot.send_message(message.chat.id, '/start - уся інформація\n/update - оновлена\n/save - сохранить в файл\n/Japan - Japan\n/Turkey - Turkey\n/Israel - Israels\n/India -  India\n/Bangladesh - Bangladesh \n/search - поиск по странам')
@bot.message_handler(commands=['Japan'])
def lala(message):
    text1=conZ()
    bot.send_message(message.chat.id, text1[6])
    bot.send_message(message.chat.id, text1[7])
    bot.send_message(message.chat.id, text1[0])
    bot.send_message(message.chat.id, text1[1])
    bot.send_message(message.chat.id, text1[2])
    bot.send_message(message.chat.id, text1[3])
    bot.send_message(message.chat.id, text1[4])
    bot.send_message(message.chat.id, text1[5])

@bot.message_handler(commands=['Turkey'])
def lala(message):
    text2=conT()
    bot.send_message(message.chat.id, text2[6])
    bot.send_message(message.chat.id, text2[7])
    bot.send_message(message.chat.id, text2[0])
    bot.send_message(message.chat.id, text2[1])
    bot.send_message(message.chat.id, text2[2])
    bot.send_message(message.chat.id, text2[3])
    bot.send_message(message.chat.id, text2[4])
    bot.send_message(message.chat.id, text2[5])
@bot.message_handler(commands=['Israel'])
def lala(message):
    text3=conTT()
    bot.send_message(message.chat.id, text3[6])
    bot.send_message(message.chat.id, text3[7])
    bot.send_message(message.chat.id, text3[0])
    bot.send_message(message.chat.id, text3[1])
    bot.send_message(message.chat.id, text3[2])
    bot.send_message(message.chat.id, text3[3])
    bot.send_message(message.chat.id, text3[4])
    bot.send_message(message.chat.id, text3[5])
@bot.message_handler(commands=['India'])
def lala(message):
    text4=conF()
    bot.send_message(message.chat.id, text4[6])
    bot.send_message(message.chat.id, text4[7])
    bot.send_message(message.chat.id, text4[0])
    bot.send_message(message.chat.id, text4[1])
    bot.send_message(message.chat.id, text4[2])
    bot.send_message(message.chat.id, text4[3])
    bot.send_message(message.chat.id, text4[4])
    bot.send_message(message.chat.id, text4[5])
@bot.message_handler(commands=['Bangladesh'])
def lala(message):
    text5=conFF()
    bot.send_message(message.chat.id, text5[6])
    bot.send_message(message.chat.id, text5[7])
    bot.send_message(message.chat.id, text5[0])
    bot.send_message(message.chat.id, text5[1])
    bot.send_message(message.chat.id, text5[2])
    bot.send_message(message.chat.id, text5[3])
    bot.send_message(message.chat.id, text5[4])
    bot.send_message(message.chat.id, text5[5])
@bot.message_handler(commands=['save'])
def lala(message):
    f = open('text.txt', 'w')
    text1 = conZ()
    text2 = conT()
    text3 = conTT()
    text4 = conF()
    text5 = conFF()
    f.write(text1[6])
    f.write(':')
    f.write(text1[7])
    f.write(' ')
    f.write(text1[0])
    f.write(':')
    f.write(text1[1])
    f.write(' ')
    f.write(text1[2])
    f.write(':')
    f.write(str(text1[3]))
    f.write(' ')
    f.write(text1[4])
    f.write(':')
    f.write(str(text1[5]))
    f.write(' ')
    f.write(text2[6])
    f.write(':')
    f.write(text2[7])
    f.write(' ')
    f.write(text2[0])
    f.write(':')
    f.write(text2[1])
    f.write(' ')
    f.write(text2[2])
    f.write(':')
    f.write(str(text2[3]))
    f.write(' ')
    f.write(text2[4])
    f.write(':')
    f.write(str(text2[5]))

    f.write(text3[6])
    f.write(':')
    f.write(text3[7])
    f.write(' ')
    f.write(text3[0])
    f.write(':')
    f.write(text3[1])
    f.write(' ')
    f.write(text3[2])
    f.write(':')
    f.write(str(text3[3]))
    f.write(' ')
    f.write(text3[4])
    f.write(':')
    f.write(str(text3[5]))

    f.write(text4[6])
    f.write(':')
    f.write(text4[7])
    f.write(' ')
    f.write(text4[0])
    f.write(':')
    f.write(text4[1])
    f.write(' ')
    f.write(text4[2])
    f.write(':')
    f.write(str(text4[3]))
    f.write(' ')
    f.write(text4[4])
    f.write(':')
    f.write(str(text4[5]))

    f.write(text5[6])
    f.write(':')
    f.write(text5[7])
    f.write(' ')
    f.write(text5[0])
    f.write(':')
    f.write(text5[1])
    f.write(' ')
    f.write(text5[2])
    f.write(':')
    f.write(str(text5[3]))
    f.write(' ')
    f.write(text5[4])
    f.write(':')
    f.write(str(text5[5]))

    f.close()
    file = open('text.txt', 'rb')
    bot.send_document(message.chat.id, file)
    file.close()
@bot.message_handler(commands=['update'])
def lala(message):
    text1 = conZ()
    text2 = conT()
    text3 = conTT()
    text4 = conF()
    text5 = conFF()

    bot.send_message(message.chat.id, text1[6])
    bot.send_message(message.chat.id, text1[7])
    bot.send_message(message.chat.id, text1[0])
    bot.send_message(message.chat.id, text1[1])
    bot.send_message(message.chat.id, text1[2])
    bot.send_message(message.chat.id, text1[3])
    bot.send_message(message.chat.id, text1[4])
    bot.send_message(message.chat.id, text1[5])

    bot.send_message(message.chat.id, text2[6])
    bot.send_message(message.chat.id, text2[7])
    bot.send_message(message.chat.id, text2[0])
    bot.send_message(message.chat.id, text2[1])
    bot.send_message(message.chat.id, text2[2])
    bot.send_message(message.chat.id, text2[3])
    bot.send_message(message.chat.id, text2[4])
    bot.send_message(message.chat.id, text2[5])

    bot.send_message(message.chat.id, text3[6])
    bot.send_message(message.chat.id, text3[7])
    bot.send_message(message.chat.id, text3[0])
    bot.send_message(message.chat.id, text3[1])
    bot.send_message(message.chat.id, text3[2])
    bot.send_message(message.chat.id, text3[3])
    bot.send_message(message.chat.id, text3[4])
    bot.send_message(message.chat.id, text3[5])

    bot.send_message(message.chat.id, text4[6])
    bot.send_message(message.chat.id, text4[7])
    bot.send_message(message.chat.id, text4[0])
    bot.send_message(message.chat.id, text4[1])
    bot.send_message(message.chat.id, text4[2])
    bot.send_message(message.chat.id, text4[3])
    bot.send_message(message.chat.id, text4[4])
    bot.send_message(message.chat.id, text4[5])

    bot.send_message(message.chat.id, text5[6])
    bot.send_message(message.chat.id, text5[7])
    bot.send_message(message.chat.id, text5[0])
    bot.send_message(message.chat.id, text5[1])
    bot.send_message(message.chat.id, text5[2])
    bot.send_message(message.chat.id, text5[3])
    bot.send_message(message.chat.id, text5[4])
    bot.send_message(message.chat.id, text5[5])
@bot.message_handler(commands=['search'])
def start_handler(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id, 'Каакая страна?')
    bot.register_next_step_handler(msg, askAge)

def askAge(message):
    chat_id = message.chat.id
    text = message.text
    c1 = "Japan"
    c2 = "Turkey"
    c3 = "Israel"
    c4 = "India"
    c5 = "Bangladesh"
    if text==c1:
        text1 = conZ()
        bot.send_message(message.chat.id, text1[6])
        bot.send_message(message.chat.id, text1[7])
        bot.send_message(message.chat.id, text1[0])
        bot.send_message(message.chat.id, text1[1])
        bot.send_message(message.chat.id, text1[2])
        bot.send_message(message.chat.id, text1[3])
        bot.send_message(message.chat.id, text1[4])
        bot.send_message(message.chat.id, text1[5])
    if text==c2:
        text2 = conT()
        bot.send_message(message.chat.id, text2[6])
        bot.send_message(message.chat.id, text2[7])
        bot.send_message(message.chat.id, text2[0])
        bot.send_message(message.chat.id, text2[1])
        bot.send_message(message.chat.id, text2[2])
        bot.send_message(message.chat.id, text2[3])
        bot.send_message(message.chat.id, text2[4])
        bot.send_message(message.chat.id, text2[5])
    if text==c3:
        text3 = conTT()
        bot.send_message(message.chat.id, text3[6])
        bot.send_message(message.chat.id, text3[7])
        bot.send_message(message.chat.id, text3[0])
        bot.send_message(message.chat.id, text3[1])
        bot.send_message(message.chat.id, text3[2])
        bot.send_message(message.chat.id, text3[3])
        bot.send_message(message.chat.id, text3[4])
        bot.send_message(message.chat.id, text3[5])
    if text==c4:
        text4 = conF()
        bot.send_message(message.chat.id, text4[6])
        bot.send_message(message.chat.id, text4[7])
        bot.send_message(message.chat.id, text4[0])
        bot.send_message(message.chat.id, text4[1])
        bot.send_message(message.chat.id, text4[2])
        bot.send_message(message.chat.id, text4[3])
        bot.send_message(message.chat.id, text4[4])
        bot.send_message(message.chat.id, text4[5])
    if text==c5:
        text5 = conFF()
        bot.send_message(message.chat.id, text5[6])
        bot.send_message(message.chat.id, text5[7])
        bot.send_message(message.chat.id, text5[0])
        bot.send_message(message.chat.id, text5[1])
        bot.send_message(message.chat.id, text5[2])
        bot.send_message(message.chat.id, text5[3])
        bot.send_message(message.chat.id, text5[4])
        bot.send_message(message.chat.id, text5[5])
    if (text!=c5 and text!=c4 and text!=c3 and text!=c2 and text!=c1):
        msg = bot.send_message(chat_id, 'Перевірте написання')
        bot.register_next_step_handler(msg, askAge) #askSource
        return
@bot.message_handler(content_types=['text'])
def lala(message):
    bot.send_message(message.chat.id, 'Напиши /help')
bot.polling(none_stop=True)
