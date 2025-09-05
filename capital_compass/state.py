from typing import TypedDict

class CapitalCompassState(TypedDict):
    """
    The state for our graph. It holds all the data we gather and generate
    as it flows through the nodes.

    Attributes:
        company_ticker: The stock ticker to analyze (e.g., "AAPL").
        overview_data: The raw JSON data from the Alpha Vantage OVERVIEW endpoint.
        news_data: The raw JSON data from the Alpha Vantage NEWS_SENTIMENT endpoint.
        quantitative_analysis: The LLM's analysis of the financial data.
        qualitative_analysis: The LLM's analysis of the news and sentiment.
        critique The LLM's critique from quantitative and qualitative analysis.
        final_report: The final, synthesized investment report.
    """
    
    company_ticker: str
    overview_data: dict
    news_data: dict
    quantitative_analysis: str
    qualitative_analysis: str
    critique: str
    final_report: str