from bot import bot
from telebot.types import Message

@bot.message_handler(commands=['start'])
def on_start(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id,
                     text='Hello, *Sweety* 💋!')
    
@bot.message_handler(commands=['hot_chick'])
def on_hot_chick(message: Message) -> None:
    with open(file='hot_chick.jpg', mode='rb') as hot_chick_photo:
        bot.send_photo(chat_id=message.from_user.id,
                        photo=hot_chick_photo)

if __name__ == '__main__':
    bot.infinity_polling()