from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",dimensions=300)

documents=[
    "Virat Kohli is the captain of Indian Team.",
    "Ms Dhoni is also known as Captain Cool.",
    "Bumrah gives the best yorker.",
    "Sachin is the God of Cricket."
]

query='tell me about Dhoni'

doc_embeddings=embedding.embed_documents(documents)
query_embeddings=embedding.embed_query(query)

scores=cosine_similarity([query_embeddings],doc_embeddings)[0]

# print (list(enumerate(scores)))
# It will provide the rankings to the scores  eg-> [(0, np.float64(0.6511644401781207)), (1, np.float64(0.7459252569209522)), (2, np.float64(0.6124251964028031)), (3, np.float64(0.6443834094919494))]

index, result=(sorted(list(enumerate(scores)),key=lambda x:x[1])[-1])

print(documents[index])
print("similarity score is: ", result)
