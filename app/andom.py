import telebot
import random , time , config
from telebot import types , TeleBot

bot = TeleBot(config.token)

@bot.message_handler(commands=['start']) 
def start(message):
    teq = 'Вжух' 
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

@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    try:
        number = random.randint(0, 100)
        r = telebot.types.InlineQueryResultArticle('1', '😉 Узнай свой шанс на увольнение', telebot.types.InputTextMessageContent('На ,  ' f'{number}%' ' ты уволен 😉 '))
        w = telebot.types.InlineQueryResultArticle('2', '🤩 На сколько ты Мезенцев ?', telebot.types.InputTextMessageContent('Вжух , и на ' f'{number}%' ' ты Мезенцев 🤩'))
        x = telebot.types.InlineQueryResultArticle('3', '🧚 Я Фея', telebot.types.InputTextMessageContent('На ,  ' f'{number}%' ' фея 🥰 ')) 
        bot.answer_inline_query(query.id, [r , w , x])
    except Exception as e:
        print(e)

bot.polling()