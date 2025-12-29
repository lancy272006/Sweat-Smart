from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# -------------------------------
# STEP 1: CREATE / LOAD VECTOR DB
# -------------------------------

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

if not os.path.exists("faiss_index"):
    print("🔹 Creating nutrition embeddings...")

    loader = TextLoader("nutrition_data.txt")
    documents = loader.load()

    # Simple Python splitter as replacement for CharacterTextSplitter
    def simple_splitter(text, chunk_size=200, overlap=20):
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start = end - overlap
        return chunks

    docs = []
    for doc in documents:
        chunks = simple_splitter(doc.page_content)
        for chunk in chunks:
            docs.append(doc.__class__(page_content=chunk, metadata=doc.metadata))

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index")

    print("✅ Nutrition data embedded and saved\n")
else:
    print("✅ Loading existing nutrition embeddings\n")
    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

# -------------------------------
# STEP 2: CONNECT TO GEMMA
# -------------------------------

llm = ChatOpenAI(
    base_url="http://192.168.27.162:1234/v1",
    api_key="lm-studio",
    model="gemma-2b-it"
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    chain_type="stuff"
)

# -------------------------------
# STEP 3: CHAT LOOP
# -------------------------------

print("🏋️ Gym Nutrition Chatbot Ready")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Stay healthy 💪")
        break

    response = qa_chain.run(user_input)
    print("Bot:", response)
