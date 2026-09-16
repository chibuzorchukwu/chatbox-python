"""Intent definitions for the chatbox: patterns to match and how to respond."""
import random
import re
from dataclasses import dataclass, field


@dataclass
class Intent:
    name: str
    patterns: list[str]
    responses: list[str]

    def matches(self, text: str) -> bool:
        return any(re.search(p, text, re.IGNORECASE) for p in self.patterns)

    def respond(self) -> str:
        return random.choice(self.responses)


INTENTS: list[Intent] = [
    Intent(
        name="greeting",
        patterns=[r"\bhi\b", r"\bhello\b", r"\bhey\b", r"^yo\b"],
        responses=["Hey there!", "Hello!", "Hi, how can I help?"],
    ),
    Intent(
        name="farewell",
        patterns=[r"\bbye\b", r"\bgoodbye\b", r"\bsee ya\b", r"\bquit\b", r"\bexit\b"],
        responses=["Goodbye!", "See you later!", "Bye for now."],
    ),
    Intent(
        name="thanks",
        patterns=[r"\bthanks\b", r"\bthank you\b", r"\bappreciate it\b"],
        responses=["You're welcome!", "Anytime!", "No problem."],
    ),
    Intent(
        name="how_are_you",
        patterns=[r"how are you", r"how's it going", r"how are things"],
        responses=["I'm doing well, thanks for asking!", "All good here!"],
    ),
    Intent(
        name="name",
        patterns=[r"what.?s your name", r"what is your name", r"who are you"],
        responses=["I'm Chatbox, a simple pattern-matching bot.", "Call me Chatbox."],
    ),
    Intent(
        name="help",
        patterns=[r"\bhelp\b", r"what can you do"],
        responses=[
            "I can chat about greetings, how you're doing, jokes, and basic small talk. "
            "Try saying hi, asking how I am, asking for a joke, or asking my name."
        ],
    ),
    Intent(
        name="joke",
        patterns=[r"\bjoke\b", r"make me laugh", r"tell me something funny"],
        responses=[
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "I told my computer I needed a break, and it said 'no problem, I'll go to sleep.'",
            "Why did the chatbot break up with the calculator? It couldn't count on it.",
        ],
    ),
    Intent(
        name="mood_positive",
        patterns=[r"i.?m (feeling )?(good|great|fine|happy|awesome)"],
        responses=["Glad to hear it!", "That's great!", "Love that for you."],
    ),
    Intent(
        name="mood_negative",
        patterns=[
            r"i.?m (feeling )?(sad|tired|bad|stressed|down)",
            r"i.?m not (feeling )?(good|great|ok|okay)",
        ],
        responses=[
            "Sorry to hear that. Want to talk about it?",
            "That sounds tough. Take it one step at a time.",
        ],
    ),
    Intent(
        name="time",
        patterns=[r"what time is it", r"current time"],
        responses=["I don't have a clock built in yet, but check your system time!"],
    ),
    Intent(
        name="compliment",
        patterns=[r"you.?re (great|awesome|smart|cool|nice)", r"good bot", r"good job"],
        responses=["Thanks, that means a lot!", "Aw, thank you!"],
    ),
]

FALLBACK_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Sorry, I don't have a response for that yet.",
    "Can you say that a different way?",
]


def get_response(text: str) -> str:
    for intent in INTENTS:
        if intent.matches(text):
            return intent.respond()
    return random.choice(FALLBACK_RESPONSES)
