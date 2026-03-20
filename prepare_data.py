from datasets import load_dataset
import random

# Load the dataset
print("Loading dataset...")
# Using a community maintained version that is accessible
dataset = load_dataset("ntcuong777/ubuntu_dialogue_corpus_train")
train_data = dataset['train']

print(f"Dataset loaded. Total rows: {len(train_data)}")
print(f"First row keys: {train_data[0].keys()}")

# Some versions of this dataset use 'Context' and 'Response'
# or they are already preprocessed into 'text'
# Let's try to find where the user query is.

queries = []
# Based on common schemas for this dataset:
# it might have 'Context' where the last part is the user query
# or just 'text'

for i in range(min(len(train_data), 100)):
    if len(queries) >= 20:
        break
    
    row = train_data[i]
    if 'text' in row:
        q = row['text'].split('\n')[0] # Take first line if multi-line
    elif 'Context' in row:
        q = row['Context'].split('__eou__')[0] # __eou__ is common end-of-utterance marker
    else:
        # Fallback to whatever string is there
        q = str(list(row.values())[0])

    if q and q not in queries:
        queries.append(q)

for idx, q in enumerate(queries):
    print(f"{idx+1}. {q}")
