import covid19cases as covid

import telebot
bot = telebot.TeleBot("1268856054:AAHWunZt1XmHfG6pbwI_hQQEkjLF8HQA__A")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    country = covid.get_country_cases( message.text )
    confirm = country['TotalCases']
    death = country['TotalDeaths']
    recover = country['TotalRecovered']

    answer = "At this moment, in " + message.text + " there are " + str(confirm) + " infected people. \n"
    answer += "The number of deaths is " + str(death) + ".  " + str(recover) + " people have recovered. \n\n" + str.upper("#stayathome")

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
