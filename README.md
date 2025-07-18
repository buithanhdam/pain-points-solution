# Pain Point to Solution Agent

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/buithanhdam/pain-points-solution.git
cd pain-points-solution
```

### 2. Set Up a Virtual Environment

#### 🔧 Unix/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🪟 Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the agent to match business pain points with relevant Filum.ai features.

### Matching Methods:

#### Fuzzy Matching:

```bash
python main.py --method fuzzy --input input_examples.json
```

#### TF-IDF + Cosine Similarity:

```bash
python main.py --method tfidf --input input_examples.json
```

#### Semantic Embeddings Matching (need to install `sentence-transformers` library in requirements.txt):

```bash
python main.py --method semantic --input input_examples.json
```

> 🔹 The [`input_examples.json`] file contains sample pain points for testing.
> 🔹 The [`output_examples.json`] file contains sample output for testing

---

## 🧠 Adding or Updating Solutions

To add or update Filum.ai features, edit the [`solutions.json`] file:

```json
{
  "feature_name": "AI Inbox",
  "category": "AI Customer Service - AI Inbox",
  "description": "A unified inbox where human and AI agents collaborate.",
  "pain_point_keywords": ["call center", "support", "agent", "chat", "calls", "email", "chatbot"],
  "example_use_cases": [
    "Reduce workload for support agents",
    "Increase customer response speed"
  ]
}
```

---

## 📁 Project Structure

```
pain-points-solution/
│
├── 📁 src/                         # Source code
│   ├── 📁 matching/                # Core matching logic modules
│   │   ├── **init**.py
│   │   ├── fuzzy_search.py        # Fuzzy keyword-based matching
│   │   ├── semantic_embed.py      # Embedding-based similarity (e.g., sentence-transformers)
│   │   ├── tfidf_cosine\_similarity.py  # TF-IDF + Cosine Similarity matching
│   ├── kb_loader.py           # Load knowledge base (features.json)
│   ├── utils.py               # Common utilities (text preprocessing, normalization, etc.)
│
├── 📁 venv/                        # Virtual environment (not committed)
│
├── .gitignore                     # Git ignore rules
├── categories.json                # Optional: categories/taxonomy for features (grouping, metadata)
├── input_examples.json            # Sample pain points for testing
├── solutions.json                 # Feature knowledge base (Filum.ai solutions)
├── main.py                        # Entry point script to run the agent
├── DESIGN.md                      # 💡 Design document (Input/Output/Matching/KB Design)
├── README.md                      # 📘 Instructions to set up and run the prototype
├── requirements.txt               # Python dependencies (e.g., sentence-transformers, scikit-learn)
├── LICENSE                        # Project license
```

---

## ✅ Requirements

* **Python Version**: 3.9+
* **Libraries**:
  - [`scikit-learn`]
  - [`sentence-transformers`]
  - [`fuzzywuzzy`], etc.

---

## 📝 License

This project is licensed under the MIT License.  