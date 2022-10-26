import telebot
import time
bot = telebot.TeleBot("5654012216:AAHHsyILaYC1Ns0dhNuVd6bXBkXyPC78DaY")

time.sleep(20)

@bot.message_handler(commands=['info', 'help'])
def send_welcome(message):
    bot.reply_to(message, "bienvenidos a nuestra empresa DCS consultora, Somos una empresa de "
                            "consultoría que promueve la transformación en las diferentes capas del "
                            "negocio de nuestros clientes mediante el uso de plataformas digitales efectivas, "
                            "que apoyen sus estrategias de negocio y les permitan alcanzar sus objetivos. Contamos con 5 líneas" 
                            "de soluciones para impulsar cambios efectivos en las organizaciones que van desde la seguridad digital,"
                            "hasta la mejora de procesos de negocio y avanzados analíticos para la operación y toma de decisiones.")


    bot.reply_to(message, "visite nuestra pagina web http://dsc.ace.com.pe")
    bot.reply_to(message, "visite nuestra API de Esperanza de Vida https://esperanzadevida.herokuapp.com/api4 ")
    bot.reply_to(message, "visite nuestra  presentacion del proyecto Esperanza de Vida  .........")
    bot.reply_to(message, "visite tambien nuestro repositorio ...........")

@bot.message_handler(commands=['info', 'help'])
def send_welcome(message):
    import requests
    from pandas import json_normalize
    r = requests.get('http://esperanzadevida.herokuapp.com/api4')
    x = r.json()
    df = json_normalize(x['api4']) 
    df=df.drop(['index'], axis=1)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.polling()
