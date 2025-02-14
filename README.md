# Transformer-Based Text Classification

This project implements a text classification pipeline using Transformer models. It downloads and organizes short stories and novels from different genres, preprocesses the text, fine-tunes a Transformer model for classification, and evaluates the model.

## Features
- Downloads short stories and novels from Project Gutenberg
- Organizes them into labeled genre folders (e.g., science fiction, fantasy, detective fiction, romance)
- Preprocesses text (lowercasing, cleaning, tokenization)
- Loads a pre-trained Transformer model dynamically
- Converts text into tensor format for training
- Fine-tunes the model using PyTorch
- Evaluates the model using accuracy, F1-score, precision, recall
- Generates and saves a confusion matrix

## Requirements

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Dataset Setup

To download the dataset, run:
```bash
python setup.py
```

This will create a `data/` directory with the following structure:

```
data/
│── science_fiction/
│   ├── story_1.txt  (War of the Worlds)
│   ├── story_2.txt  (The Machine Stops)
│── fantasy/
│   ├── story_1.txt  (The Wonderful Wizard of Oz)
│── detective_fiction/
│   ├── story_1.txt  (The Hound of the Baskervilles)
│── romance/
│   ├── story_1.txt  (Pride and Prejudice)
...
```

## Training the Model

To train the Transformer model on the dataset, run:
```bash
python data_processing.py --data_path ./data --model_name bert-base-uncased
```

### Additional Arguments
| Argument | Description |
|----------|-------------|
| `--data_path` | Path to the dataset folder (default: `./data/`) |
| `--model_name` | Name of the pre-trained Transformer model (e.g., `bert-base-uncased`) |
| `--batch_size` | Batch size for training (default: 16) |
| `--epochs` | Number of training epochs (default: 3) |
| `--learning_rate` | Learning rate for fine-tuning (default: 5e-5) |

## Model Evaluation
After training, evaluation metrics (accuracy, F1-score, precision, recall) are displayed, and a confusion matrix is saved as `confusion_matrix.png`.

## License
This project is open-source and available for modification and distribution.
