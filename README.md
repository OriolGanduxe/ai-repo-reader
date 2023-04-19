# ai-repo-reader

## Notes
- What is this about? Semantic search with GPT.
- Why embeddings? 
  - Is it said to offer a superior approach to fine-tuning GPT
  - It does not require any specific training data, in contrast to fine-tuning
- What are embeddings? [TO DO: link something about embeddings]
- What is Pinecone? A vector database and search engine [TO DO: link about vector database]

### Get started
Follow instructions in `example/notebook.ipynb`

### Prepare environment

[pyenv](https://realpython.com/intro-to-pyenv/) makes it easy to manage python versions without conflicts

- Build dependencies
```
brew install openssl readline sqlite3 xz zlib
```

- Install pyenv
```
curl https://pyenv.run | bash
```

- Install pyenv 3.10.6
```
pyenv install -v 3.10.6
```

- Set global python version
```
pyenv global 3.10.6
```

[pipenv](https://realpython.com/pipenv-guide/) makes it easy to manage python packages and virtual environments
```
pip install pipenv
```

- Install jupyterlab
```
pipenv install jupyterlab
```

- Activate the project virtual environment
```
pipenv shell
```

- Start jupyterlab
```
jupyter lab
```

A browser window should open with the jupyterlab interface. The source code is under `example/notebook.ipynb`
Tip: You can also run the notebook in VSCode, using the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

## Resources
- Tutorial: https://www.mlq.ai/gpt-3-enabled-research-assistant-langchain-pinecone/