
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#Command Handlers
def start(update, context):
    update.message.reply_text('I AM ALIVE!')


#function to respond to help cmd
def help(update, context):
    update.message.reply_text('I am currently not smart enough to help you.')

#function to echo the users message
def echo(update, context):
    update.message.reply_text(update.message.text + '' + ' AND JOSH IS THE GREATEST.')

#function to log errors and display
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def affirm(update, context):
    update.message.reply_text("You are a great python programmer")

def reminder(update, context):
    update.message.reply_text("Keep watching the course, never falter")

def powerful(update, context):
    update.message.reply_text("You will finish this course and make $5000 a month from this")


def main():
    updater = Updater("5449486272:AAHTtE3T_nB6J3hU6u-0BLlw8BUU4LXXCzE", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("affirm", affirm))
    dp.add_handler(CommandHandler("reminder", reminder))
    dp.add_handler(CommandHandler("powerful", powerful))
    
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()