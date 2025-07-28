def extract_title(spans):
    first_page_spans = [s for s in spans if s["page"] == 0 and len(s["text"].strip()) > 5]
    if not first_page_spans:
        return "Untitled Document"

    max_size = max(s["size"] for s in first_page_spans)
    candidates = [s["text"] for s in first_page_spans if abs(s["size"] - max_size) < 0.5]

    seen = set()
    title_parts = []
    for text in candidates:
        clean_text = text.strip()
        if clean_text not in seen:
            seen.add(clean_text)
            title_parts.append(clean_text)

    return " ".join(title_parts).strip()