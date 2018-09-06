import requests


class Base(object):
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


class TgBot(Base):
    def send_message(self, chat_id, text, **kwargs):
        return self._post(locals(), 'sendMessage')

    def forward_message(self, chat_id, from_chat_id, message_id, **kwargs):
        return self._post(locals(), 'forwardMessage')