import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot("6963295512:AAFBZ5UvNrKwlVung5lzZHlykcECeNfCKPk")

print("THE ROBOT STARTED")

first_button = telebot.types.InlineKeyboardButton("ME", url=("https://t.me/info_miti"))
markup = telebot.types.InlineKeyboardMarkup(row_width=1)
markup.add(first_button)

@bot.message_handler(commands=["start"])
def send_welcome(m):
    bot.send_message(m.chat.id, f"HI {m.chat.first_name} \nYour numeric ID is : <code>{m.chat.id}</code>", reply_markup=markup, parse_mode="HTML")
    print("OK :)")
    

bot.infinity_polling()