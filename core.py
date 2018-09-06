import requests


class TelegramBot(object):
    def __init__(self, token):
        self.token = token
        self.url = f'https://api.telegram.org/bot{token}/'
        self._settings = {}

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, value):
        self._settings = value

    def _post(self, data, url):
        data.pop('self')
        return requests.post(self.url + url, json=data, **self.settings)


class TgBot(TelegramBot):
    def send_message(self, chat_id, text, **kwargs):
        return self._post(locals(), 'sendMessage')

    def forward_message(self, chat_id, from_chat_id, message_id, **kwargs):
        return self._post(locals(), 'forwardMessage')


bot = TgBot(token='463811481:AAHG08HbFiQq8NuFoJlaZOfKJL1-0s-XdKA')
#bot.settings = {'proxies': {'https': 222}}
#bot.settings['proxies'] = {'https': 222}
message = bot.send_message(-1001338600997, 4)
print(message.text)
bot.forward_message(-1001338600997, -1001338600997, 746)