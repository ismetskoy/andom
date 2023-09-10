import telebot
import random , time , config
from telebot import types , TeleBot

bot = TeleBot(config.token)

@bot.message_handler(commands=['start']) 
def start(message):
    teq = '' 
    keyboard = types.InlineKeyboardMarkup();
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); 
    keyboard.add(key_yes);
    key_no= types.InlineKeyboardButton(text='Поделись своим волшебством 🍭', switch_inline_query=teq);
    keyboard.add(key_no)    
    bot.send_message(message.from_user.id, text='🧚 Узнаем на сколько ты Фея?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "yes": 
        number = random.randint(0, 100)
        bot.send_message(call.from_user.id, 'А ты смелый. Ну что же, Стартуем .... 💨 ');
        bot.send_message(call.from_user.id, '1...');
        time.sleep(1)
        bot.send_message(call.from_user.id, '2...');
        time.sleep(1)
        bot.send_message(call.from_user.id, '3....');
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Вжух , и на ' f'{number}%' ' ты фея ' );
        keyboard = types.InlineKeyboardMarkup();
        key_more= types.InlineKeyboardButton(text='Ещё?', callback_data='more');
        keyboard.add(key_more);
        bot.send_document(call.message.chat.id, 'https://symbl.cc/i/emoji/descr/boryalove.gif' , reply_markup=keyboard)


    elif call.data == "no":
        bot.send_message(call.from_user.id, 'Ну попробуй разок, не будь ...');
    elif call.data == "more":
        bot.send_message(call.from_user.id, 'На сегодня хватит, сладкий 💋');

@bot.inline_handler(lambda query: query.query == '')
def query_text(query):
    try:
        qwe = ''
        button = types.InlineKeyboardButton(text='Поделись 🍭', switch_inline_query=qwe)
        keyboard = telebot.types.InlineKeyboardMarkup().add(button)
        number_0 = random.randint(0, 100)
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        r = telebot.types.InlineQueryResultArticle('1', '😉 Узнай свой шанс на увольнение', telebot.types.InputTextMessageContent('Шанс на увольнение -  ' f'{number_0}%' ' 😉 '),reply_markup=keyboard,thumbnail_url='https://img.icons8.com/?size=64&id=P9iy9QbkXKL7&format=png',description='Шанс и шанс')
        w = telebot.types.InlineQueryResultArticle('2_', '🤩 На сколько ты Мезенцев ?', telebot.types.InputTextMessageContent('Вжух ... и на - ' f'{number_1}%' ' ты Мезенцев 🤩 '),reply_markup=keyboard, thumbnail_url='https://img.icons8.com/?size=96&id=60277&format=png',description='Рискни и удача тебе улыбнется :)')
        x = telebot.types.InlineQueryResultArticle('3', ' 🧚 На сколько ты Фея ?', telebot.types.InputTextMessageContent('На - ' f'{number_2}%' ' ты фея 🥰 '),reply_markup=keyboard, thumbnail_url='https://img.icons8.com/?size=96&id=45524&format=png',description='А вдруг')
        bot.answer_inline_query(query.id, [r, w, x] , cache_time=0)

    except Exception as e:
        print(e)
        
bot.polling()
