from components import base_classes
from chromadb.utils import embedding_functions


class EmbedderChroma(base_classes.Embedder):
    """
    Embedder class for generating embeddings using a Chroma database.
    """

    def embed(self, text):
        """
        Embeds text using the Chroma database.
        :param text: Text to embed.
        :return: Embedding of the text.
        """
        embedding_function = embedding_functions.DefaultEmbeddingFunction()
        return embedding_function(text)
