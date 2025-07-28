import os
import json

def write_json(title, outline, filename, output_dir):
    out = {
        "title": title.strip(),
        "outline": outline
    }
    with open(os.path.join(output_dir, filename.replace(".pdf", ".json")), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)