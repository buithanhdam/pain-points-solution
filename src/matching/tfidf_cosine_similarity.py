from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils import preprocess
def build_corpus(kb):
    # Kết hợp keywords + pain_points cho mỗi feature thành 1 chuỗi
    corpus = []
    for feature in kb:
        text = " ".join(feature.get("keywords", [])) + " " + " ".join(feature.get("pain_points", []))
        corpus.append(text)
    return corpus

def match_tfidf_cosine(pain_point, kb, topn=3, threshold=0.3):
    corpus = build_corpus(kb)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([pain_point] + corpus)
    sims = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    results = []
    for idx, score in enumerate(sims):
        if score >= threshold:
            feature = kb[idx]
            results.append({
                "name": feature["name"],
                "description": feature["description"],
                "categories": feature["categories"],
                "link": feature["link"],
                "relevance_score": round(float(score), 2)
            })
    # Sắp xếp theo score giảm dần
    results = sorted(results, key=lambda x: x["relevance_score"], reverse=True)
    return results[:topn]