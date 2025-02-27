# from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate , load_prompt

from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = OllamaLLM(model = 'llama3.2')

st.header("Reasearch Tool")

paper_input = st.selectbox("Select Reasearch Paper Name" , ["Select..." , "Attention Is All You Need" , "BERT: Pre-training of Deep Bidirectional Transformers" , "GPT-3: Language Models are Few-Shot Learners" , "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style" , ["Begineer-Friendly" , "Technical" , "Code-Oriented" , "Mathematical"])

length_input = st.selectbox("Select Explanation Length" , ["Short (1-2 paragraphs)" , "Medium (3-5 paragraphs)" , "Long (detailed explanation)"])

template = load_prompt("template.json")


# fill the placeholders
prompt = template.invoke({
    'paper_input': paper_input , 
    'style_input': style_input , 
    'length_input': length_input
})


if st.button("Summarize"):
    result = llm.invoke(prompt)
    st.write(result)

