# Word frequency counter
from collections import Counter

with open('sample_text.txt', 'r') as file:
    words = file.read().lower().split()
    word_counts = Counter(words)

print(word_counts.most_common(5))
