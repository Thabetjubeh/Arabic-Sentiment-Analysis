# Arabic Sentiment Analysis

## Description
A supervised learning project to classify Arabic text as positive, negative, or neutral. Built using Python with free and open-source tools.

## Features
- Preprocessing Arabic text (diacritics removal, tokenization, normalization)
- Model training with Logistic Regression, SVM, or BERT
- REST API for sentiment analysis

## Getting Started

### Prerequisites
- Python 3.8 or later

### Setup
1. Clone the repository:

### Usage

#### Preprocessing the Dataset

Before training the model, preprocess the raw dataset to clean and normalize the text.

##### Steps:

1. Place your raw dataset file (in CSV format) in the `data/` directory and name it `raw_dataset.csv`.
   - The file should have at least one column named `text` containing the raw Arabic text.

2. Run the preprocessing script:
   ```bash
   python src/dataset_preprocessor.py

3. The cleaned dataset will be saved in the `data/` directory as `cleaned_dataset.csv`.

### License
This project is licensed under the MIT License.