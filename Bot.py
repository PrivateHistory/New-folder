from telegram.ext import CommandHandler, CallbackQueryHandler,Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import LoginUrl
import os
import sys
import pyqiwi
### function
def start(update, context):
  update.message.reply_text("Добро пожаловать "+str(update.message.from_user.id) +" в Les Miserable онлайн магазин",
                            reply_markup=main_menu_keyboard())

def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text="Добро пожаловать обратно в магазин Les Miserable",
                        reply_markup=main_menu_keyboard())

def shop(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=shop_message(),
                        reply_markup=shop_keyboard())

def wallet(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=wallet_message(),
                        reply_markup=wallet_keyboard())

def support(update,context):
   pass


def shop_Uplay(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
                          text="Стоимость Uplay 500 руб. Хотите купить?",
                          reply_markup=Uplay_keyboard())

def shop_Lol(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
                          text="Стоимость Lol 550 руб. Хотите купить?",
                          reply_markup=Uplay_keyboard())

def shop_Origin(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
                          text="Стоимость Origin 700 руб. Хотите купить?",
                          reply_markup=Origin_keyboard())

def shop_Check_Object(update,context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(
                              text="Стоимость Check Object 1 руб. Хотите купить?",
                              reply_markup=Check_Object_keyboard())

def wallet_balance(update,context):
    pass


def wallet_put_money(update,context):
    pass

def Uplay_buy(update,context):
    pass
def Check_Object_buy(update,context):
    pass
def Origin_buy(update,context):
    pass
def Lol_buy(update,context):
    pass

####keyboards####
def main_menu_keyboard():
    keyboard=[[InlineKeyboardButton("Mагазин",callback_data="shop")],
    [InlineKeyboardButton("Kошелек",callback_data="wallet")],
    [InlineKeyboardButton("Суппорт",callback_data="support")]]
    return InlineKeyboardMarkup(keyboard)

def shop_keyboard():
    keyboard=[[InlineKeyboardButton("Uplay",callback_data="Uplay_Shop")],
    [InlineKeyboardButton("Origin",callback_data="Origin_Shop")],
    [InlineKeyboardButton("Lol",callback_data="Lol_Shop")],
    [InlineKeyboardButton("Check Object",callback_data="Check_Object_Shop")],
    [InlineKeyboardButton("Главное",callback_data="main")]]
    return InlineKeyboardMarkup(keyboard)


def wallet_keyboard():
    keyboard=[[InlineKeyboardButton("Баланс",callback_data="wallet_balance")],
    [InlineKeyboardButton("Добавить",callback_data="wallet_put_money")],
    [InlineKeyboardButton("Главное",callback_data="main")]]
    return InlineKeyboardMarkup(keyboard)

def Uplay_keyboard():
    keyboard=[[InlineKeyboardButton("Купить",callback_data="Buy_Uplay")],
    [InlineKeyboardButton("Главное",callback_data="main")]]
    return InlineKeyboardMarkup(keyboard)

def Origin_keyboard():
    keyboard=[[InlineKeyboardButton("Купить",callback_data="Buy_Origin")],
    [InlineKeyboardButton("Главное",callback_data="main")]]
    return InlineKeyboardMarkup(keyboard)

def Lol_keyboard():
        keyboard=[[InlineKeyboardButton("Купить",callback_data="Buy_Lol")],
        [InlineKeyboardButton("Главное",callback_data="main")]]
        return InlineKeyboardMarkup(keyboard)

def Check_Object_keyboard():
    keyboard=[[InlineKeyboardButton("Купить",callback_data="Buy_Check_Object")],
    [InlineKeyboardButton("Главное",callback_data="main")]]
    return InlineKeyboardMarkup(keyboard)

###mesages
def shop_message():
    return "Mагазин"

def wallet_message():
    return "Kошелек"

def stop():
    print("It wroked")
    updater.stop()
    os.execl(sys.executable, sys.executable, *sys.argv)
updater=Updater(token="1182408515:AAH8DTTiYWtY7wfqSTYgjc7WSUI87oamPrE",use_context=True)

##dispatcher
updater.dispatcher.add_handler(CommandHandler('stop',stop))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu,pattern="main"))
updater.dispatcher.add_handler(CallbackQueryHandler(shop,pattern="shop"))
updater.dispatcher.add_handler(CallbackQueryHandler(wallet,pattern="wallet"))
updater.dispatcher.add_handler(CallbackQueryHandler(Check_Object_buy,pattern="Buy_Check_Object"))
updater.dispatcher.add_handler(CallbackQueryHandler(Lol_buy,pattern="Buy_Lol"))
updater.dispatcher.add_handler(CallbackQueryHandler(Origin_buy,pattern="Buy_Origin"))
updater.dispatcher.add_handler(CallbackQueryHandler(Uplay_buy,pattern="Buy_Uplay"))
updater.dispatcher.add_handler(CallbackQueryHandler(wallet_put_money,pattern="wallet_put_money"))
updater.dispatcher.add_handler(CallbackQueryHandler(wallet_balance,pattern="wallet_balance"))
updater.dispatcher.add_handler(CallbackQueryHandler(shop_Uplay,pattern="Uplay_Shop"))
updater.dispatcher.add_handler(CallbackQueryHandler(shop_Lol,pattern="Lol_Shop"))
updater.dispatcher.add_handler(CallbackQueryHandler(shop_Origin,pattern="Origin_Shop"))
updater.dispatcher.add_handler(CallbackQueryHandler(shop_Check_Object,pattern="Check_Object_Shop"))
updater.dispatcher.add_handler(CallbackQueryHandler(support,pattern="support"))

updater.start_polling()
