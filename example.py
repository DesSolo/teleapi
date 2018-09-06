from tgbotapi import TgBot

bot = TgBot(token='463811481:AAHG08HbFiQq8NuFoJlaZOfKJL1-0s-XdKA')
#bot.settings = {'proxies': {'https': 222}}
#bot.settings['proxies'] = {'https': 222}
message = bot.send_message(-1001338600997, 4)
print(message.text)
bot.forward_message(-1001338600997, -1001338600997, 746)