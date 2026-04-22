import re

def clean_text(text):
    # convert to lowercase
    text = text.lower()
    
    # remove special characters
    text = re.sub(r'[^a-zA-Z ]', '', text)
    
    return text
