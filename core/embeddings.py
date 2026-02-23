import numpy as np
from sentence_transformers import SentenceTransformer

class EmbeddingEngine:
    def __init__(self, model="all-MiniLM-L6-v2",):
        self.model = SentenceTransformer(model)

    def embed(self, text: str) -> np.ndarray:
        if not text or not isinstance(text, str):
            raise ValueError("Input text must be a non-empty string.")

        vector = self.model.encode(text)
        return np.array(vector)
    
    @staticmethod
    def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
        if vec1.shape != vec2.shape:
            raise ValueError("Vectors must be of the same shape for cosine similarity.")
        
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)

        if norm_vec1 == 0 or norm_vec2 == 0:
            return 0.0
        
        return float(np.dot(vec1, vec2) / (norm_vec1 * norm_vec2))