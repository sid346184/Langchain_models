from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv
load_dotenv()

llm1=ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['pos','neg']=Field(description="Give the sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template=("Classify the sentiment of the following feedback into positive or negative \n {feedback}"
    "Feedback:{feedback}"
    "{format_instruction}"
    ),
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain= prompt1 | llm1 |parser2

prompt2=PromptTemplate(
    template="Write an approprite response to this positive feedback \n {feedbacK}",
    input_variables=['feedback']
)
prompt3=PromptTemplate(
    template="Write an approprite response to this negative feedback \n {feedbacK}",
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    # (condition1,chain1),
    # (condition2,chain2),
    # default chain

    (lambda x:x.sentiment=='pos',prompt2|llm1|parser),
    (lambda x:x.sentiment=='neg',prompt3|llm1|parser),
    RunnableLambda(lambda x: "could not find sentiment")                               # since it is not a chain so we need to convert it into runnable
)

chain=classifier_chain | branch_chain

print(chain.invoke({'feedback':'This is a terrible phone'}))