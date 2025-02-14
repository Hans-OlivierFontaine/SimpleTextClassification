from transformers import AutoModelForSequenceClassification, AutoTokenizer

def model_factory(model_name):
    """Factory function to load a pre-trained transformer model and tokenizer based on the model name."""
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer