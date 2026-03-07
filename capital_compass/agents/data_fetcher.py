from capital_compass.state import CapitalCompassState
from capital_compass.tools.alpha_vantage_client import get_company_overview, get_news_sentiment
from capital_compass.tools.tavily_search_tool import tavily_search_tool
from capital_compass.utils.data_normalizer import normalize_overview_data, normalize_news_sentiment_data


def fetch_overview_node(state: CapitalCompassState):
    ticker = state['company_ticker']
    overview = get_company_overview(ticker=ticker)

    # Validate response - check for error messages
    if "Information" in overview or "Error Message" in overview or "Note" in overview:
        # Return empty dict instead of error data
        return {"overview_data": {}}

    # Normalize the API response (convert "1. Name" to "Name")
    normalized_overview = normalize_overview_data(overview)
    return {"overview_data": normalized_overview}


def fetch_news_node(state: CapitalCompassState):
    ticker = state['company_ticker']
    news = get_news_sentiment(ticker)

    # Validate response
    if "Information" in news or "Error Message" in news or "Note" in news:
        return {"news_data": {"feed": []}}

    # Normalize the API response
    normalized_news = normalize_news_sentiment_data(news)
    return {"news_data": normalized_news}


def web_search_node(state: CapitalCompassState):
    ticker = state['company_ticker']
    search_results = tavily_search_tool(ticker=ticker)
    return {"web_search_data": search_results}