from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Initialize the LLM
load_dotenv()

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

# Define the Input
topic = input("Enter a topic")

# Format the prompt manually using PromptTemplate
formatted_prompt = prompt.format(topic = topic)

# Call the LLM directly
blog_title = llm.predict(formatted_prompt)

# Print the output
print("Generated Blog Title:" , blog_title)

