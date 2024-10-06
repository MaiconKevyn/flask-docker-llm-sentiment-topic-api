"""Module providing functionalities for text analysis including sentiment and topic classification."""

import logging
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

#Topic modeling
MINIMUM_CONFIABILITY_SCORE = 0.7
topics = ["Performance", "Quality", "Usability", "Error Handling", "Personal Data", "Data Accuracy"]
topic_modeling_model_name = "MoritzLaurer/deberta-v3-large-zeroshot-v2.0"
topic_classifier = pipeline("zero-shot-classification", model=topic_modeling_model_name)

def classify_topic(text):
    """
    Classifies the given text into predefined topics using zero-shot classification.

    This function uses a zero-shot classification model to analyze the given text
    and classify it into one or more predefined topics. It applies a threshold
    to filter topics based on their confidence scores.

    Parameters:
        text (str): The text to be classified into topics.

    Returns:
        list: A list of topics that have confidence scores above the defined threshold.
    """

    hypothesis_template = """The following text is a user comment from a product feedback system,
     primarily concerning the {} aspect of the product."""

    topics_result = topic_classifier(text,
                                     topics,
                                     multi_label=True,
                                     hypothesis_template=hypothesis_template
    )
    topics_above_threshold = [
        topic for topic, score in zip(topics_result['labels'], topics_result['scores']) if score > MINIMUM_CONFIABILITY_SCORE
    ]
    return topics_above_threshold

#Sentiment analysis
sentiment_analysis_model_name = 'cardiffnlp/twitter-roberta-base-sentiment-latest'
sentiment_analysis_tokenizer = AutoTokenizer.from_pretrained(sentiment_analysis_model_name)
sentiment_analysis_model = AutoModelForSequenceClassification.from_pretrained(sentiment_analysis_model_name)
sentiment_classifier = pipeline('sentiment-analysis', model=sentiment_analysis_model, tokenizer=sentiment_analysis_tokenizer)

def classify_sentiment(text):
    """
    Classifies the sentiment of the given text.

    This function uses a sentiment analysis model to classify the given text 
    into one of the predefined sentiment labels (e.g., positive, negative, neutral).

    Parameters:
        text (str): The text to be analyzed for sentiment.

    Returns:
        str: The sentiment label of the text (e.g., 'positive', 'negative', 'neutral').
    """

    result = sentiment_classifier(text)
    return result[0]['label']

def is_comment_valid(comment):
    """
    Preprocesses the input comment to clean and validate it before further analysis.

    Args:
    comment (str): The comment text to preprocess.

    Returns:
    str or None: Returns the processed comment if it's valid, or None if it's invalid.
    """

    is_only_digit = comment.isdigit()
    is_only_symbols = re.match(r'^\W+$', comment)
    is_repeated_chars = len(comment) < 2 or comment == len(comment) * comment[0] #verifica se o comentario tem apenas um caracter repetido

    return not is_only_digit and not is_only_symbols and not is_repeated_chars

#Feedback analysis
def analyze(text):
    """
    Conducts a comprehensive analysis of the provided text, determining both sentiment 
    and topic classifications.

    This function orchestrates the entire process of text analysis by first verifying the 
    validity of the input text using `is_comment_valid`. If the text is deemed invalid, 
    it logs an error and returns an error message.
    If valid, the function proceeds to determine the sentiment of the text with 
    `classify_sentiment` and classify
    its topic with `classify_topic`. The results from both operations are combined into 
    a single dictionary, which is then logged and returned.

    Args:
        text (str): The text to be analyzed. It should be a non-empty string that 
        is not composed solely of digits or special characters.

    Returns:
        dict: A dictionary containing the results of the sentiment and topic analysis 
        if the text is valid.
        If the text is invalid or an error occurs during processing, it returns a dictionary 
        with an 'error' key and a descriptive message as its value.

    Raises:
        Exception: Captures and logs any exception that arises during the sentiment or topic 
        classification process, returning an error message within the dictionary. 
        This ensures the function does not cause the application to crash and provides meaningful 
        error information to the caller.
    """
    if not is_comment_valid(text):
        error_message = "Invalid input text"
        logging.error(error_message)
        return {"error": error_message}

    try:
        sentiment = classify_sentiment(text)
        topic = classify_topic(text)
        analysis_result = {
            'sentiment': sentiment,
            'topic': topic
        }
        return analysis_result
    except ValueError as ve:
        logging.error("Value error encountered: %s", str(ve), exc_info=True)
        return {"error": str(ve)}
    except RuntimeError as rne:
        logging.error("Runtime error during model processing: %s", str(rne), exc_info=True)
        return {"error": "Model processing error"}
    except Exception as e:
        logging.error("Unexpected error processing text: %s", str(e), exc_info=True)
        return {"error": "An unexpected error occurred"}
