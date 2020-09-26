from telegram.ext import Updater
from telegram.ext import CommandHandler
import pyqiwi
current_items=[]
wallet = pyqiwi.Wallet(token='f372cb25954fb4f8bb6b5051f026d7e8')
updater=Updater(token="1396381300:AAFtNnWv2adnSg7L3ZZQRr6x_ZNvGk39zG0",use_context=True)
dispatcher = updater.dispatcher
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to online shop,I am your bot and I will help you!")
    context.bot.send_message(chat_id=update.effective_chat.id,text="Bellow are a list of command you can use")
    context.bot.send_message(chat_id=update.effective_chat.id,text="/items  list the items in the shop")
    context.bot.send_message(chat_id=update.effective_chat.id,text="/current_items list of current items you bought")
    context.bot.send_message(chat_id=update.effective_chat.id,text="/buy+item buy and item from a list,dont forget to include the item too")
    context.bot.send_message(chat_id=update.effective_chat.id,text="/show_money show how much money I have on account")
def buy(update,conext,user_data):
    context.bot.send_message(chat_id=update.effective.chat.id,text="you want to buy "+str(user_data))
def items(update,context):
    items=["trousers","hat","glasses"]
    context.bot.send_message(chat_id=update.effective_chat.id,text=",".join(items))
def current_items(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text=",".join(current_items))
def show_money(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text=str(wallet.balance()))
start_handler = CommandHandler('start', start)
items_handler=CommandHandler("items",items)
current_items_handler=CommandHandler("current_items",items)
buy_handler=CommandHandler("buy",buy,pass_user_data=True)
show_money_handler=CommandHandler("show_money",show_money)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(items_handler)
dispatcher.add_handler(current_items_handler)
dispatcher.add_handler(show_money_handler)
updater.start_polling()
updater.idle()
