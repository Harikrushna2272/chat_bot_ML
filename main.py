from src.chat import get_response

def chat():
    print("Let's chat! (type 'quit' to exit)")
    while True:
        message = input("You: ")
        if message == "quit":
            break

        resp = get_response(message)
        print("Bot:", resp)

if __name__ == "__main__":
    chat()
