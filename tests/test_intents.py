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


def test_joke():
    from chatbox.intents import INTENTS
    joke_responses = next(i for i in INTENTS if i.name == "joke").responses
    assert get_response("tell me a joke") in joke_responses


def test_mood_positive():
    assert get_response("I'm feeling great today") in [
        "Glad to hear it!", "That's great!", "Love that for you."
    ]


def test_mood_negative():
    assert get_response("I'm feeling sad") in [
        "Sorry to hear that. Want to talk about it?",
        "That sounds tough. Take it one step at a time.",
    ]


def test_compliment():
    assert get_response("good bot") in ["Thanks, that means a lot!", "Aw, thank you!"]


def test_name_variants():
    assert get_response("what is your name") in [
        "I'm Chatbox, a simple pattern-matching bot.", "Call me Chatbox."
    ]
