
print("ChatBot: Hello! Type 'bye' to exit.")

while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("ChatBot: Hi! How are you?")
        elif user_input == "how are you":
            print("ChatBot: I'm fine, thank you!")
        elif user_input == "what is your name":
            print("ChatBot: My name is ChatBot.")
        elif user_input == "bye":
            print("ChatBot: Goodbye!")
            break
        else:
            print("ChatBot: Sorry, I don't understand.")

# Run the chatbot
chatbot()