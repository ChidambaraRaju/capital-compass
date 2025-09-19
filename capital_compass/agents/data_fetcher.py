from capital_compass.state import CapitalCompassState
from capital_compass.tools.alpha_vantage_client import get_company_overview, get_news_sentiment
from capital_compass.tools.tavily_search_tool import tavily_search_tool

def fetch_overview_node(state: CapitalCompassState):
    ticker = state['company_ticker']
    overview = get_company_overview(ticker=ticker)
    return{"overview_data": overview}

def fetch_news_node(state: CapitalCompassState):
    ticker = state['company_ticker']
    news = get_news_sentiment(ticker=ticker)
    return{"news_data": news}

def web_search_node(state: CapitalCompassState):
    ticker = state['company_ticker']
    search_results = tavily_search_tool(ticker=ticker)
    return {"web_search_data": search_results}