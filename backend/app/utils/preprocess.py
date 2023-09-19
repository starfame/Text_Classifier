import re

import tensorflow as tf
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.layers import TextVectorization


class TextPreprocessor:
    def __init__(self, max_words, max_length, vectorizer_path=None):
        self.stopwords_set = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        if vectorizer_path:
            self.vectorizer = tf.saved_model.load(vectorizer_path)
        else:
            self.vectorizer = TextVectorization(max_tokens=max_words,
                                                standardize=None,
                                                output_sequence_length=max_length)

    def preprocess_text(self, texts: list[str]) -> list[str]:
        preprocessed_texts = []
        for text in texts:
            text = text.lower()
            text = re.sub('[^a-z\s]', '', text)
            words = text.split()
            words = [self.lemmatizer.lemmatize(word) for word in words if word not in self.stopwords_set]
            words = ' '.join(words)
            preprocessed_texts.append(words)
        return preprocessed_texts

    def adapt_vectorizer(self, data):
        self.vectorizer.adapt(data)

    def vectorize_text(self, text):
        if isinstance(self.vectorizer, TextVectorization):
            return self.vectorizer.call(tf.constant(text))
        else:
            serving_fn = self.vectorizer.signatures["serving_default"]
            output = serving_fn(tf.constant(text))
            return output["outputs"]
