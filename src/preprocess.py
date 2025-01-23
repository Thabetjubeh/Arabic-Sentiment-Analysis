import re
import nltk
from nltk.corpus import stopwords

# Ensure necessary NLTK resources are downloaded
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

class ArabicTextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('arabic'))

    def remove_diacritics(self, text):
        """Removes Arabic diacritics from the text."""
        pattern = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
        return re.sub(pattern, '', text)

    def normalize_text(self, text):
        """Normalizes Arabic text by standardizing common variations."""
        text = re.sub(r'[إأآا]', 'ا', text)
        text = re.sub(r'ى', 'ي', text)
        text = re.sub(r'ؤ', 'و', text)
        text = re.sub(r'ئ', 'ي', text)
        text = re.sub(r'ة', 'ه', text)
        return text

    def tokenize(self, text):
        """Tokenizes the text into words."""
        return nltk.word_tokenize(text)

    def remove_stopwords(self, tokens):
        """Removes Arabic stopwords from a list of tokens."""
        return [word for word in tokens if word not in self.stop_words]

    def preprocess(self, text):
        """Applies the complete preprocessing pipeline to the input text."""
        text = self.remove_diacritics(text)
        text = self.normalize_text(text)
        tokens = self.tokenize(text)
        tokens = self.remove_stopwords(tokens)
        return ' '.join(tokens)

if __name__ == "__main__":
    # Example usage
    sample_text = "إِنَّ اللَّهَ يُحِبُّ الْمُتَوَكِّلِينَ"
    preprocessor = ArabicTextPreprocessor()
    processed_text = preprocessor.preprocess(sample_text)
    print("Original Text:", sample_text)
    print("Processed Text:", processed_text)
