from core.vector_store import VectorStore
from core.retrieval_service import RetrievalService
from core.agent import SimpleAgent


def test_simple_agent():
    store = VectorStore()
    store.add("r1", "Built scalable AWS cloud infrastructure")
    store.add("r2", "Developed frontend applications using React")

    retrieval = RetrievalService(store)
    agent = SimpleAgent(retrieval)

    result = agent.run(
        "Looking for AWS cloud experience",
        top_k=1
    )

    assert result["query"] == "Looking for AWS cloud experience"
    assert result["retrieved_documents"][0]["id"] == "r1"
    assert "AWS" in result["context"]