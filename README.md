teleapi
======
[![PyPI version](https://badge.fury.io/py/teleapi.svg)](https://badge.fury.io/py/teleapi)
[![Python version](https://img.shields.io/pypi/pyversions/teleapi.svg)](https://pypi.python.org/pypi/teleapi)
[![License](https://img.shields.io/pypi/l/teleapi.svg)](https://pypi.python.org/pypi/teleapi)

Easy telegram API  
*See official telegram api [documentation](https://core.telegram.org/bots/api)*

### Install
`pip install teleapi`

### Usage
``` python
from teleapi import TelegramApi

BOT_TOKEN = 'TOKEN'
CHAT_ID = 'example_chat_id'
PROXY = 'soks5h://USERNAME:PASSWORD@IP:PORT'

telegram_api = TelegramApi(BOT_TOKEN, proxy=PROXY)
telegram_api.send_message(CHAT_ID, 'Hello world!')
```
More [examples](https://github.com/DesSolo/TeleBotProxy/blob/master/example.py)
