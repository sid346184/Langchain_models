from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_groq import ChatGroq
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

messages=[
    SystemMessage(content="You are an helpful assistant which answers all the queries"),
]

while True:
    user_input=input("Ask your query: ")
    if user_input.lower()=="exit":
        break
    messages.append(HumanMessage(content=user_input))
    result=llm.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print(result.content)
