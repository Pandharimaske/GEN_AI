from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it" , 
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}' , 
    input_variables = ['topic']
)

# model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()
