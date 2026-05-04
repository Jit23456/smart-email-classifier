import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

def summarize_email(text, num_sentences=2):
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return text

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    words = [w for w in words if w not in stop_words and w not in string.punctuation]

    word_freq = Counter(words)

    # Score each sentence by sum of word frequencies
    scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                scores[sentence] = scores.get(sentence, 0) + word_freq[word]

    top_sentences = sorted(scores, key=scores.get, reverse=True)[:num_sentences]
    # Return in original order
    summary = [s for s in sentences if s in top_sentences]
    return " ".join(summary)
