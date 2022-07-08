import telegram

token = '5536319569:AAEoQcgDqWIvhFDsVU52jk8vt5s3-jXWD3g'
bot = telegram.Bot(token = token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)