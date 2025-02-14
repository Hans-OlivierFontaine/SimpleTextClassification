from sklearn.model_selection import train_test_split

from dataset_preparation import discover_folders_and_files, read_text_file, preprocess_text


def prepare_dataset(base_path, test_size=0.2):
    """Prepare dataset by discovering files, reading them, preprocessing, and splitting into train/test."""
    data = discover_folders_and_files(base_path)
    texts, labels = [], []
    for label, files in data.items():
        for file in files:
            text = read_text_file(file)
            preprocessed_text = preprocess_text(text)
            texts.append(preprocessed_text)
            labels.append(label)
    return train_test_split(texts, labels, test_size=test_size, random_state=42)