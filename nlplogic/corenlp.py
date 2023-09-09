#!/usr/bin/env python
from textblob import TextBlob
import wikipedia as wiki


# function to pull a text
def get_text(name):
    """
    Get text by searching for a given name.

    Args:
        name (str): The name to search for.

    Returns:
        str: The text found by searching for the given name.
    """
    print(f"searching for {name}")
    return wiki.search(name)


def summarize_wiki(name):
    """
    Retrieves a summary of information from Wikipedia based on the given name.

    Args:
        name (str): The name to search for in Wikipedia.

    Returns:
        str: The summary of information retrieved from Wikipedia.
    """
    print(f"Finding wikipedia summary for name: {name}")
    return wiki.summary(name)

def get_text_blob(text):
    """
    Returns a TextBlob object representing the given text.

    Args:
        text (str): The input text.

    Returns:
        TextBlob: A TextBlob object representing the given text.
    """
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """
    Extracts noun phrases from a Wikipedia article.

    Args:
        name (str): The name of the Wikipedia article.

    Returns:
        list: A list of noun phrases extracted from the article.
    """
    # Get the text of the Wikipedia article
    text = summarize_wiki(name)

    # Create a TextBlob object from the article text
    blob = get_text_blob(text)

    # Extract noun phrases from the TextBlob object
    phrases = blob.noun_phrases

    # Return the extracted noun phrases
    return phrases
