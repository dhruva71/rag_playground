import chromadb
from components import base_classes


class DatastoreChroma(base_classes.Datastore):
    """
    Embedder class for storing embeddings in a Chroma database.
    """

    def __init__(self, storage_path=None, tenant_id=None, database=None, collection_name=None, embedding_function=None,
                 collection_metadata=None):
        """
        Initializes the EmbedderChroma object.
        :param storage_path: Path to the Chroma database. If None, uses "./chromadb".
        :param tenant_id: Tenant ID for the Chroma database. If None, uses the default tenant.
        :param database: Database name for the Chroma database. If None, uses the default database.
        :param collection_name: Collection name for the Chroma database. If None, uses "default_collection".
        :param embedding_function: Embedding function to use for embedding text. If None, uses the default embedding.
        :param collection_metadata: Metadata to store with the collection.
        """
        if storage_path is None:
            storage_path = "./chromadb"
        if tenant_id is None:
            tenant_id = chromadb.DEFAULT_TENANT
        if database is None:
            database = chromadb.DEFAULT_DATABASE
        if collection_name is None:
            collection_name = "default_collection"

        # collection name must be between 3-64 characters
        self._verify_collection_name(collection_name)

        self.embedding_function = embedding_function
        self.collection_metadata = collection_metadata

        try:
            self.db_client = chromadb.PersistentClient(path=storage_path, tenant=tenant_id, database=database)
            self.collection = self.db_client.create_collection(collection_name,
                                                               embedding_function=self.embedding_function,
                                                               metadata=collection_metadata)
        except Exception as e:
            raise ValueError(f"Error initializing Chroma database: {e}")

    def store(self, data: str, collection=None):
        if collection is None:
            collection = self.collection
        collection.add(documents=[data], ids=[f'id_{self.count()}'])

    def retrieve(self, query):
        pass

    def delete(self, query):
        pass

    def update(self, query, data):
        pass

    def list(self, query):
        pass

    def count(self):
        return self.collection.count()

    def create_collection(self, collection):
        pass

    def drop_collection(self, collection):
        pass

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
        pass

    def close(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _verify_collection_name(self, collection_name):
        if len(collection_name) < 3 or len(collection_name) > 64:
            raise ValueError("Collection name must be between 3-64 characters.")
