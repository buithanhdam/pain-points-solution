from sentence_transformers import SentenceTransformer, util
from src.utils import preprocess
def build_semantic_corpus(kb):
    # Ghép keywords + pain_points cho mỗi feature để nhúng
    texts = []
    for feature in kb:
        text = " ".join(feature.get("keywords", [])) + ". " + " ".join(feature.get("pain_points", []))
        texts.append(text)
    return texts

def match_semantic(pain_point, kb, topn=3, threshold=0.4):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    feature_texts = build_semantic_corpus(kb)
    # Encode
    emb_pain_point = model.encode(pain_point, convert_to_tensor=True)
    emb_features = model.encode(feature_texts, convert_to_tensor=True)
    # Cosine similarity
    sims = util.cos_sim(emb_pain_point, emb_features)[0]
    results = []
    for idx, score in enumerate(sims):
        score = float(score)
        if score >= threshold:
            feature = kb[idx]
            results.append({
                "name": feature["name"],
                "description": feature["description"],
                "categories": feature["categories"],
                "link": feature["link"],
                "relevance_score": round(score, 2)
            })
    results = sorted(results, key=lambda x: x["relevance_score"], reverse=True)
    return results[:topn]