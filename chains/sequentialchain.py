from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

user_input=input("Enter the topic: ")

prompt1=PromptTemplate(
    template="Write a summary on the {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Write a 6 line poem on the {topic}",
    input_variables=['topic']
)
parser=StrOutputParser()

chain= prompt1 | llm | parser | prompt2 | llm | parser
print(chain.invoke({'topic':user_input}))