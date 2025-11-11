from romeo_and_juliet import PLAY
import string

def get_words(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

def words_frequency(words):
    freq_map = {}
    for word in words:
        if word in freq_map:
            freq_map[word] += 1
        else:
            freq_map[word] = 1
    return freq_map

def top_n_words(freq, n):
    for _ in range(n):
        most_common_word = max(freq, key=freq.get)
        print(f"{most_common_word}: {freq[most_common_word]}")
        del freq[most_common_word]

def main():
    words = get_words(PLAY)
    freq = words_frequency(words)
    print("Top 50 most frequent words:")
    top_n_words(freq, 50)

if __name__ == "__main__":
    main()

print(PLAY[:1000])
