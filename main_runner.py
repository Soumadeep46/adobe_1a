from pdf_reader import extract_spans
from title_extractor import extract_title
from heading_classifier import classify_headings
from json_writer import write_json
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if not filename.lower().endswith(".pdf"):
        continue

    pdf_path = os.path.join(INPUT_DIR, filename)
    spans = extract_spans(pdf_path)
    title = extract_title(spans)
    outline = classify_headings(spans)
    write_json(title, outline, filename, OUTPUT_DIR)