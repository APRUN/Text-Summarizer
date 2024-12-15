import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer

def extractive_summary_lsa(text, num_sentences=3):
    try:
        # Split the text into sentences
        sentences = text.split('. ')
        
        # Preprocess the text: remove special characters, and tokenize
        clean_sentences = [re.sub(r'\W+', ' ', sentence.lower()) for sentence in sentences]
        
        # Create a term-document matrix
        vectorizer = CountVectorizer(stop_words='english')  # Custom stopwords can be added
        term_doc_matrix = vectorizer.fit_transform(clean_sentences).toarray()
        
        # Perform Singular Value Decomposition (SVD)
        u, s, vt = np.linalg.svd(term_doc_matrix, full_matrices=False)
        
        # Select top-ranked sentences based on their contributions to the largest singular values
        ranked_sentences = np.argsort(-u[:, 0])  # Sort by the contribution to the first topic
        
        # Generate summary by selecting the top `num_sentences` sentences
        summary_sentences = [sentences[i] for i in ranked_sentences[:num_sentences]]
        summary = ' '.join(summary_sentences)
        
        return summary

    except Exception as e:
        return f"An error occurred: {e}"

# Read the CSV file containing text data (assuming it's in 'input_data.csv')
csv_file_path = 'Text-Summarizar\\essays.csv'  # Replace with your actual CSV file path
df = pd.read_csv(csv_file_path)

# Assuming the CSV has a column 'text' that contains the text data to summarize
df['summary'] = df['text'].apply(lambda text: extractive_summary_lsa(text, num_sentences=3))
print("Sample Summaries:")
print("=================")
for i, row in df.head(5).iterrows():  # Print the first 5 summaries
    print(f"Summary for text {i+1}:")
    print(row['summary'])
    print("-" * 50)
# Save the summaries into a new CSV file
output_csv_path = 'summarized_output.csv'
df.to_csv(output_csv_path, index=False)

# Optionally, print out the resulting summaries
print("Summaries have been saved to:", output_csv_path)
