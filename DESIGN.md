# Pain Point Design Document

## 1. Agent Input Design

### 1.1. Required Information

- **Pain Point Description**: A clear, natural-language statement of the business pain point (e.g., "Our support agents are overwhelmed by the high volume of repetitive questions").
- **Optional Context** (for future enhancements):

  - Channel (e.g., web, mobile, email, call): Identify where the pain point occurs
  - Industry (e.g., ecommerce, banking, etc.): Provide industry-relevant solutions

### 1.2. Input Format (JSON)

```json
{
  "pain_point": "Our support agents are overwhelmed by the high volume of repetitive questions.",
  "context": {
    "channel": "email",
    "industry": "ecommerce"
  }
}
```

**Rationale**:

- Structured JSON format makes it extensible for future context-aware reasoning.
- Enables easy integration with APIs or frontend systems.

---

## 2. Agent Output Design

### 2.1. Output Structure

Each solution recommendation should contain:

- `name`: Name of the proposed solution
- `description`: Brief summary of how it addresses the pain point
- `categories`: High-level product grouping
- `link`: URL to learn more
- `relevance_score`: Numeric score indicating match strength (0–1)

### 2.2. Output Format (JSON)

```json
[
  {
    "name": "AI Agent for FAQ & First Response",
    "description": "AI agents handle repetitive and common queries instantly, allowing human agents to focus on complex tasks.",
    "categories": ["AI Customer Service"],
    "link": "https://filum.ai/products/customer-service-ai",
    "relevance_score": 0.95
  }
]
```

**Rationale**:

- Easy for UI rendering or downstream automation
- Ranked by score for prioritization

---

## 3. Feature Knowledge Base Structure

### 3.1. Schema Design

Each feature in `solutions.json` should have the following structure:

```json
{
  "id": "string", // Unique identifier
  "name": "string",
  "description": "string",
  "categories": ["string"], // Broad solution areas
  "modules": ["string"],
  "keywords": ["string"], // Search terms for basic matching
  "pain_points": ["string"], //Pre-defined problem statements
  "benefits": ["string"],
  "use_cases": ["string"], // Implementation scenarios
  "link": "string",
  "priority": "high | medium | low"
}
```

### 3.2. Example Entry

```json
{
  "id": "voc_surveys_post_purchase",
  "name": "Automated Post-Purchase Surveys",
  "description": "Trigger surveys automatically via email, SMS, Zalo, QR, POS, or web after a transaction to collect timely customer feedback.",
  "categories": ["Voice of Customer (VoC)"],
  "modules": ["Surveys"],
  "keywords": ["feedback collection", "post purchase", "survey"],
  "pain_points": [
    "We're struggling to collect customer feedback consistently after a purchase"
  ],
  "benefits": ["Automatically trigger surveys after transactions"],
  "use_cases": ["E-commerce post-purchase feedback"],
  "link": "https://filum.ai/products/voice-of-customer/survey",
  "priority": "high"
}
```

**Rationale**:

- Enables effective keyword matching and future expansion with NLP.
- Supports multi-category/module association for broader coverage.

---

## 4. Agent Core Logic & Matching Approach

### 4.1. Step-by-Step Workflow

1. **Input Ingestion**: Receive `pain_point` as JSON.
2. **Preprocessing**: Lowercase, remove punctuation, tokenize text.
3. **Matching Strategy**:

   - Match against `keywords` and `pain_points` fields in knowledge base.
   - Optionally use fuzzy matching , cosine or semantic similarity (e.g., sentence embeddings).

4. **Scoring**:

   - Compute a simple score (e.g., number of keyword matches / total keywords).
   - Normalize to range \[0, 1].

5. **Ranking and Filtering**:

   - Filter by a threshold (e.g., relevance_score > 0.6).
   - Sort descending by score.

6. **Return Output**: Format and deliver structured solution list.

### 4.2. Matching Example

- **Input**:

```
{
  "pain_point": "Our support agents are overwhelmed by the high volume of repetitive questions.",
  "context": {
  "channel": "email",
  "industry": "ecommerce"
  }
}
```

- **Matched Solution**:

```
{
  "name": "AI Agent for FAQ & First Response",
  "description": "AI agents handle repetitive and common queries instantly, allowing human agents to focus on complex tasks.",
  "categories": [
  "AI Customer Service"
  ],
  "link": "https://filum.ai/products/customer-service-ai/contact-center",
  "relevance_score": 0.99
}
```

- **Why**: Keywords "AI", "repetitive", "FAQ", "first response" match.

---

## 5. Optional: Prototype Implementation

### 5.1. Directory Structure

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

### 5.2. Tools

- Python (basic NLP with fuzzy search, scikit-learn, transformers)
- JSON-based storage

### 5.3. Example Run

- Input: sample Json pain point
- Output: list of relevant Filum.ai features with scores
