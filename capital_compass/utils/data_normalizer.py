"""
Data normalization utilities for API responses.

Alpha Vantage API responses often use numbered keys (e.g., "1. Name", "2. Symbol").
This module provides utilities to convert these to plain keys for easier access.
"""


def normalize_overview_data(raw_data: dict) -> dict:
    """
    Converts Alpha Vantage OVERVIEW API response with numbered keys to plain keys.

    Args:
        raw_data: Raw response dict from Alpha Vantage OVERVIEW endpoint

    Returns:
        Normalized dict with plain keys (e.g., "Name" instead of "1. Name")

    Example:
        Input: {"1. Symbol": "AAPL", "2. Name": "Apple Inc."}
        Output: {"Symbol": "AAPL", "Name": "Apple Inc."}
    """
    normalized = {}

    # Skip informational messages or error responses
    if not raw_data or any(key in raw_data for key in ["Information", "Error Message", "Note"]):
        return raw_data

    for key, value in raw_data.items():
        # Remove "1. ", "2. ", etc. prefix (pattern: "N. keyname")
        if ". " in key:
            clean_key = key.split(". ", 1)[-1]
        else:
            clean_key = key
        normalized[clean_key] = value

    return normalized


def normalize_news_sentiment_data(raw_data: dict) -> dict:
    """
    Normalizes Alpha Vantage NEWS_SENTIMENT API response.

    Args:
        raw_data: Raw response dict from Alpha Vantage NEWS_SENTIMENT endpoint

    Returns:
        Normalized dict
    """
    # News sentiment data typically has a "feed" array with articles
    # Each article may have numbered keys
    if "feed" not in raw_data:
        return raw_data

    normalized_feed = []
    for article in raw_data.get("feed", []):
        normalized_article = {}
        for key, value in article.items():
            if ". " in key:
                clean_key = key.split(". ", 1)[-1]
            else:
                clean_key = key
            normalized_article[clean_key] = value
        normalized_feed.append(normalized_article)

    return {
        **raw_data,
        "feed": normalized_feed
    }
