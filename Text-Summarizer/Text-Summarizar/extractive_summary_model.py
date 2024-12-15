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


# Example input text
input_text = """
Quaid-e-Azam Muhammad Ali Jinnah (1876-1948) was a prominent figure in the founding of Pakistan and is considered the country's father: 
Birth and early life Born in Karachi, Jinnah was educated at the Sindh Madrassat-ul-Islam and the Christian Mission School. He went to England to study law at Lincoln's Inn, becoming the youngest Indian to be called to the bar. 
Political career Jinnah began his political career in 1905 with the Indian National Congress. He joined the All India Muslim League in 1913 and became its leader in 1933. 
Pakistan's founding In 1940, the Muslim League adopted the Pakistan resolution at its annual session in Lahore, calling for a separate homeland for Muslims in India. Jinnah led the Muslims in their struggle for independence, and Pakistan was established on August 14, 1947. Jinnah became Pakistan's first Governor-General. 
Legacy Jinnah is known as Quaid-e-Azam, which means "the great leader" in Urdu. He is also known as Baba-e-Qaum, which means "the father of the nation" in Urdu. His birthday is a national holiday in Pakistan. 
"""

# Generate summary using the custom LSA implementation
summary = extractive_summary_lsa(input_text, num_sentences=3)
print("Summary:")
print(summary)
