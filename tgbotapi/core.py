import requests
import os


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

    def _post(self, data, url, **kwargs):
        return requests.post(self.url + url, data=data, files=kwargs.get('files'), **self.settings)


class TgBot(Base):
    def send_message(self, chat_id, text, **kwargs):
        return self._post(locals(), 'sendMessage')

    def forward_message(self, chat_id, from_chat_id, message_id, **kwargs):
        return self._post(locals(), 'forwardMessage')

    def send_photo(self, chat_id, photo, **kwargs):
        if not os.path.isfile(photo):
            return self._post(locals(), 'sendPhoto')
        with open(photo, 'rb') as ph:
            photo = ph.read()
        return self._post({'chat_id': chat_id, **kwargs}, 'sendPhoto', files={"photo": photo})