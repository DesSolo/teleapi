import pytest
from teleapi import TelegramApi
from teleapi.core import input_file_or_string
from tempfile import NamedTemporaryFile


@pytest.mark.parametrize(
    'token',
    [
        'test_token',
        'test_token`'
    ]
)
def test_token(token):
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


def generate_temp_file(data):
    tmp_file = NamedTemporaryFile('w', delete=False)
    tmp_file.write(data)
    return tmp_file.name


@pytest.mark.parametrize(
    'source, resp_data, resp_files',
    [
        ({'audio': 'test_audio'}, {'audio': 'test_audio'}, {}),
        ({'video1': 'test_video1', 'video2': 'test_video2'}, {'video1': 'test_video1', 'video2': 'test_video2'}, {}),
        ({'video': generate_temp_file('test_text')}, {}, {'video': b'test_text'}),
        ({'file': generate_temp_file('test'), 'audio': 'test'}, {'audio': 'test'}, {'file': b'test'}),
    ]
)
def test_input_file_or_string(source, resp_data, resp_files):
    data, files = input_file_or_string(**source)
    assert data == resp_data
    assert files == resp_files
