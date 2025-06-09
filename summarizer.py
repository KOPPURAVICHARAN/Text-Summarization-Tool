
import spacy
from collections import Counter
from string import punctuation
import heapq

nlp = spacy.load("en_core_web_sm")

def summarize_text(text, num_sentences=5):
    doc = nlp(text)
    word_frequencies = {}
    stopwords = nlp.Defaults.stop_words
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            word_frequencies[word.text.lower()] = word_frequencies.get(word.text.lower(), 0) + 1
    if not word_frequencies:
        return ""
    max_freq = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] /= max_freq
    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word.text.lower()]
    summarized_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    final_summary = " ".join([sent.text for sent in summarized_sentences])
    return final_summary
