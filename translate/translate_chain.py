import os

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

parser = StrOutputParser()

prompt_template = ChatPromptTemplate.from_messages(
    [("system", "Translate the following into {language}:"), ("user", "{text}")]
)

chain = prompt_template | model | parser

chain.invoke({"language": "italian", "text": "hi"})
