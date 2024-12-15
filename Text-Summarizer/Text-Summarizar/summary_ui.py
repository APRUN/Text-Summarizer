import streamlit as st
import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer

# Extractive summary using Latent Semantic Analysis (LSA)
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

# Streamlit UI
st.title('Text Summarization with LSA')

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Show the first few rows of the uploaded CSV
    st.subheader("Uploaded CSV Preview:")
    st.write(df.head())

    # Check if 'text' column exists
    if 'text' in df.columns:
        # Summarize the text
        st.subheader("Summarized Texts")
        df['summary'] = df['text'].apply(lambda text: extractive_summary_lsa(text, num_sentences=3))

        # Display summaries
        for i, row in df.head(5).iterrows():  # Show summaries of the first 5 texts
            st.write(f"**Summary for text {i+1}:**")
            st.write(row['summary'])
            st.write("-" * 50)

        # Download summarized CSV
        st.subheader("Download Summarized CSV")
        output_csv = df.to_csv(index=False)
        st.download_button(
            label="Download Summarized File",
            data=output_csv,
            file_name="summarized_output.csv",
            mime="text/csv"
        )
    else:
        st.error("The CSV file must contain a column named 'text'.")

