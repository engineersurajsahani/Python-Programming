# Count words and sentences in a file
def count_words_and_sentences(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = len(content.split())
        sentences = content.count('.') + content.count('!') + content.count('?')
    return words, sentences

filename = 'sample_text.txt'
word_count, sentence_count = count_words_and_sentences(filename)
print(f"Word count: {word_count}, Sentence count: {sentence_count}")
