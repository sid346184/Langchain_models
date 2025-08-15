from langchain_groq import ChatGroq
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
# For continuous chat but it is not recommended as when the chat gets bigger and bigger it is difficult to identify which message is of AI and which has of human so we have to maintain a dictionary instead of a list and langchain has built in classes for this, it is called (MESSAGES).
# GO TO chatbotv2.py 
chat_history=[]


while True:
    user_input = input('You: ')
    chat_history.append(user_input) 
    if user_input == 'exit':
        break
    else:
        result=llm.invoke(chat_history)
        chat_history.append(result.content)
        print ("AI: ",result.content)
