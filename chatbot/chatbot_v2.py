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
user_input=input("Ask your query: ")

messages=[
    SystemMessage(content="You are an helpful assistant which answers all the queries"),
    HumanMessage(content=user_input),
]

result = llm.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages[-1].content) # IF you only want to print the ai message

