from teleapi import TelegramApi

api = TelegramApi(token='TOKEN')
api_proxy = TelegramApi(token='TOKEN', proxy='https://USERNAME:PASSWORD@IP:PORT')

message = api.send_message(-100, 'Hello')
print(message.text)
message = api.forward_message(-100, -100, 1)  # 1 - id message
print(message.text)
photo = api.send_photo(-100, '/PATH/TO/FILE/SOME_FILE')
print(photo.text)
photo = api.send_photo(-100, 'https://exapmle.com/test.jpg')
print(photo.text)
