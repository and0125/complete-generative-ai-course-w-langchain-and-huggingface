# Notes

We create an API key and use it within an `.env` file.

I created this API key from Claude.

Also needed a langchain API key, and a Lanchaing Project name.

Once these are done, you'd need the following packages:

- langchain
- python-dotenv: for importing env variables in jupyter notebooks.
- langchain_community (needed as well)
- pypdf (for pdf processing)

This Will set you up to work with LangChain, LangSmith, and LangServe.

Then we'll use prompt templates, models, and output parsers.

## Basic Components of Langchain

Before we start to use the library, lets look at the most important concepts of the library.

side note: retrieval augmented generation is used when you have a specific data source (like a pdf file). If you want to make that PDF into a Q&A bot application, where a user can ask a query and send the response from the pdf. This is a high level overview; and we can create a gen ai app from this, so that when any question is asked, the user can converse with the data source.

We'll look at the components we need to do this.

First, we need to **load the data set**. Could be PDF, images, URL, etc. whenever we do this sort of application, data ingestion is the most important component.

Then we'll **split pdfs into chunks**. This is because in later stages, when we use the model, the model has limitations on the context we can provide, called the `context size`. The data will be split into chunks, and this is done as a data transformation technique -- main output is chunked data.

3rd step is to **embed the data**. This is `text embedding`, taking the text and converting it into vectors. This enables things like similarity search, which can use a cosine search to understand the differences between the sentences you are trying to find. There are plenty of open source embedding technique.

Fourth, we need to store the vectors somewhere, which would be a **vector store database**. THere are a number of these, like FAISS, ChromaDB, AstraDB. From the vector db you can query this as well, but it will respond with just the context from the documents, not a crafted response. The vector databases are useful; and the responses from just the vector db are based on the similarity search.

Then there's another part of the diagram, to talk through the prompt setup for the LLM, and assigning the model a role. From querying, the user will ask the vector store based on the system role and the document staff load check, and then use a retrieval chain, which is responsible for querying the vector store DB. Through this reflection on the document, the model will retrieve and return your responses.

You'd create a retrieval chain along with a prompt template to the LLM to get the response.

## Important Components of Langchain

We can do all the above steps with langchain.

data ingestion can be done with the document loader in langchain.

Need to get into the habit of reading the documentation; it is very scattered. The videos order the package to be easier to follow.

Document loaders are a bunch of different ways to optimize loading documents.

We'll go over the most common use cases for loading documents though.

The first is the `text loader`, which is helpful for any `.txt` file.

```python
from langchain_community.document_loaders import TextLoader

# initialize with file path
loader = TextLoader("/path/to/file.txt")

# creates a python object of the text
text_documents = loader.load()
```

For a pdf file:

```python
from langchain_community.document_loaders import PyPDFLoader

docs = PyPDFLoader('attention.pdf')
```
