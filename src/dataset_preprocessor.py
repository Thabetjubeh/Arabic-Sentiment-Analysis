import pandas as pd
from preprocess import ArabicTextPreprocessor

class DatasetPreprocessor:
    def __init__(self, input_file, output_file):
        """
        Initializes the dataset preprocessor.

        Args:
            input_file (str): Path to the raw dataset CSV.
            output_file (str): Path to save the cleaned dataset.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.text_preprocessor = ArabicTextPreprocessor()  # Use the existing class

    def preprocess_dataset(self):
        """
        Preprocesses the dataset by cleaning text and saving the cleaned dataset.
        """
        # Load the dataset
        df = pd.read_csv(self.input_file)

        # Check for required column
        if 'text' not in df.columns:
            raise ValueError("The dataset must contain a 'text' column.")

        # Apply the ArabicTextPreprocessor to the text column
        df['cleaned_text'] = df['text'].apply(self.text_preprocessor.preprocess)

        # Save the cleaned dataset
        df.to_csv(self.output_file, index=False)
        print(f"Cleaned dataset saved to {self.output_file}")

if __name__ == "__main__":
    # Define file paths
    input_file = "data/raw_dataset.csv"  # Raw dataset file path
    output_file = "data/cleaned_dataset.csv"  # Cleaned dataset file path

    # Initialize and run the preprocessor
    dataset_preprocessor = DatasetPreprocessor(input_file, output_file)
    dataset_preprocessor.preprocess_dataset()
