from abc import ABC, abstractmethod
from typing import Optional


class LLM(ABC):
    """
    Base class for LLM. This provides the interface for using a language model.
    """

    @abstractmethod
    def generate(self, prompt):
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
    Base class for Generator. This provides the interface for generating text using an LLM object.
    """

    @abstractmethod
    def generate(self, context: list[str], query: str):
        pass


class Embedder(ABC):
    """
    Base class for Embedder. This provides the interface for embedding text.
    """

    @abstractmethod
    def embed(self, text):
        pass


class Datastore(ABC):
    """
    Base class for DataStore. This provides the interface for storing and retrieving data.
    """

    @abstractmethod
    def store(self, data) -> Optional[str]:
        pass

    @abstractmethod
    def store_many(self, documents: list[str]) -> Optional[list[str]]:
        pass

    @abstractmethod
    def retrieve(self, query):
        pass

    @abstractmethod
    def delete(self, query):
        pass

    @abstractmethod
    def update(self, query, data):
        pass

    @abstractmethod
    def list(self, query):
        pass

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def create_collection(self, collection):
        pass

    @abstractmethod
    def drop_collection(self, collection):
        pass

    @abstractmethod
    def create_database(self, database):
        pass

    @abstractmethod
    def drop_database(self, database):
        pass

    @abstractmethod
    def create_tenant(self, tenant):
        pass

    @abstractmethod
    def drop_tenant(self, tenant):
        pass

    @abstractmethod
    def get_collection(self, collection):
        pass

    @abstractmethod
    def get_database(self, database):
        pass

    @abstractmethod
    def get_tenant(self, tenant):
        pass

    @abstractmethod
    def get_client(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class RAGStrategy(ABC):
    """
    Base class for RAG strategy.
    This provides the interface for reading, embedding, generating and retrieving documents.
    """

    @abstractmethod
    def retrieve(self, query):
        pass

    @abstractmethod
    def read_and_store_documents(self, documents):
        pass

    @abstractmethod
    def generate(self, context: list[str], query: str):
        pass

    @abstractmethod
    def embed(self, text):
        pass
