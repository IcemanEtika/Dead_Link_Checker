# import pytest
import requests
import DLFunctions as dlf


def test_for_200(monkeypatch):
    class mock_network_response:
        def __init__(self):
            self.status_code = 200

    def mock_url(url):
        return mock_network_response()

    monkeypatch.setattr(requests, "get", mock_url)
    assert dlf.single_link_status_checker("https://google.com") == 200


def test_for_400(monkeypatch):
    class mock_network_response:
        def __init__(self):
            self.status_code = 404

    def mock_url(url):
        return mock_network_response()

    monkeypatch.setattr(requests, "get", mock_url)
    assert dlf.single_link_status_checker("https://google.com") == 404


# Test for printing color "Good" and "Bad"
def test_good_link(capsys):
    matchedString = "\x1b[32mPASSED [200] https://google.com - Good\n"
    dlf.good_links("https://google.com", 200)
    captured = capsys.readouterr()

    assert captured.out == matchedString


def test_bad_link(capsys):
    matchedString = "\x1b[31mFAILED [400] https://google.com - Bad\n"
    dlf.bad_links("https://google.com", 400)
    captured = capsys.readouterr()

    assert captured.out == matchedString