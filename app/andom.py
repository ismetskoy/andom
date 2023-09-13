import telebot , random , time , config , json
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
        #Поиск цитат из .txt
        with open('cet.txt', 'r', encoding='utf-8', errors='ignore') as file:
            quotes = file.readlines()
        random_quote = random.choice(quotes)
        #Поиск цитат из .json
        with open('url.json', 'r') as file:
            data = json.load(file)
            photo_urls = data['urls']
        random_photo_url = random.choice(photo_urls) 
        #Выбор чата
        search = ''
        #Кнопка поделиться 
        button = types.InlineKeyboardButton(text='Поделись 🍭', switch_inline_query=search)
        keyboard = telebot.types.InlineKeyboardMarkup().add(button)
        #Рандом
        number_0 = random.randint(0, 100)
        number_1 = random.randint(0, 100)
        number_2 = random.randint(1, 30)
        
        url_0 = 'https://www.meme-arsenal.com/memes/81e181cffa2315158ea5ee67c0daf8fb.jpg'
        #Меню инлайта

        r = telebot.types.InlineQueryResultArticle(
            id='1', 
            title='😉 Узнай свой шанс на увольнение', 
            input_message_content=types.InputTextMessageContent('Шанс на увольнение -  ' f'{number_0}%' ' 😉 '), 
            reply_markup=keyboard, thumbnail_url='https://cdn.iz.ru/sites/default/files/styles/1920x1080/public/article-2019-02/TASS_8515540.jpg', 
            description='Увольнение - это как сюрприз на День рождения')
        
        x = telebot.types.InlineQueryResultArticle(
            id='2', 
            title='😎 Цитатка ot дяди Стэтхэма ', 
            input_message_content=types.InputTextMessageContent(f'{random_quote}© Jason Statham'), 
            reply_markup=keyboard, 
            thumbnail_url='https://texterra.ru/upload/medialibrary/bd1/r9d1w1bpa5caexz61px4copthgaip92u/1.webp', 
            description='© Jason Statham')
        
        w = telebot.types.InlineQueryResultArticle(
            id='3', 
            title='🤩 На сколько ты Мезенцев ', 
            input_message_content=types.InputTextMessageContent('Вжух ... и на - ' f'{number_1}%' ' ты Мезенцев 🤩 '), 
            reply_markup=keyboard, 
            thumbnail_url='https://memepedia.ru/wp-content/uploads/2021/10/duejn-skala-dzhonson-zhestko-mem-360x270.jpg', 
            description='Это как пирожок сюрприз')
        
        e = telebot.types.InlineQueryResultArticle(
            id='4', 
            title='🤠 Сколько у тебя Dick ?  ', 
            input_message_content=types.InputTextMessageContent(message_text= 'И так твой ---: ' f'{number_2}' 'см ' f'<a href="{url_0}"> 🤠 </a>', parse_mode='HTML'), 
            reply_markup=keyboard, 
            thumbnail_url='https://www.meme-arsenal.com/memes/81e181cffa2315158ea5ee67c0daf8fb.jpg', 
            description='Рискни и удача тебе улыбнется 😉')
        
        mem = types.InlineQueryResultArticle(
            id='5',
            title='Мемчик на денёк',
            description='Мемчик на денёк, чтоб стоял дружок',
            input_message_content=types.InputTextMessageContent(
            message_text= 'Мемчик на Денёк' f'<a href="{random_photo_url}"> 👾 </a>', parse_mode='HTML'),
            reply_markup=keyboard,
            thumbnail_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOJvLjnLet-U873MdMENaGSWv6VSj39jJ_HA&usqp=CAU')
            
        bot.answer_inline_query(query.id, [r, mem, x, e , w], cache_time=0)

    
    except Exception as e:
        print(e)

bot.polling()
        
