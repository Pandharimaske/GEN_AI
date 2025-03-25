from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template = 'write a joke about {topic}' , 
    input_variables = ['topic']
)

# Load the LLM
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = 'Explain the following joke - {text}' , 
    input_variables = ['text']
)

chain = RunnableSequence(prompt1 , model , parser , prompt2 , model , parser)

print(chain.invoke({'topic':'AI'}))

