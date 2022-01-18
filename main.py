import praw
import random
import pyjokes

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
updater = Updater("5095901879:AAG1RoLuRFsNI8NblqzjZMdO-Str-jogJIY", use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("""HELLO!!

I am a bot used for memes jokes and evne get Rick roll link.

/meme - to send meme pictures.
/joke - to send some joke texts.
/rick_roll - to get Rick roll link.""")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""/meme - to send meme pictures.
/joke - to send some joke texts.
/rick_roll - to get Rick roll link.""")

def meme(update: Update, context: CallbackContext):
    reddit = praw.Reddit(client_id ="Vm6O9-qztabNwUZXdetuNg", client_secret = "tEo-JMR9IFpi_HBIqri8KmDx_2RJ1g", username = "Mighty-Memer", password = "mightymemer@arks00!", user_agent = "Mightymeme")
    subreddit = reddit.subreddit("memes")
    meme_data_list = []
    top = subreddit.top(limit = 5)
    for submission in top:
        meme_data_list.append(submission)
    meme_data = random.choice(meme_data_list)
    meme_title = meme_data.title
    meme_url = meme_data.url
    update.message.reply_text(f"{meme_title}:\n{meme_url}")

def joke(update: Update, context: CallbackContext):
    joke = pyjokes.get_joke()
    update.message.reply_text(joke)
    
def rick_roll(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('meme', meme))
updater.dispatcher.add_handler(CommandHandler('joke', joke))
updater.dispatcher.add_handler(CommandHandler('rick_roll', rick_roll))

updater.start_polling()
updater.idle()