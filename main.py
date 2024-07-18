from components.rag_strategy import rag_strategy_naive
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    rag_strategy = rag_strategy_naive.RagStrategyNaive()

    documents = [
        "The capital of France is Paris.",
        "The capital of Spain is Madrid.",
        "France won the 2018 FIFA World Cup.",
        "Spain won the 2010 FIFA World Cup.",
        "The Eiffel Tower is in Paris.",
        "France is famous for its wines.",
        "Spain is famous for its beaches.",
        "USA is famous for its fast food.",
        ]

    ids = rag_strategy.read_and_store_documents(documents)

    query = "What is the capital of France?"
    retrieved_documents = rag_strategy.retrieve(query)

    context = [retrieved_documents[0]]
    response = rag_strategy.generate(context=context, query=query)

    print(response)