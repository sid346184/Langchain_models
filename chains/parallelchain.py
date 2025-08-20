from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv
load_dotenv()

llm1=ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)
llm2=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Based on the {topic}, provide me the detailed notes for my exam",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="Generate 5 question answers on the following {topic}",
    input_variables=['topic']
)
prompt3=PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'notes':prompt1 | llm1 | parser,
    'quiz':prompt2 | llm2 | parser
})

merged_chain = prompt3 | llm1 | parser

chain = parallel_chain | merged_chain
print(chain.invoke({'topic':'AI and Machine Learning'}))