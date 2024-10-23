from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import hashlib

def readData():
    data = ""
    with open("data.txt", 'r') as f:
        data = f.readline()
    return data

def genUsername() -> str:
    data = readData()
    
    md5_hash = hashlib.md5()
    
    md5_hash.update(data.encode('utf-8'))
    username = md5_hash.hexdigest()                                                                                                                              
    
    return username

async def ping(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('pong')
    
async def getUsername(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text((genUsername()))

def main():
    # Thay 'REDIRECT TOKEN' bằng API Token của bot mà bạn nhận được từ BotFather
    application = Application.builder().token("{REDIRECT TOKEN}").build()

    # Đăng ký lệnh 'ping' cho bot
    application.add_handler(CommandHandler("ping", ping))
    
    application.add_handler(CommandHandler("username", getUsername))

    # Bắt đầu bot
    application.run_polling()
    print(genUsername())

if __name__ == '__main__':
    main()
