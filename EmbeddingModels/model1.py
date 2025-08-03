from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings= GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001')
vector=embeddings.embed_query("HI")

print(vector[:5])