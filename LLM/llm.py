from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=1.5,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

user_input=input("Enter your query:" )

messages=[
    SystemMessage(content="You are a helpful AI assistant who answers all my queries correctly."),
    HumanMessage(content=user_input)
]

result=llm.invoke(messages)
print(result.content)