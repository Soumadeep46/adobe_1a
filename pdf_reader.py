import fitz  # PyMuPDF

def extract_spans(pdf_path):
    doc = fitz.open(pdf_path)
    spans = []
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    spans.append({
                        "text": span["text"].strip(),
                        "size": round(span["size"], 2),
                        "font": span["font"],
                        "page": page_num,
                        "flags": span["flags"]
                    })
    return spans