import praw
import pyjokes
import os
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
updater = Updater("5095901879:AAGfLQetcl1LxoCMfIy1Bah90r-1HE-XzEU", use_context=True)
PORT = int(os.environ.get('PORT', 5000))
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
time = 0
def meme(update: Update, context: CallbackContext):
    global time
    reddit = praw.Reddit(client_id ="CLIENT ID", client_secret = "CLIENT SECRET", username = "USERNAME", password = "PASSWORD", user_agent = "USER AGENT")
    subreddit = reddit.subreddit("memes")
    meme_data_list = []
    top = subreddit.top(limit = 100)
    for submission in top:
        meme_data_list.append(submission)
    for i in range(len(meme_data_list)):
        meme_data = meme_data_list[time]
    #meme_data = random.choice(meme_data_list)
    meme_title = meme_data.title
    meme_url = meme_data.url
    update.message.reply_text(f"{meme_title}:\n{meme_url}")
    time += 1

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

#updater.start_webhook(listen="0.0.0.0",
#                          port=int(PORT),
#                          url_path="HEROKU USER ID")
#updater.bot.setWebhook('https://tele-bot5.herokuapp.com/' + "HEROKU USER ID")
updater.idle()
