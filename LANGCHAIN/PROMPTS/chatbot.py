from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
load_dotenv()

model = OllamaLLM(model = 'llama3.2')

chat_history = []

while True:

    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result)
    print("AI: " , result)

print(chat_history)


