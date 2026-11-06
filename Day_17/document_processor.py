
from pathlib import Path
from pypdf import PdfReader


def extract_text(file_path):
    """Extract text from a PDF or TXT document."""

    file_path = Path(file_path)
    extension = file_path.suffix.lower()

    if extension == ".pdf":
        reader = PdfReader(str(file_path))
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text

    elif extension == ".txt":
        return file_path.read_text(encoding="utf-8")

    else:
        raise ValueError("Unsupported file format. Use PDF or TXT.")


def split_into_chunks(text, chunk_size=500, overlap=50):
    """Split extracted text into smaller overlapping chunks."""

    if chunk_size <= overlap:
        raise ValueError("Chunk size must be greater than overlap.")

    chunks = []

    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks
