from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

if not os.environ["TAVILY_API_KEY"]:
    raise ValueError("TAVILY_API_KEY is not found in environmental variables. Please set your .env file")

def tavily_search_tool(ticker: str):
    """
    Uses the Tavily Search tool to fetch Latest analyst ratings and consensus price target for a given stock ticker.
    """
    tavily_tool = TavilySearch(max_results=10)
    search_query = f"Latest analyst ratings and consensus price target for {ticker}"
    results = tavily_tool.invoke(search_query)
    return results


'''
#Self testing code
if __name__ == "__main__":
    ticker = "NVDA"
    search_results = tavily_search_tool(ticker)
    print(search_results)
'''