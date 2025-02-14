from pathlib import Path
import random
import re

def discover_folders_and_files(base_path):
    """Discover folders (labels) and their corresponding text files."""
    base_path = Path(base_path)
    data = {label.name: list(label.glob("*.txt")) for label in base_path.iterdir() if label.is_dir()}
    return data

def read_text_file(file_path):
    """Read the content of a text file."""
    with file_path.open('r', encoding='utf-8') as file:
        return file.read()

def preprocess_text(text):
    """Basic text preprocessing: lowercasing, removing special characters, extra spaces."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
