from components import base_classes
from chromadb.utils import embedding_functions


class EmbedderChroma(base_classes.Embedder):
    """
    Embedder class for generating embeddings using a Chroma database.
    """

    def __init__(self):
        self.embedding_function = embedding_functions.DefaultEmbeddingFunction()

    def embed(self, texts: list[str]):
        return self.embedding_function(texts)

    def __call__(self, input):
        return self.embed(input)

