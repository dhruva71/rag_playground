from abc import ABC, abstractmethod


class Retriever(ABC):
    @abstractmethod
    def retrieve(self, query):
        pass


class Reader(ABC):
    @abstractmethod
    def read(self, documents):
        pass


class Generator(ABC):
    @abstractmethod
    def generate(self, reader_output):
        pass


class RAGStrategy(ABC):
    @abstractmethod
    def retrieve(self, query):
        pass

    @abstractmethod
    def read(self, documents):
        pass

    @abstractmethod
    def generate(self, reader_output):
        pass
