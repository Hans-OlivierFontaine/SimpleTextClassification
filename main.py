import argparse

from data_processing import discover_folders_and_files, preprocess_text, read_text_file
from model import model_factory
from training import create_dataloader, fine_tune_model
from metrics import evaluate_model
from setup import setup_dataset

def main():
    parser = argparse.ArgumentParser(description="Text Classification with Transformers")
    parser.add_argument("--data_path", type=str, required=True, help="Path to the dataset folders")
    parser.add_argument("--model_name", type=str, required=True, help="Pre-trained transformer model name")
    parser.add_argument("--batch_size", type=int, default=16, help="Batch size for training")
    parser.add_argument("--epochs", type=int, default=3, help="Number of training epochs")
    parser.add_argument("--learning_rate", type=float, default=5e-5, help="Learning rate")
    parser.add_argument("--setup", action='store_true', help="Download and setup dataset")
    
    args = parser.parse_args()
    
    if args.setup:
        setup_dataset(args.data_path)
        return
    
    model, tokenizer = model_factory(args.model_name)
    data = discover_folders_and_files(args.data_path)
    texts, labels = [], []
    for label, files in data.items():
        for file in files:
            texts.append(preprocess_text(read_text_file(file)))
            labels.append(label)
    
    dataloader = create_dataloader(texts, labels, tokenizer, args.batch_size)
    fine_tune_model(model, dataloader, args.epochs, args.learning_rate)
    evaluate_model(model, dataloader)

if __name__ == "__main__":
    main()
