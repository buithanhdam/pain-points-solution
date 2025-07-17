import json

def load_kb(path="solutions.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
if __name__ == "__main__":
    kb = load_kb()
    print(kb)