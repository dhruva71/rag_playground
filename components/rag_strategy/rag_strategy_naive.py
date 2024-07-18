import os
from typing import Optional

import components.llms.llm_openai
from components import base_classes
from components.embedders import embedder_chroma
from components.datastores import datastore_chroma
from components.generators import generator_context_response


class RagStrategyNaive(base_classes.RAGStrategy):
    def __init__(self, llm: Optional[base_classes.LLM] = None, embedder: Optional[base_classes.Embedder] = None,
                 datastore: Optional[base_classes.Datastore] = None,
                 generator: Optional[base_classes.Generator] = None):
        if llm is None:
            llm = components.llms.llm_openai.LLMOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        if embedder is None:
            embedder = components.embedders.embedder_chroma.EmbedderChroma()
        if datastore is None:
            datastore = components.datastores.datastore_chroma.DatastoreChroma()
        if generator is None:
            generator = components.generators.generator_context_response.GeneratorContextResponse(llm=llm)

        self.llm = llm
        self.embedder = embedder
        self.datastore = datastore
        self.generator = generator

    def read_and_store_documents(self, documents: list[str]):
        self.datastore.store_many(documents=documents)

    def embed(self, text):
        return self.embedder.embed(text)

    def retrieve(self, query):
        self.datastore.retrieve(query=query)

    def generate(self, context: list[str], query: str):
        self.generator.generate(context=context, query=query)
