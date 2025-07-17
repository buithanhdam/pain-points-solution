from fuzzywuzzy import fuzz

def build_fuzzy_corpus(kb):
    # Ghép keywords + pain_points thành 1 chuỗi để so khớp
    corpus = []
    for feature in kb:
        text = " ".join(feature.get("keywords", [])) + " " + " ".join(feature.get("pain_points", []))
        corpus.append(text)
    return corpus

def match_fuzzy(pain_point, kb, topn=3, threshold=60):
    corpus = build_fuzzy_corpus(kb)
    results = []
    for idx, text in enumerate(corpus):
        # Sử dụng fuzzywuzzy partial_ratio để so sánh
        score = fuzz.partial_ratio(pain_point.lower(), text.lower())
        if score >= threshold:
            feature = kb[idx]
            results.append({
                "name": feature["name"],
                "description": feature["description"],
                "categories": feature["categories"],
                "link": feature["link"],
                "relevance_score": round(score / 100, 2)
            })
    results = sorted(results, key=lambda x: x["relevance_score"], reverse=True)
    return results[:topn]