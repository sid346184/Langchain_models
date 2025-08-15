from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=1.5,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

chat_template=ChatPromptTemplate([
    ('system','You are a helpful expert in {domain}'),
    ('user','Explain the topic in detail as an expert in {domain}, what is {topic} in 4-5 lines')

    # We dont use it in dynamic messages because langchain does not support it
    # SystemMessage(content='You are a helpful expert in {domain}'),
    # HumanMessage(content="Explain the topic in detail as an expert in {domain}, what is {topic}")
])

prompt=chat_template.invoke({'domain':'cricket','topic':'rules'})
print(prompt)

answer=llm.invoke(prompt)
chat_template.append(AIMessage(content=answer.content))
print(chat_template[-1].content)  