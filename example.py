from tgbotapi import TgBot

bot = TgBot(token='Token')
#bot.settings = {'proxies': {'https': 222}}
#bot.settings['proxies'] = {'https': 222}
message = bot.send_message(-1001338600997, 4)
print(message.text)
bot.forward_message(-1001338600997, -1001338600997, 746)