def chatbot():
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!"
    }
    
    print("Chatbot started (type 'bye' to exit)")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Bot: Goodbye!")
            break
        
        # .get() returns a default if the key isn't found
        reply = responses.get(user_input, "I don't understand that.")
        print(f"Bot: {reply}")

if __name__ == "__main__":
    chatbot()