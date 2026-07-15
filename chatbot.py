def chatbot():
    print("===== Basic Chatbot =====")
    print("Type 'bye' to exit the chat.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")
        elif user == "what is your name":
            print("Bot: I am a simple Python Chatbot.")
        elif user == "who created you":
            print("Bot: I was created using Python.")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()