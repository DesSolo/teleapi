import pytest
from teleapi import TelegramApi


def test_token():
    token = 'test_token'
    api = TelegramApi(token)
    assert api.url == f'https://api.telegram.org/bot{token}/'


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
    api = TelegramApi('test_token', proxy=proxy)
    assert api.session.proxies['https'] == proxy
