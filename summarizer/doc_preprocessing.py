from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def read_document(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    text = ""
    for page in pages:
        text += page.page_content
    return text

def remove_invalid_symbols(text):
  symbols = sorted(list(set(text)))
  if 'z' not in symbols:
    symbols.append('z')
  last_index = symbols.index('z')
  inv_symbols = symbols[(last_index+1):]
  text = ''.join([char for char in text if char not in inv_symbols])
  return text

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=4000,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False
    )
    docs = splitter.create_documents([text])
    return docs

def preprocess_text(file_path):
    text = read_document(file_path)
    text = remove_invalid_symbols(text)
    docs = chunk_text(text)
    return docs