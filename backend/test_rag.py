from rag.retriever import retrieve_context

print("=" * 80)

context = retrieve_context(
    "How do I return my damaged laptop?",
    "returns"
)

print(context)

print("=" * 80)