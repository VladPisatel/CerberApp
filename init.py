from twx.botapi import TelegramBot, ReplyKeyboardMarkup, InputFile, InputFileInfo

"""
Setup the bot
"""
print("started")

bot = TelegramBot('157665031:AAHaeUoydRVxbisOrx-yA3542NYlmA0XOdo')
bot.update_bot_info().wait()
print(bot.username)

"""
Send a message to a user
"""
user_id = int(122012260)
fp = open('0005-006-TSypljonok-ostalsja-u-zabora-odin.png', 'rb')
file_info = InputFileInfo('0005-006-TSypljonok-ostalsja-u-zabora-odin.png', fp, 'image/png')

i = InputFile('photo', file_info)

bot.send_photo(chat_id=79434866, photo=i)
#result = bot.send_message(user_id, 'ddd').wait()
#print(result)

"""
Get updates sent to the bot
"""
updates = bot.get_updates().wait()
for update in updates:
    print(update)

"""
Use a custom keyboard
"""
keyboard = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
         ['0']
]
reply_markup = ReplyKeyboardMarkup.create(keyboard)