# Simple Python Chatbot

![Chatbot](chatbot.png)

This is a simple text-based chatbot implemented in Python using the Natural Language Toolkit (NLTK) library. The chatbot engages in conversations with users by responding to various patterns defined in its conversation pairs.

## Features

- Responds to greetings such as "hi", "hello", and "hey".
- Answers inquiries about its well-being and name.
- Provides a virtual location and acknowledges its lack of physical presence.
- Politely declines requests related to real-time weather updates and purchasing assistance.
- Allows users to exit the conversation by typing "quit".

## Usage

1. **Install NLTK library**:
    ```bash
    pip install nltk
    ```

2. **Run the script**:
    ```bash
    python chatbot.py
    ```

3. **Engage in conversation** with the chatbot by typing messages and pressing Enter.

4. **Type "quit"** to exit the conversation.

## Customization

You can customize the chatbot's responses and patterns by modifying the conversation pairs defined in the script. Each pair consists of a regular expression pattern and a list of possible responses.

## Dependencies

- Python 3.x
- NLTK library

## Acknowledgments

The chatbot's implementation is inspired by various NLTK tutorials and examples available online.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
