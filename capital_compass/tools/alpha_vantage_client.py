import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

from capital_compass.exceptions import APIClientError

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

if not API_KEY:
    raise ValueError("ALPHAVANTAGE_API_KEY is not found in environmental variables. Please set your .env file")

def get_company_overview(ticker: str) -> dict:
    """
    Fetches company overview data (P/E Ratio, EPS, etc.) from Alpha Vantage.
    """
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Checks for bad HTTP responses
        data = response.json()
        
        if not data or "Error Message" in data:
            raise APIClientError(f"Ticker '{ticker}' not found or is invalid. Please check the symbol.")
        # Handles cases where the API returns a note (e.g., rate limit)
        if not data or "Note" in data:
            raise APIClientError(f"API limit reached or no data found for OVERVIEW of {ticker}.")
            
        return data
    except requests.exceptions.RequestException as e:
        # Raises a custom error for network or HTTP issues
        raise APIClientError(f"Network error fetching company overview for {ticker}: {e}")
    except requests.exceptions.JSONDecodeError:
        # Raises a custom error if the response is not valid JSON
        raise APIClientError(f"Failed to decode JSON response for OVERVIEW of {ticker}.")

def get_news_sentiment(ticker: str) -> dict:
    """
    Fetches recent news and sentiment scores from the last 60 days.
    """
    time_from = (datetime.now() - timedelta(days=60)).strftime('%Y%m%dT%H%M')
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&time_from={time_from}&limit=25&apikey={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not data or "Note" in data:
            raise APIClientError(f"API limit reached or no data found for NEWS_SENTIMENT of {ticker}.")

        return data
    except requests.exceptions.RequestException as e:
        raise APIClientError(f"Network error fetching news sentiment for {ticker}: {e}")
    except requests.exceptions.JSONDecodeError:
        raise APIClientError(f"Failed to decode JSON response for NEWS_SENTIMENT of {ticker}.")


def search_company_by_name(keywords: str) -> list[dict]:
    """
    Search for company ticker by company name or partial name using Alpha Vantage SYMBOL_SEARCH endpoint.

    Args:
        keywords: Company name or partial name to search

    Returns:
        List of matching companies with keys: symbol, name, type, region, marketOpen, marketClose, timezone, currency, matchScore
        Sorted by matchScore in descending order (best matches first)

    Raises:
        APIClientError: If API request fails or returns error
    """
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Handle API rate limit or no data
        if data and "Note" in data:
            raise APIClientError(f"API limit reached or no data found for search: {keywords}.")

        # Get best matches from response
        matches = data.get("bestMatches", [])

        # Normalize keys - Alpha Vantage returns numbered keys like "1. symbol", "2. name"
        normalized = []
        for match in matches:
            normalized.append({
                "symbol": match.get("1. symbol") or match.get("symbol"),
                "name": match.get("2. name") or match.get("name"),
                "type": match.get("3. type") or match.get("type"),
                "region": match.get("4. region") or match.get("region"),
                "marketOpen": match.get("5. marketOpen") or match.get("marketOpen"),
                "marketClose": match.get("6. marketClose") or match.get("marketClose"),
                "timezone": match.get("7. timezone") or match.get("timezone"),
                "currency": match.get("8. currency") or match.get("currency"),
                "matchScore": match.get("9. matchScore") or match.get("matchScore"),
            })

        # Sort by match score (descending) - best matches first
        normalized.sort(key=lambda x: float(x.get("matchScore", 0)), reverse=True)

        return normalized

    except requests.exceptions.RequestException as e:
        raise APIClientError(f"Network error searching for company '{keywords}': {e}")
    except requests.exceptions.JSONDecodeError:
        raise APIClientError(f"Failed to decode JSON response for search: {keywords}.")


#Self testing code
if __name__ == "__main__":
    ticker = "AAPL"
    try:
        overview_data = get_company_overview(ticker)
        news_data = get_news_sentiment(ticker)
        print("Successfully fetched data.")
        # print(overview_data)
        # print(news_data)
    except APIClientError as e:
        print(f"An error occurred: {e}")
