from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough , RunnableBranch , RunnableLambda

load_dotenv()

# Load the LLM
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template = "Write a detailed report on {topic}" , 
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Summarize the following text /n {text}" , 
    input_variables = ['text']
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1 , model , parser)

branch_chain = RunnableBranch(
    (lambda x : len(x.split()) > 300 , RunnableSequence(prompt2 , model , parser)) ,
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain , branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))

