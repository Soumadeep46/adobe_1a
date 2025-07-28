from utils.font_utils import cluster_font_sizes
from utils.page_utils import normalize_page

def classify_headings(spans):
    spans = [s for s in spans if s["text"].strip()]
    size_to_level = cluster_font_sizes(spans)
    outline = []
    seen = set()

    for span in spans:
        level = size_to_level.get(span["size"])
        if not level:
            continue

        cleaned_text = span["text"].strip()
        if len(cleaned_text) < 3 and not cleaned_text.replace(".", "").isalnum():
            continue

        key = (cleaned_text.lower(), span["page"])
        if key in seen:
            continue
        seen.add(key)

        outline.append({
            "level": level,
            "text": cleaned_text,
            "page": normalize_page(span["page"])
        })
    return outline