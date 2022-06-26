'''Utility module containing methods for preprocessing
the app reviews data.'''
import re
import nltk

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def binarize(star):
    '''Given a rating (start) returns if it is
    positive rating or negative rating.'''
    return 1 if star >= 3 else 0

def preprocess_text(text):
    text = text.lower()

    # Additional contractions reference: https://edu.gcfglobal.org/en/grammar/contractions/1/
    text = re.sub('\'t', ' not', text)
    text = re.sub('\'s', ' is', text)
    text = re.sub('\'ve', ' have', text)
    text = re.sub('\'m', ' am', text)
    text = re.sub('\'re', ' are', text)
    text = re.sub('\'ll', ' will', text)
    text = re.sub('\'d', ' would', text)

    # Replace character other than a-z, A-Z, 0-9, _ with space
    text = re.sub(r'\W', ' ', text)

    # Replace multiple spaces with single space
    text = re.sub(' {2,}', ' ', text)

    # Remove one letter words
    pattern = r'\b\w{,1}\b'
    text = re.sub(pattern, '', text)

    return text

# Reference: https://towardsdatascience.com/sentimental-analysis-using-vader-a3415fef7664
sid = SentimentIntensityAnalyzer()
def is_positive(text):
    score = sid.polarity_scores(text)
    if score['compound'] >= 0.5:
        return 1
    elif score['compound'] <= -0.5:
        return 0
    else:
        return -1

def get_contradicting_app_reviews(df, review_col, rating_col):
    # Drop rows whose review is 'nan'
    df = df.drop(df[df[review_col].isna()].index)
    # Binarize the rating to positive/negative
    df['is_positive'] = df[rating_col].map(binarize)
    # Preprocess the text review
    df[review_col] = df[review_col].apply(preprocess_text)
    # Get polarity using semantics of the text review
    df['is_positive_vader'] = df[review_col].apply(is_positive)
    
    # Get rid of neutral reviews
    df_vader = df[df['is_positive_vader'] != -1]

    # Get reviews with contradictions between actual polarity and predicted polarity
    mask = df_vader['is_positive'] != df_vader['is_positive_vader']
    records = df_vader[mask][[review_col, rating_col]]
    records = records.sort_values(rating_col, ascending=False)

    return records