# PDF Outline Extractor — Round 1A (Adobe India Hackathon 2025)

Extract the **Title** and hierarchical **H1**, **H2**, **H3** headings from PDF files (≤ 50 pages), outputting clean JSON files for each.

---

## ✔️ Quick Start (Docker)

```bash
docker build --platform linux/amd64 -t pdf-outliner:latest .
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
```
### pdf-outliner:latest
### Place PDFs in input/.

Outputs matching JSON files in output/.

🧠 How It Works
Title: Largest, sufficiently long text on page 0 (font-size heuristic).

Headings:

H1: font-size ≥ 16

H2: font-size ≥ 13.5

H3: font-size ≥ 11.5

Duplicate Cleanup: Removes identical consecutive headings.

Invalid PDF Handling: Skips corrupt/empty files gracefully.

📦 JSON Output Format
Each .json file follows:

```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Heading 1 ", "page": 0 },
    { "level": "H2", "text": "Subheading 1.1 ", "page": 1 },
    { "level": "H3", "text": "Sub‑section 1.1.1 ", "page": 2 }
  ]
}
```
page: 0-indexed

text: includes trailing space for consistency

Title may be "" if no valid candidate found

⚡ Features & Compliance
Processes 50‑page PDFs in ≤ 10s on AMD64 CPU

Compatible with offline use (no internet)

Total size under 200 MB (no large ML models)

Modular, testable, and easy to integrate

🛠️ Local Development (Optional)
``` bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main_runner.py
```
Make sure input/ and output/ directories are present.

Need unit tests, multilingual support, or integration into Round 1B persona-driven pipelines? Just let me know!

``` yaml

---

This concise `README.md` includes all critical details:
- Purpose & output schema
- Usage steps (Docker + optional local)
- Key algorithm behavior
- Constraint compliance summary

Let me know if you'd like to **add badges**, **contributing guidelines**, or **license** info!
::contentReference[oaicite:0]{index=0}
```
