from typing import List, Tuple, Dict, Any
import numpy as np

from core.embeddings import EmbeddingEngine

class VectorStore:
    def __init__(self):
        self.embedding_engine = EmbeddingEngine()
        self.records: List[Dict[str, Any]] = []

    def add(self, id: str, text: str, metadata: Dict[str, Any] | None = None):
        vector = self.embedding_engine.embed(text)
        
        record = {
            "id": id,
            "text": text,
            "vector": vector,
            "metadata": metadata or {}
        }

        self.records.append(record)

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        query_vector = self.embedding_engine.embed(query)
        
        scored_results = []
        
        for record in self.records:
            score = self.embedding_engine.cosine_similarity(
                query_vector, 
                record["vector"]
            )

            scored_results.append({
                "id": record["id"],
                "text": record["text"],
                "metadata": record["metadata"],
                "score": score
            })

        #Sort by similarity score(highest first)
    
        scored_results.sort(key=lambda x:x["score"],reverse=True)

        return scored_results[:top_k]


