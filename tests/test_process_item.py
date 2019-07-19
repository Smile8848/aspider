import pytest
from requests_html import HTMLSession, HTML
from example.parser import parse_item


@pytest.fixture
def html():
    url = 'https://www.cdnbus.bid/MADM-116'
    with open('./tests/html.txt') as f:
        html = f.read()
    return html


def test_process_item(html):
    print('')
    meta, tags = parse_item(html)
    print(meta)
    print(tags)
