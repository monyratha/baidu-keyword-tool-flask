from unittest.mock import patch, MagicMock

import pytest

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, fetch_related_terms


def test_index_get():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Baidu Keyword Extractor' in resp.data


@patch('requests.get')
def test_fetch_related_terms(mock_get):
    html = '''<div class="cos-row cos-space-pb-xs font-size-upgrade_2fasj"><div class="cos-col"><span class="content-link_2AXFK c-fwb">term1</span></div></div>'''
    mock_resp = MagicMock()
    mock_resp.text = html
    mock_resp.raise_for_status = lambda: None
    mock_get.return_value = mock_resp

    headers = {}
    cookies = {}
    result = fetch_related_terms('kw', headers, cookies)
    assert result == {'term1'}
