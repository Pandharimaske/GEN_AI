from langchain_openai import OpenaAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenaAIEmbeddings(model = 'text-embedding-3-large' , dimension = 32)

documents = [
    "Delhi is the capital of india" , 
    "Kolkata is the capital of West Bengal" , 
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))
