from chatbox import get_response
from chatbox.intents import FALLBACK_RESPONSES


def test_greeting():
    assert get_response("hi there") in [
        "Hey there!", "Hello!", "Hi, how can I help?"
    ]


def test_farewell():
    assert get_response("bye") in ["Goodbye!", "See you later!", "Bye for now."]


def test_thanks():
    assert get_response("thank you so much") in [
        "You're welcome!", "Anytime!", "No problem."
    ]


def test_unknown_falls_back():
    assert get_response("xyzzy plugh quux") in FALLBACK_RESPONSES


def test_case_insensitive():
    assert get_response("HELLO") in ["Hey there!", "Hello!", "Hi, how can I help?"]
