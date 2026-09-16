# Chatbox

A simple pattern-matching chatbot in Python. Picked up from the "Machine Learning Projects" GitHub board.

## Run it

```bash
python3 main.py
```

## Test it

```bash
python3 -m pytest tests/
```

## How it works

`chatbox/intents.py` defines a list of `Intent`s, each with regex patterns and a set of possible responses. `get_response()` checks user input against each intent in order and returns a random matching response, or a fallback if nothing matches.

## Next steps

- Add more intents (weather, jokes, etc.)
- Swap the rule-based matcher for an actual NLP/embedding-based intent classifier
- Add a simple web UI (Flask/FastAPI) instead of the terminal loop
