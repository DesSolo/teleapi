import os
import pytest
from teleapi import TelegramApi

TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']
PROXY = os.environ['PROXY']


@pytest.fixture()
def client():
    return TelegramApi(TOKEN, proxy=PROXY)


def test_token():
    api = TelegramApi(TOKEN)
    assert api.url == f'https://api.telegram.org/bot{TOKEN}/'


@pytest.mark.parametrize(
    'proxy',
    [
        'https://example.com',
        'http://example.com:443',
        'socks5://example.com',
        'socks5h://user@password:example.com'
    ]
)
def test_proxies(proxy):
    api = TelegramApi(TOKEN, proxy=proxy)
    assert api.session.proxies['https'] == proxy


def test_send_message(client):
    message = client.send_message(CHAT_ID, 'test')
    assert message.status_code == 200
    assert message.json()['result']['message_id']


def test_send_message_markdown(client):
    text = """
    *bold text*
    _italic text_
    [text](URL)
    """
    message = client.send_message(CHAT_ID, text, parse_mode="Markdown")
    assert message.status_code == 200
    assert message.json()['result']['message_id']


def test_send_message_disable_notification(client):
    message = client.send_message(CHAT_ID, 'test', disable_notification=True)
    assert message.status_code == 200
    assert message.json()['result']['message_id']


def test_send_photo_url(client):
    message = client.send_photo(CHAT_ID, 'https://via.placeholder.com/150')
    assert message.status_code == 200
    assert message.json()['result']['message_id']


def test_send_photo_file(client):
    message = client.send_photo(CHAT_ID, 'test_data/photo.png')
    assert message.status_code == 200
    assert message.json()['result']['message_id']


def test_send_document_url(client):
    message = client.send_document(CHAT_ID, 'https://via.placeholder.com/150')
    assert message.status_code == 200
    assert message.json()['result']['message_id']


def test_send_document_file(client):
    message = client.send_document(CHAT_ID, 'test_data/photo.png')
    assert message.status_code == 200
    assert message.json()['result']['message_id']
