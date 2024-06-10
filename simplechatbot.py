import re

patterns = {
    "hello||hi": "Hello! How can I help you today?",
    "how are you": "I'm a chatbot, so I'm always good. How about you?",
    "bye": "Goodbye! Have a nice day!",
}

def respond(user_input):
    for pattern, response in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that. Can you please rephrase?"


print("ChatBot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = respond(user_input)
    print("ChatBot:", response)
    if user_input.lower() == "bye":
        break
