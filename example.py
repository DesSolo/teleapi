from tgbotapi import TgBot

bot = TgBot(token='TOKEN')
bot.settings = {'proxies': {'https': 'https://USERNAME:PASSWORD@IP:PORT'}}
bot.settings['proxies'] = {'https': 'https://USERNAME:PASSWORD@IP:PORT'}
message = bot.send_message(-1001338600997, 'Hello')
print(message.text)
message = bot.forward_message(-1001338600997, -1001338600997, 1) # 1 - id message
print(message.text)
photo = bot.send_photo(-1001338600997, '/PATH/TO/FILE/SOME_FILE')
print(photo.text)
photo = bot.send_photo(-1001338600997, 'https://pbs.twimg.com/profile_images/1019623145471295488/SZCsC2Ci_400x400.jpg')
print(photo.text)