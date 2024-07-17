from abc import ABC, abstractmethod


class Retriever(ABC):
    """
    Base class for Retriever. This provides the interface for retrieving documents.
    """

    @abstractmethod
    def retrieve(self, query):
        pass


class Reader(ABC):
    """
    Base class for Reader. This provides the interface for reading documents.
    """

    @abstractmethod
    def read(self, documents):
        pass


class Generator(ABC):
    """
    Base class for Generator. This provides the interface for generating text using a reader output.
    """

    @abstractmethod
    def generate(self, reader_output):
        pass


class Embedder(ABC):
    """
    Base class for Embedder. This provides the interface for embedding text. This is where the logic for storing in the
    database should be implemented.
    """

    @abstractmethod
    def embed(self, text):
        pass


class RAGStrategy(ABC):
    """
    Base class for RAG strategy.
    """

    @abstractmethod
    def retrieve(self, query):
        pass

    @abstractmethod
    def read(self, documents):
        pass

    @abstractmethod
    def generate(self, reader_output):
        pass

    @abstractmethod
    def embed(self, text):
        pass
