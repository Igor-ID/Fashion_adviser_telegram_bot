from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os
from model import fashion_advisor

TOKEN = os.environ['TOKEN']
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start_command(update, context):  # Defines what happens when bot is started
    update.message.reply_text('Hi there, this is your fashion adviser! \n Please enter your query. '
                              '\n Type /help for instructions.')


def end_to_end(update, context):
    query = update.message.text
    answer = fashion_advisor(query)
    update.message.reply_text(answer)


def help_command(update, context):  # To give specific instructions to user
    update.message.reply_text(
        'This bot can give you advice on what to wear with garments you give it (advice)'
        ' or can tell you if your items of clothing fit together (match)')
    update.message.reply_text(
        "Query should contain items separated by ';', at the end of your query, specify advice or match, for example:"
        " \n- for garment advice specify: black shirt; blue jeans; advice"
        " \n- for garment matching specify: black shirt; blue jeans; black,leather bag; match")


def error(update, context):
    print(f"Update {update} caused error {context.error}")


dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(MessageHandler(Filters.text, end_to_end))
dispatcher.add_error_handler(error)

updater.start_polling()

# Uncomment the following code if you want to deploy to cloud services such as Heroku, AWS, Google Clouds, etc.
# In this case, you need a plan with 4GB+ of memory.
# app_name = ""
# updater.start_webhook(listen="0.0.0.0",
#                       port=int(os.environ.get('PORT', '8443')),
#                       url_path=TOKEN,
#                       webhook_url=app_name + TOKEN)

