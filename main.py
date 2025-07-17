import argparse
import json
from src.kb_loader import load_kb
from src.matching.tfidf_cosine_similarity import match_tfidf_cosine
from src.matching.semantic_embed import match_semantic
from src.matching.fuzzy_search import match_fuzzy
from src.utils import preprocess

def main():
    parser = argparse.ArgumentParser(description="Pain Point to Solution Agent")
    parser.add_argument('--method', type=str, choices=['tfidf', 'semantic', 'fuzzy'], default='tfidf', help='Choose matching method')
    parser.add_argument('--input', type=str, required=True, help='Path to input JSON file')
    parser.add_argument('--topn', type=int, default=3, help='Show top N results')
    args = parser.parse_args()

    kb = load_kb()
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            input_json = json.load(f)
        pain_point = preprocess(input_json["pain_point"])

        if args.method == "tfidf":
            results = match_tfidf_cosine(pain_point, kb, topn=args.topn)
        elif args.method == "semantic":
            results = match_semantic(pain_point, kb, topn=args.topn)
        elif args.method == "fuzzy":
            results = match_fuzzy(pain_point, kb, topn=args.topn)
        else:
            raise ValueError("Invalid method")
        print(json.dumps(results, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()