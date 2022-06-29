from telegram.ext import *
import os
from model import fashion_advisor

# telegram_bot_token = os.getenv('API_KEY')
telegram_bot_token = os.environ['API_KEY']
updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher
app_name = 'https://conv-ai-adviser.herokuapp.com/'

def start_command(update, context):  # Defines what happens when bot is started
    update.message.reply_text('Welcome to fashion advisor \n Please enter your query.')


def end_to_end(update, context):
    query = update.message.text
    answer = fashion_advisor(query)
    update.message.reply_text(answer)

    # if attr is None:
    #     update.message.reply_text("An unknown problem occurred please contact the support.")
    #
    # URL = []
    #
    # if len(attr) == 1:  # garment matching
    #     attr0, match = garment_matching(attr[0], 5)
    #     update.message.reply_text(attr[0].capitalize() + ' will match with the following attributes: ')
    #     update.message.reply_text(match)
    #     update.message.reply_text('\nHere are some images of your item with some good matches:\n')
    #
    #     for item in match:
    #         URL = URL + new_extract_image(attr0, item, 1)
    #         URL = list(dict.fromkeys(URL))
    #
    #     chat_id = update.message.chat_id
    #
    #     for i in range(len(URL)):
    #         context.bot.sendPhoto(chat_id=chat_id, photo=URL[i])
    #
    #
    # elif len(attr) == 2:  # garment advice
    #     attr1, attr2, g = garment_advice(attr[0], attr[1], 10)
    #     if g == True:
    #         update.message.reply_text(attr[0].capitalize() + ' would be a good match with ' + attr[1])
    #         update.message.reply_text('\nHere are some images of that combo: ')
    #         URL = new_extract_image(attr1, attr2, 5)
    #         URL = list(dict.fromkeys(URL))
    #
    #         chat_id = update.message.chat_id
    #
    #         for i in range(len(URL)):
    #             context.bot.sendPhoto(chat_id=chat_id, photo=URL[i])
    #
    #
    #     elif attr1 is None:
    #         update.message.reply_text("Those items are not commonly worn together !")
    #
    #     else:
    #         update.message.reply_text(attr1)
    #
    #
    # elif len(attr) == 0:
    #     return None
    #
    # else:
    #     update.message.reply_text(
    #         'More than 2 attributes were detected, this version only support 1 attribute for garment matching and 2 for garment advice')


def help_command(update, context):  # To give specific instructions to user
    update.message.reply_text(
        'This bot can give you advice about what to wear with garments you give it (advice)'
        ' or can tell you if your items are a good fit together (match)')
    update.message.reply_text(
        "Your query should contain items separated by ';', e.g.: \n - garment advice: yellow shirt; white boots; advice"
        " \n  - garment matching: black skirt; blue heels; black, checkered, leather bag; match")


def error(update, context):
    print(f"Update {update} caused error {context.error}")


dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(MessageHandler(Filters.text, end_to_end))
dispatcher.add_error_handler(error)

updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', 5000)),
                      url_path=telegram_bot_token,
                      webhook_url=app_name + telegram_bot_token)
# updater.idle()
