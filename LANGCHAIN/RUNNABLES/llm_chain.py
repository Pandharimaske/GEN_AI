from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Load the LLM
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

# Create a Prompt Template
prompt = PromptTemplate(
    input_variables = ["topic"] , 
    template = "Suggest a catchy blog title about {topic}."
)

# Create a LLMChain
chain = LLMChain(llm = llm , prompt = prompt)

# Run the chain with a specific topic
topic = input('Enter a topic')
output = chain.run(topic)

print("Generated Blog Title:" , output)

