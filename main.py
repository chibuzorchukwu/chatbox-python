"""Run the chatbox as an interactive terminal chat."""
from chatbox import get_response


def main() -> None:
    print("Chatbox ready. Type 'exit' or 'quit' to leave.")
    while True:
        try:
            text = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if not text:
            continue
        reply = get_response(text)
        print(f"bot> {reply}")
        if text.lower() in {"exit", "quit", "bye", "goodbye"}:
            break


if __name__ == "__main__":
    main()
