import requests
from bs4 import BeautifulSoup
import telegram
import logging
from telegram.ext import Updater, CommandHandler

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_='section')
    if container:
        return container.text.strip()
    else:
        return "Error: Unable to find data container on the webpage."

def send_to_telegram(token, chat_id, message):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id, text=message)



def command1(update, context):
    url = "https://www.ethiobookreview.com/bookstores"
    scraped_data = scrape_data(url)
    send_to_telegram(bot_token, chat_id, scraped_data)



if __name__ == '__main__':
    bot_token = "6616563094:AAFh0_xdurWtbgxOARoGXwS4RJpTnvcD3IQ"
    chat_id = "709403071"

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info('Starting bot...')

    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('command1', command1))



    

    updater.start_polling()
    updater.idle()
    