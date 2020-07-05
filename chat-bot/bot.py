from telegram.ext import Updater, CommandHandler
import datetime


def welcome(update, context):
    message = "Olá " + update.message.from_user.first_name + " " + update.message.from_user.last_name + "!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def horario(update, context):
    now = datetime.datetime.now()
    time_stamp = "Hora Atual: {}:{}:{} - Data de Hoje: {}/{}/{}".format(
        now.hour,
        now.minute,
        now.second,
        now.day,
        now.month,
        now.year
    )
    print(time_stamp)
    context.bot.send_message(chat_id=update.effective_chat.id, text=time_stamp)

def main():

    token = 'TOKEM AQUI'
    updater = Updater(token = token, use_context= True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.dispatcher.add_handler(CommandHandler('time', horario))


    updater.start_polling()
    print(str(updater))
    updater.idle()


if __name__ == "__main__":
    main()
