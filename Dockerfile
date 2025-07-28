FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install pymupdf

RUN mkdir -p /app/output

CMD ["python", "process_pdfs.py"]