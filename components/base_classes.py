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
    def store(self, data):
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
