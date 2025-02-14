from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
print("Running OpenAI Chat Model")

model = ChatOpenAI(model = 'gpt-4' , temperature = 0 , max_completion_toknes = 10)

# result = model.invoke("What is the capital of India?")
result = model.invoke("Suggest me 5 indian male names")

print(result.content)

print("model run successfully")
