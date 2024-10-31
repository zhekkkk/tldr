from langchain_mistralai import ChatMistralAI
from langchain.chains.summarize import load_summarize_chain
from langchain_core.documents import Document

from .doc_preprocessing import preprocess_text
from .doc_selection import select_relevant_docs
from .prompts import chunks_prompt

model = ChatMistralAI(model='mistral-large-latest')

chunks_sum_chain = load_summarize_chain(
    llm=model,
    chain_type="stuff",
    prompt=chunks_prompt,
)

def summarize_chunks(docs):
    summaries = []
    for doc in docs:
        summary = chunks_sum_chain.run([doc])
        summaries.append(summary)
    return summaries

def create_final_summary(summaries):
    return '\n'.join(summaries)

def summarize_text(file_path):
    docs = preprocess_text(file_path)
    most_representative_docs = select_relevant_docs(docs)
    summaries = summarize_chunks(most_representative_docs)
    final_summary = create_final_summary(summaries)
    return final_summary