import streamlit as st
from extractive_summary_logic import extractive_summary  # Import the summarizer function

# Streamlit UI
st.title("Extractive Summarizer")

# Input text area for user input
input_text = st.text_area("Enter Text", height=200)

# Button to generate summary
if st.button("Generate Summary"):
    if input_text:
        # Generate summary using the extractive_summary_lsa function
        summary = extractive_summary(input_text, num_sentences=3)
        
        # Display the summary
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
