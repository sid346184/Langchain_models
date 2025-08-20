from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm=ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

prompt=PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

user_input=input("Enter the topic: ")
parser=StrOutputParser()

chain=prompt | llm | parser

result=(chain.invoke({"topic":user_input}))
print(result)
# chain.get_graph().print_ascii()     to print the chain structure