# 📄 PDF Chat Bot (Document Q&A)

A simple Streamlit app that lets you **upload a PDF and ask questions about it**. It uses Google Gemini and LangChain (Retrieval-Augmented Generation) to find the relevant parts of the document and answer from them.

🔗 **Live demo:** https://pdf-chat-bot-4c24mwjs7gjstdcokjdappq.streamlit.app

---

## ✨ Features

- Upload any PDF (up to 200 MB)
- Ask questions in natural language
- Answers are based on the content of your document
- Runs in the browser, no database needed

## 🛠️ Tech Stack

| Part | Tool |
|------|------|
| UI | Streamlit |
| LLM | Google Gemini (`gemini-2.5-flash`) |
| Embeddings | `gemini-embedding-001` |
| Framework | LangChain |
| PDF loading | pypdf |
| Vector store | LangChain `InMemoryVectorStore` |
| Config | python-dotenv |

## ⚙️ How It Works

1. The PDF is uploaded and read page by page (`pypdf`).
2. The text is split into small chunks (`langchain-text-splitters`).
3. Each chunk is converted into an embedding and stored in memory.
4. When you ask a question, the most relevant chunks are retrieved.
5. Gemini reads those chunks and generates the answer.

## 📁 Project Structure

```
PDF-CHAT-BOT/
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── .gitignore          # Keeps .env and other private files out of Git
```

> **Note:** the file must be named `requirements.txt` in **lowercase**. Streamlit Cloud runs on Linux and will not find `Requirements.txt`.

## 🚀 Run Locally

**1. Clone the repo**

```bash
git clone https://github.com/sjha-dev/PDF-CHAT-BOT.git
cd PDF-CHAT-BOT
```

**2. Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac / Linux
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Add your Gemini API key**

Get a free key from [Google AI Studio](https://aistudio.google.com/apikey), then create a `.env` file in the project folder:

```
GOOGLE_API_KEY=your_api_key_here
```

**5. Start the app**

```bash
streamlit run app.py
```

## ☁️ Deploy on Streamlit Cloud

1. Push the code to GitHub (never push your `.env` file).
2. Go to [share.streamlit.io](https://share.streamlit.io) and create a new app from this repo (`main` branch, `app.py`).
3. Open **Manage app → Settings → Secrets** and add:

   ```toml
   GOOGLE_API_KEY = "your_api_key_here"
   ```

4. Save and reboot the app.

## 🐞 Common Errors and Fixes

| Error | Fix |
|-------|-----|
| `No module named 'dotenv'` | Add `python-dotenv` (not `dotenv`) to `requirements.txt` and make sure the file is named `requirements.txt` |
| `API key required for Gemini Developer API` | Add `GOOGLE_API_KEY` in Streamlit Secrets (or `.env` locally) |
| `404 NOT_FOUND ... gemini-embedding-2-preview` | Use `GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")` |

## 🔐 Security

- Never commit your API key or `.env` file.
- Keep `.env` listed in `.gitignore`.
- If a key is ever exposed, delete it and generate a new one.

## 👤 Author

**Sudhanshu Shekhar Jha**
IT-A, Bhagwan Parshuram Institute of Technology (BPIT), New Delhi
GitHub: [@sjha-dev](https://github.com/sjha-dev)


