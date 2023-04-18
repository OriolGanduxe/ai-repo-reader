# ai-repo-reader

## Notes
- What is this about? Semantic search with GPT.
- Why embeddings? 
  - Is it said to offer a superior approach to fine-tuning GPT
  - It does not require any specific training data, in contrast to fine-tuning
- What are embeddings? [TO DO: link something about embeddings]
- What is Pinecone? A vector database and search engine [TO DO: link about vector database]

## Get started
Download Alice in Wonderland text
```
curl https://www.gutenberg.org/cache/epub/11/pg11.txt > alice.txt
```

Install requirements
```
!pip install langchain 
!pip install llama_index
!pip install openai
!pip install transformers
!pip install torch
!pip install sentence_transformers
!pip install pinecone-client
```
(Tip: use pyenv and pipenv to manage python version)

## Resources
- Tutorial: https://blog.futuresmart.ai/semantic-search-using-llamaindex-and-langchain