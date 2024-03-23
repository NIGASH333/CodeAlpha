import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!"]
    ],
    [
        r"what is your name ?",
        ["You can call me Chatbot.", "I'm just a simple chatbot."]
    ],
    [
        r"(.) your name (.)",
        ["You can call me Chatbot.", "I'm just a simple chatbot."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual chatbot, so I don't have a physical location.", "I exist in the virtual world."]
    ],
    [
        r"(.) (weather|temperature) in (.)?",
        ["I'm sorry, I'm just a text-based chatbot and cannot provide real-time weather updates."]
    ],
    [
        r"(.) (buy|purchase) (.)",
        ["I'm sorry, I'm just a chatbot and cannot assist with purchasing."]
    ],
    [
        r"quit",
        ["Goodbye!", "Take care!"]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def chat():
    print("Welcome! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    nltk.download('punkt')
    chat()
