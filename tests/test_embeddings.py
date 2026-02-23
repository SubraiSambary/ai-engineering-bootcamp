import numpy as np
import pytest
from core.embeddings import EmbeddingEngine

def test_embedding_returns_vector():
    engine = EmbeddingEngine()
    text = "Hello, world!"
    vec = engine.embed(text)

    assert isinstance(vec, np.ndarray)
    assert len(vec) > 0


def text_same_text_high_similarity():
    engine = EmbeddingEngine()
    text1 = "Hello, world!"
    text2 = "Hello, world!"
    
    vec1 = engine.embed(text1)
    vec2 = engine.embed(text2)

    similarity = engine.cosine_similarity(vec1, vec2)
    assert similarity > 0.90

def test_different_text_low_similarity():
    engine = EmbeddingEngine()
    text1 = "Hello, world!"
    text2 = "The cat is on the roof."
    
    vec1 = engine.embed(text1)
    vec2 = engine.embed(text2)

    similarity = engine.cosine_similarity(vec1, vec2)
    assert similarity < 0.9

def test_invalid_input():
    engine = EmbeddingEngine()
    with pytest.raises(ValueError):
        engine.embed("")  # Empty string input should raise an error
    