from components import base_classes


class RagStrategySimple(base_classes.RAGStrategy):
    def __init__(self):
        pass

    def read(self, documents):
        pass

    def embed(self, text):
        pass

    def retrieve(self, query):
        pass

    def generate(self, prompt: str):
        return prompt
