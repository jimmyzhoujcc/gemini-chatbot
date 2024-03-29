import sys
from configparser import ConfigParser
from chatbot import ChatBot
import os
os.environ["http_proxy"] = "http://192.168.3.12:7890"
os.environ["https_proxy"] = "http://192.168.3.12:7890"

def main():
    config = ConfigParser()
    config.read('credentials.ini')
    api_key = config['gemini_ai']['API_KEY']

    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()
    # chatbot.clear conversation()

    print("Welcome to the JJ Gemini chatBot cLI. Type 'quit' to exit.")

    # print('{0}: {1}'.format(chatbot.CHATBOT_NAME, chatbot.history[-1]['text']))
    while True:
        user_input = input("You:")
        if user_input.lower()=='quit':
            print("Exiting chatBot cLI...")
            sys.exit()
        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as e:
            print(f"Error: {e}")

main()