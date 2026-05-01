from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from src.domain.prompts import main_prompt
from src.clients.qdrant import retriever
from src.domain.llm import llm

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | ChatPromptTemplate.from_template(main_prompt)
    | llm
    | StrOutputParser()
)
