from langchain.prompts import PromptTemplate

chunks_prompt_template = """
You will be given one passage from the book. Your goal is to provide a summary of this section so that the reader has an understanding of what the text is about.
Your answer should reflect what is said in the passage and retain the main terms and quotations. Add a title reflecting the main point of the passage. Do not add introduction and conclusion to the summary. 
Paraphrase the text, do not write in the third person.
text: {text}
"""

chunks_prompt = PromptTemplate(
    input_variables=['text'],
    template=chunks_prompt_template
)

# final_prompt_template = """
# You will be given a list of summaries of passages of a book. Your goal is to provide a structured outline of this section so that 
# the reader has a complete understanding of what each summarized passage is about.
# The outline should retain the main terms and quotations.
# text: {text}
# """

# final_prompt = PromptTemplate(
#     input_variables=['text'],
#     template=final_prompt_template
# )