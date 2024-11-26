import tkinter as tk
from tkinter import scrolledtext
from extractive_summary_logic import extractive_summary


def generate_summary():
    input_text = input_text_area.get("1.0", tk.END)  
    summary = extractive_summary(input_text, num_sentences=3)  
    output_text_area.delete("1.0", tk.END)  
    output_text_area.insert(tk.END, summary)  


window = tk.Tk()
window.title("Extractive Summarizer")
window.geometry("800x600")


tk.Label(window, text="Enter Text:", font=("Arial", 14)).pack(pady=10)
input_text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=10, font=("Arial", 12))
input_text_area.pack(pady=10)


generate_button = tk.Button(window, text="Generate Summary", font=("Arial", 14), command=generate_summary)
generate_button.pack(pady=10)


tk.Label(window, text="Summary:", font=("Arial", 14)).pack(pady=10)
output_text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=10, font=("Arial", 12))
output_text_area.pack(pady=10)


window.mainloop()
