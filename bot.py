import requests
import cairosvg
import logging
from uuid import uuid4
from configparser import ConfigParser


from telegram import Update, InlineQueryResultCachedPhoto
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.utils.helpers import escape_markdown

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

config = ConfigParser()
config.read("config.ini")
botinfo = config["BOTINFO"]

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Please use this bot as inline in your chat!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')
    
    
def latex_image(text):
    """ Fetches SVG image and converts to PNG from Latex API"""
    url = "https://math.now.sh"
    params = {'from':text}
    response = requests.get(url, params = params)
    cairosvg.svg2png(bytestring=response.content, write_to="output.png", dpi = 200)
    
def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    latex_image(query)
    if query == "":
        return
    infophoto = context.bot.sendPhoto(chat_id= int(botinfo["usid"]),photo=open('output.png','rb'),caption="tt")
    thumbphoto = infophoto["photo"][0]["file_id"]
    originalphoto = infophoto["photo"][-1]["file_id"]
    results = [
        InlineQueryResultCachedPhoto(
            id=uuid4(),
            title="CachedPhoto",
            photo_file_id=originalphoto)
        ]
    context.bot.answer_inline_query(update.inline_query.id, results)
    
def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(botinfo["token"])

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
    
    

"""
function to get png without API
def latex_image(text):
    preamble = "\\documentclass[10pt]{article}\n" \
        "\\usepackage{amsmath,amsfonts}\\begin{document}"
    preview(r'$$' + text + r'$$', dvioptions=["-D 300"], viewer = 'file', filename='output.png', euler= False)#,  preamble=preamble)
    
"""
