from teleapi import TelegramApi

api = TelegramApi(token='TOKEN')
api.settings = {'proxies': {'https': 'https://USERNAME:PASSWORD@IP:PORT'}}
api.settings['proxies'] = {'https': 'https://USERNAME:PASSWORD@IP:PORT'}
message = api.send_message(-1001338600997, 'Hello')
print(message.text)
message = api.forward_message(-1001338600997, -1001338600997, 1)  # 1 - id message
print(message.text)
photo = api.send_photo(-1001338600997, '/PATH/TO/FILE/SOME_FILE')
print(photo.text)
photo = api.send_photo(-1001338600997, 'https://pbs.twimg.com/profile_images/1019623145471295488/SZCsC2Ci_400x400.jpg')
print(photo.text)
