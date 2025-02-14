from pathlib import Path
import requests

def setup_dataset(base_path: Path):
    """Download and set up a dataset of short stories and novels categorized into genres."""
    genres = {
        "fantasy_science_fiction": [
            "https://www.gutenberg.org/cache/epub/36/pg36.txt",     # War of the Worlds
            "https://www.gutenberg.org/cache/epub/5230/pg5230.txt", # The Machine Stops
            "https://www.gutenberg.org/ebooks/84.txt.utf-8",        # Frankenstein
            "https://www.gutenberg.org/cache/epub/1228/pg1228.txt",  # The Wonderful Wizard of Oz
            "https://www.gutenberg.org/cache/epub/43/pg43.txt",     # The Strange Case of Dr. Jekyll and Mr. Hyde
            "https://www.gutenberg.org/cache/epub/345/pg345.txt",   # Dracula
            "https://www.gutenberg.org/cache/epub/16/pg16.txt" # Peter Pan
        ],
        "detective_fiction": [
            "https://www.gutenberg.org/cache/epub/174/pg174.txt",   # The Mysterious Affair at Styles
            "https://www.gutenberg.org/cache/epub/2852/pg2852.txt", # The Hound of the Baskervilles
            "https://www.gutenberg.org/cache/epub/155/pg155.txt",   # The Moonstone
            "https://www.gutenberg.org/cache/epub/2148/pg2148.txt", # The Works of Edgar Allan Poe 
            "https://www.gutenberg.org/cache/epub/1661/pg1661.txt"  # The Adventures of Sherlock Holmes
        ],
        "romance": [
            "https://www.gutenberg.org/cache/epub/1212/pg1212.txt" # Pride and Prejudice
        ],
        "historical_fiction": [
            "https://www.gutenberg.org/cache/epub/4217/pg4217.txt", # A Tale of Two Cities
            "https://www.gutenberg.org/cache/epub/766/pg766.txt" # Ivanhoe
        ],
        "western": [
            "https://www.gutenberg.org/cache/epub/104/pg104.txt", # Riders of the Purple Sage
            "https://www.gutenberg.org/cache/epub/12344/pg12344.txt" # The Log of a Cowboy
        ]
    }
    
    base_path.mkdir(parents=True, exist_ok=True)
    
    for genre, urls in genres.items():
        genre_path = base_path / genre
        genre_path.mkdir(exist_ok=True)
        
        for idx, url in enumerate(urls):
            response = requests.get(url)
            if response.status_code == 200:
                file_path = genre_path / f"story_{idx+1}.txt"
                with file_path.open("w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f"Downloaded {url} into {file_path}")
            else:
                print(f"Failed to download {url}")

if __name__ == "__main__":
    setup_dataset(Path(__file__).parent / "data")