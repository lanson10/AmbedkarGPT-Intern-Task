# AmbedkarGPT 

This project is a simple **local RAG (Retrieval Augmented Generation)** Q&A system built using:

- **Python 3**
- **LangChain**
- **ChromaDB (local vector database)**
- **HuggingFace MiniLM Embeddings**
- **Ollama + Mistral 7B (local LLM, no API keys needed)**

The system loads a short speech by Dr. B.R. Ambedkar, embeds it into a vector store, retrieves relevant text, and answers user questions **based only on the provided document**.

.

---

## ✔ Features

- Local embeddings using **all-MiniLM-L6-v2**
- Local vector store using **ChromaDB**
- Local LLM using **Ollama Mistral**
- 100% offline, no API keys required
- Clean, simple command-line question answering
- Fully reproducible environment

---

## 📦 Folder Structure
AmbedkarGPT-Intern-Task/
│
├── main.py
├── speech.txt
├── requirements.txt
├── README.md
└── .gitignore


---

## 🔧 Installation & Setup

### 1. Install Python 3.10+
Make sure Python is installed and available on your system.

---

### 2. Install Ollama
Ollama runs the local Mistral 7B model.

Download from:
https://ollama.com/download

Then pull Mistral:
ollama pull mistral


---

### 3. Clone This Repository



git clone https://github.com/
lanson10/AmbedkarGPT-Intern-Task

cd AmbedkarGPT-Intern-Task


---

### 4. Create & Activate Virtual Environment

#### Windows (PowerShell)


python -m venv venv
.\venv\Scripts\Activate.ps1


#### Linux / macOS


python3 -m venv venv
source venv/bin/activate


---

### 5. Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt


---

## ▶ Run the Application



python main.py


You will see:


--- AmbedkarGPT Q&A System ---
Loaded speech.txt
Split into X chunks.
Vector store created and saved.
RAG pipeline ready.


Now type any question, for example:



What is the real remedy for caste?


Type `exit` to close the program.

---

## 📁 Provided Document

The system uses the following provided text (excerpt from *Annihilation of Caste*) stored in **speech.txt**.  
All answers strictly come from this document.

---

## ✔ Technologies Used

- **LangChain** – Text loader, text splitter, retriever, pipeline
- **ChromaDB** – Local vector store for embeddings
- **HuggingFace Transformers** – MiniLM embeddings (FREE)
- **Ollama** – Local LLM runtime
- **Mistral 7B** – LLM for answer generation
- **Python** – Entire pipeline and CLI interface

---

## 🚀 Goal of the Assignment

This project demonstrates:

- Understanding of RAG architecture  
- Ability to build a functional prototype  
- Ability to work with embeddings, vector stores, and LLMs  
- Clean code and environment setup  
- Ability to document projects clearly  

---

## 📞 Contact

For any issues, feel free to open an issue in the repository.

---


