from app.vector_store import load_vector_store
from app.llm import GroqLLM

# Initialize once (important for performance)
llm = GroqLLM()


def get_answer(query):
    try:
        db = load_vector_store()

        # 🔥 Retrieve top relevant chunks
        docs = db.similarity_search(query, k=3)

        # ❌ No context found
        if not docs:
            return "I don't know based on the provided medical document.", []

        # 📄 Build context safely
        context = "\n\n".join(
            [doc.page_content for doc in docs if doc.page_content]
        )

        # 🧠 Improved RAG prompt (more strict + structured)
        prompt = f"""
You are an expert medical AI assistant.

RULES:
- Answer ONLY using the given context
- Do NOT use outside knowledge
- If answer is not in context, say exactly: "I don't know based on the provided document"
- Be clear, simple, and medically accurate
- Do not hallucinate

Context:
{context}

Question:
{query}

Answer in short paragraph:
"""

        # 🤖 Generate response
        answer = llm.generate(prompt)

        return answer.strip(), docs

    except Exception as e:
        return f"Error: {str(e)}", []