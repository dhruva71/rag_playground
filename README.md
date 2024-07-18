# RAG Playground

This is a project to implement RAG systems with very simple layers, and minimal dependencies.

## Components
The key components can be found in the `components` directory. Each component is a simple class that can be used to build a RAG system.

The base classes are:
* **LLM**: To interact with the language model. This only implements logic to interact with the model, and does not contain any logic to generate the RAG.
* **Embedder**: To generate embeddings for the text.
* **Datastore** : This stores the data, and handles retrieval as well. It uses an `Embedder` to generate the embeddings. You can inherit from this and write your own datastore logic.
* **Reader**: To handle reading various files and providing the data to the datastore.

## Current support
* ChromaDb
* OpenAI models

## Supported RAG techniques
* Naive RAG