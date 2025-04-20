
# Text Analyzer - Step 1

# Ask the user to paste some text
text = input("Paste your text here:\n")

import string

# Remove punctuation
clean_text = text.translate(str.maketrans('', '', string.punctuation))

# Lowercase and split
words = clean_text.lower().split()
word_count = len(words)
char_count_with_spaces = len(text)
char_count_no_spaces = len(text.replace(" ", ""))
avg_word_length = sum(len(word) for word in words) / word_count

from collections import Counter

word_freq = Counter(words)
most_common = word_freq.most_common(1)[0]
reading_time_minutes = word_count / 200  # Assuming 200 wpm

import re

sentences = re.split(r'[.!?]', text)
sentence_count = len([s for s in sentences if s.strip() != ""])
unique_words = len(set(words))
vocab_richness = unique_words / word_count
print("\n--- Text Analysis ---")
print(f"Total words: {word_count}")
print(f"Total characters (with spaces): {char_count_with_spaces}")
print(f"Total characters (no spaces): {char_count_no_spaces}")
print(f"Average word length: {avg_word_length:.2f}")
print(f"Most common word: '{most_common[0]}' (used {most_common[1]} times)")
print(f"Estimated reading time: {reading_time_minutes:.2f} minutes")
print(f"Total sentences: {sentence_count}")
print(f"Vocabulary richness: {vocab_richness:.2f}")