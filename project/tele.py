
from telegram.ext import *
import keys
from  news_bot_api import get_news

print('starting up bot...')

def start_command(update, context):
    update.message.reply_text('Hello there ! I\'m a bot. Nice to meet you !')

    
def help_command(update, context):
    update.message.reply_text('Try typing anything and I will respond !')
    

def custom_command(update, context):
    update.message.reply_text('This is a custom command !')
    
def handle_response(text: str) -> str:
    if 'hello' in text.lower().strip():
        return 'Hey there !'

    if 'how are you' in text.lower().strip():
        return 'I am good, thanks!'

    #if 'weather' in text.lower().strip():
       # return '🏥' + '/n🏥'  .join(get_weather())  

    if 'news' in text .lower().strip():
        return '📰' + '\n 📰' .join(get_news()) 

    return 'Idk, Try other query!'  


def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ' '

    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    if message_type =='group':
        if '@feb_pybot' in text:
            new_text = text.replace('@feb_pybot', '').strip()
            response = handle_response(new_text)

    else:
        response = handle_response(text)
       
    update.message.reply_text(response)

def error(update, context):
    print(f'Update {update} caused error: {context.error}') 

# run the program
if __name__=='__main__':
    updater = Updater(keys.token,use_context=True)
    dp = updater.dispatcher

    # commands
    dp.add_handler(CommandHandler('start', start_command))      
    dp.add_handler(CommandHandler('help', help_command))  
    dp.add_handler(CommandHandler('custom', custom_command))  
         

    # messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))     

    #Errors
    dp.add_error_handler(error)

    # Run bot
    updater.start_polling(1.0)
    updater.idle()