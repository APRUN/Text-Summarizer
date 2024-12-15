import numpy as np
import pandas as pd
import re

def extractive_summary(text, num_sentences=3):
    try:
        
        sentences = text.split('. ')  
        words = re.findall(r'\w+', text.lower())  
        
        
        stopwords = set([
            "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself",
            "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", 
            "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", 
            "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", 
            "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", 
            "with", "about", "against", "between", "into", "through", "during", "before", "after", 
            "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", 
            "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", 
            "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", 
            "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", 
            "should", "now"
        ])
        
        
        filtered_words = [word for word in words if word not in stopwords]
        
        
        word_frequencies = pd.Series(filtered_words).value_counts()
        max_frequency = word_frequencies.max()
        
        
        word_frequencies = word_frequencies / max_frequency
        
        
        sentence_scores = {}
        for sentence in sentences:
            sentence_words = re.findall(r'\w+', sentence.lower())
            score = sum(word_frequencies.get(word, 0) for word in sentence_words)
            sentence_scores[sentence] = score
        
        
        ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
        
        
        summary = ' '.join(ranked_sentences[:num_sentences])
        
        return summary

    except Exception as e:
        return f"An error occurred: {e}"


# input_text = """
# Quaid-e-Azam Muhammad Ali Jinnah (1876-1948) was a prominent figure in the founding of Pakistan and is considered the country's father: 
# Birth and early life Born in Karachi, Jinnah was educated at the Sindh Madrassat-ul-Islam and the Christian Mission School. He went to England to study law at Lincoln's Inn, becoming the youngest Indian to be called to the bar. 
# Political career. Jinnah began his political career in 1905 with the Indian National Congress. He joined the All India Muslim League in 1913 and became its leader in 1933. 
# Pakistan's founding. In 1940, the Muslim League adopted the Pakistan resolution at its annual session in Lahore, calling for a separate homeland for Muslims in India. Jinnah led the Muslims in their struggle for independence, and Pakistan was established on August 14, 1947. Jinnah became Pakistan's first Governor-General. 
# Legacy Jinnah is known as Quaid-e-Azam, which means "the great leader" in Urdu. He is also known as Baba-e-Qaum, which means "the father of the nation" in Urdu. His birth day is a national holiday in Pakistan. 
# """


# summary = extractive_summary(input_text, num_sentences=1)
# print(summary)
