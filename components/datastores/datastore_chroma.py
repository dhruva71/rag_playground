from typing import Optional

import chromadb
from chromadb.utils import embedding_functions

import components.base_classes
from components import base_classes
from components.embedders import embedder_chroma


def _verify_collection_name(collection_name):
    if len(collection_name) < 3 or len(collection_name) > 64:
        raise ValueError("Collection name must be between 3-64 characters.")


class DatastoreChroma(base_classes.Datastore):
    """
    Embedder class for storing embeddings in a Chroma database.
    """

    def __init__(self, storage_path=None, tenant_id: Optional[str] = None, database: Optional[str] = None,
                 collection_name: Optional[str] = None, embedder: Optional[components.base_classes.Embedder] = None,
                 collection_metadata: Optional[dict[str, str]] = None):
        """
        Initializes the EmbedderChroma object.
        :param storage_path: Path to the Chroma database. If None, uses "./chromadb".
        :param tenant_id: Tenant ID for the Chroma database. If None, uses the default tenant.
        :param database: Database name for the Chroma database. If None, uses the default database.
        :param collection_name: Collection name for the Chroma database. If None, uses "default_collection".
        :param embedding_function: Embedding function to use for embedding text. If None, uses the default embedding.
        :param collection_metadata: Metadata to store with the collection.
        """
        self.collection = None
        if storage_path is None:
            storage_path = "./chromadb"
        if tenant_id is None:
            tenant_id = chromadb.DEFAULT_TENANT
        if database is None:
            database = chromadb.DEFAULT_DATABASE
        if collection_name is None:
            collection_name = "default_collection"
        if embedder is None:
            embedder = components.embedders.embedder_chroma.EmbedderChroma()

        # collection name must be between 3-64 characters
        _verify_collection_name(collection_name)

        self.embedder = embedder
        self.collection_metadata = collection_metadata

        try:
            self.db_client = chromadb.PersistentClient(path=storage_path, tenant=tenant_id, database=database)
            self.create_collection(collection_name=collection_name,
                                   embedding_function=self.embedder,
                                   collection_metadata=collection_metadata)
        except Exception as e:
            raise ValueError(f"Error initializing Chroma database: {e}")

    def store(self, text: str, collection: Optional[str] = None, metadata: Optional[list[str]] = None) -> str:
        if collection is None:
            collection = self.collection
        document_id = f'id_{self.count()}'  # generate a unique ID
        collection.add(documents=[text], ids=[document_id], metadatas=metadata)

        return document_id

    def store_many(self, documents: list[str], collection: Optional[str] = None,
                   metadata: Optional[list[str]] = None) -> list[str]:
        if collection is None:
            collection = self.collection
        document_ids = [f'id_{self.count() + i}' for i in range(len(documents))]
        self.collection.add(documents=documents, ids=document_ids, metadatas=metadata, )

        return document_ids

    def retrieve(self, query: str, collection: Optional[str] = None, num_results: int = 3, **kwargs):
        """
        Retrieves documents from the collection based on the query. Returns the top `num_results` documents.
        :param query: The query to search for.
        :param collection: The collection to search in. If None, uses the default collection.
        :param num_results: The number of results to return. Default is 3.
        :param kwargs: Extra arguments to pass to the Chroma query. For example, `where`, `where_document`, etc.
        :return: List of documents matching the query.
        """
        if collection is None:
            collection = self.collection
        return collection.query(
            query_texts=[query],
            n_results=3,
            **kwargs
        )

    def delete(self, query):
        raise NotImplementedError("Delete operation is not implemented yet.")

    def update(self, query, data):
        pass

    def list(self, query):
        pass

    def count(self):
        return self.collection.count()

    def create_collection(self, collection_name: Optional[str] = None, embedding_function=None,
                          collection_metadata: Optional[dict[str, str]] = None) -> chromadb.Collection:
        """
        Creates a new collection in the database. If the collection already exists, it will be overwritten.
        :param collection_name:
        :param embedding_function:
        :param collection_metadata:
        :return:
        """
        self.collection = self.db_client.create_collection(collection_name,
                                                           embedding_function=self.embedder,
                                                           metadata=collection_metadata)
        return self.collection

    def drop_collection(self, collection: Optional[str] = None):
        if collection is None:
            collection = self.collection.name
        self.db_client.delete_collection(collection)

    def create_database(self, database):
        pass

    def drop_database(self, database):
        pass

    def create_tenant(self, tenant):
        pass

    def drop_tenant(self, tenant):
        pass

    def get_collection(self, collection):
        pass

    def get_database(self, database):
        pass

    def get_tenant(self, tenant):
        pass

    def get_client(self):
        return self.db_client

    def close(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
