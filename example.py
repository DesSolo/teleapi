from tgbotapi import TgBot

bot = TgBot(token='sdsdsd')
#bot.settings = {'proxies': {'https': 222}}
#bot.settings['proxies'] = {'https': 222}
#message = bot.send_message(-1001338600997, 4)
#print(message.text)
bot.forward_message(-1001338600997, -1001338600997, 746)
f = bot.send_photo(-1001338600997, '/home/solo/Изображения/Выделение_007.jpg')
f = bot.send_photo(-1001338600997, 'https://pbs.twimg.com/profile_images/1019623145471295488/SZCsC2Ci_400x400.jpg')
print(f.text)