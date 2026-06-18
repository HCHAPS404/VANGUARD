import os
import chromadb
from chromadb.utils import embedding_functions

class ChromaManager:
    """
    Manages connections and operations with ChromaDB vector store.
    """
    def __init__(self, persist_dir: str = None, collection_name: str = "vanguard_docs"):
        self.persist_dir = persist_dir or os.getenv("CHROMA_PERSIST_DIR", "./data/chroma")
        
        # If persist_dir is ":memory:", we use EphemeralClient (for tests)
        if self.persist_dir == ":memory:":
            self.client = chromadb.EphemeralClient()
        else:
            os.makedirs(self.persist_dir, exist_ok=True)
            self.client = chromadb.PersistentClient(path=self.persist_dir)
            
        self.collection_name = collection_name
        self.ef = embedding_functions.DefaultEmbeddingFunction()
        
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=self.ef
        )
        
    def add_chunks(self, document_id: str, chunks: list[str]):
        """Embeds and stores document chunks in ChromaDB."""
        if not chunks:
            return
            
        ids = [f"{document_id}_chunk_{i}" for i in range(len(chunks))]
        metadatas = [{"document_id": document_id, "chunk_index": i} for i in range(len(chunks))]
        self.collection.add(
            documents=chunks,
            ids=ids,
            metadatas=metadatas
        )
        
    def query(self, query_text: str, n_results: int = 3) -> list[str]:
        """Queries the vector database for the most similar chunks."""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        if not results["documents"]:
            return []
        return results["documents"][0]
