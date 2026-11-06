
from sentence_transformers import SentenceTransformer
import numpy as np
from transformers import pipeline


# Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load the language model
generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)


def create_embeddings(chunks):
    """Convert document chunks into numerical vectors."""
    return embedding_model.encode(
        chunks,
        convert_to_numpy=True,
        normalize_embeddings=True
    )


def retrieve_chunks(question, chunks, embeddings, top_k=3):
    """Find the most relevant chunks for a question."""

    question_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True,
        normalize_embeddings=True
    )[0]

    scores = np.dot(embeddings, question_embedding)
    best_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for index in best_indices:
        results.append({
            "text": chunks[index]["text"],
            "source": chunks[index]["source"],
            "score": float(scores[index])
        })

    return results


def generate_answer(question, retrieved_chunks):
    """Generate an answer using retrieved document content."""

    context = "\n\n".join(
        item["text"] for item in retrieved_chunks
    )

    prompt = f"""Answer the question using only the context below.
If the answer is not available, say you could not find it in the documents.

Context:
{context}

Question: {question}

Answer:"""

    response = generator(
        prompt,
        max_new_tokens=150,
        do_sample=False
    )

    return response[0]["generated_text"][len(prompt):].strip()
