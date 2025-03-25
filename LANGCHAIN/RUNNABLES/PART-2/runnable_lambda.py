from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough , RunnableLambda

def word_counter(text):
    return len(text.split())


prompt = PromptTemplate(
    template = "Write a joke about {topic}" , 
    input_variables = ['topic']
)

# Load the LLM
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt , model , parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough() , 
    'word_count': RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_gen_chain , parallel_chain)

print(final_chain.invoke({'topic':'Cricket'}))
