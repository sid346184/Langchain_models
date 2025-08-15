from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
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

### ChatTemplate

chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer agent'),
    MessagesPlaceholder(variable_name='chat_history'),  # It is used to fetch the chat history and then give outputs accordingly 
    ('human','{query}')
])


chat_history=[]
### load chat history
try:
    with open('chat_history.txt', 'r') as f:
        for line in f:
            role, content = line.strip().split(":", 1)
            chat_history.append({"type": role.strip().lower(), "content": content.strip()})
except FileNotFoundError:
    pass


### create prompt
user_input=input("What is your query: ")
prompt=chat_template.invoke({'chat_history':chat_history, 'query':user_input })

answer=llm.invoke(prompt)
print(answer.content)


with open('chat_history.txt', 'a') as f:
    f.write(f"human: {user_input}\n")
    f.write(f"ai: {answer.content}\n")

chat_history.append({"type": "ai", "content": answer.content})