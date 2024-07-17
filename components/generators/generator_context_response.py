import os

from components import base_classes
from components.llms import llm_openai


class GeneratorContextResponse(base_classes.Generator):
    def __init__(self, llm: base_classes.LLM = None, prompt: str = None):
        if llm is None:
            llm = llm_openai.LLMOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.llm = llm
        if prompt is None:
            self.prompt = """You are an expert in answering questions using a given context. Here is the context:\n
            Context: {context}
            
            Question: {query}
            """
        else:
            self.prompt = prompt

    def generate(self, context: list[str], query: str) -> str:
        response = self.llm.generate(prompt=self.prompt.format(context=context, query=query))
        return response
