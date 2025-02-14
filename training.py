import torch
from torch.utils.data import DataLoader

from dataset import TextDataset

def create_dataloader(texts, labels, tokenizer, batch_size=16):
    """Create DataLoader for training."""
    dataset = TextDataset(texts, labels, tokenizer)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)

def fine_tune_model(model, dataloader, epochs=3, learning_rate=5e-5):
    """Fine-tune the transformer model on the dataset."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
    loss_fn = torch.nn.CrossEntropyLoss()

    model.train()
    for epoch in range(epochs):
        for batch in dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            optimizer.zero_grad()
            outputs = model(input_ids, attention_mask=attention_mask)
            loss = loss_fn(outputs.logits, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch + 1}, Loss: {loss.item()}")