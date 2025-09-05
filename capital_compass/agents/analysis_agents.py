from capital_compass.state import CapitalCompassState
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

if not  os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY is not found in environmental variables. Please set your .env file")

financial_llm = ChatGroq(model="moonshotai/kimi-k2-instruct-0905")
sentiment_llm = ChatGroq(model="qwen/qwen3-32b")
report_llm = ChatGroq(model="openai/gpt-oss-120b")

def analyze_financials(state: CapitalCompassState):
    """
    Analyzes the company's financial overview data.

    Args:
        state: The current graph state.

    Returns:
        A dictionary with the quantitative analysis.
    """
    overview = state['overview_data']
    
    # Select key financial metrics to include in the prompt for efficiency
    try:
        market_cap_val = int(overview.get('MarketCapitalization', 0))
        market_cap_str = f"${market_cap_val:,}"
    except (ValueError, TypeError):
        market_cap_str = "N/A"
    key_metrics = {
        "Company": overview.get("Name"),
        "Sector": overview.get("Sector"),
        "P/E Ratio": overview.get("PERatio"),
        "EPS": overview.get("EPS"),
        "Return on Equity (ROE)": overview.get("ReturnOnEquityTTM"),
        "Market Cap": market_cap_str,
        "Dividend Yield": overview.get("DividendYield"),
        "52 Week High": overview.get("52WeekHigh"),
        "52 Week Low": overview.get("52WeekLow"),
    }
    prompt = f"""
    You are a senior financial analyst. Analyze the company's financial health using the metrics provided.  

    Organize your response into **detailed sections** with clear insights:  

    1. **Valuation**  
    - Analyze P/E, Forward P/E, PEG, Price-to-Book, and Price-to-Sales ratios.  
    - Compare current valuation multiples to growth prospects.  
    - Identify whether the company appears undervalued, fairly valued, or overvalued.  

    2. **Profitability**  
    - Evaluate margins (Operating Margin, Profit Margin, Gross Profit).  
    - Discuss efficiency ratios (ROE, ROA).  
    - Mention EPS trends and sustainability of earnings.  

    3. **Growth Trends**  
    - Examine Quarterly Revenue Growth (YoY), Quarterly Earnings Growth (YoY), and Revenue Per Share.  
    - Identify whether growth is accelerating, stable, or slowing.  
    - Note industry trends if implied.  

    4. **Financial Strength**  
    - Assess dividend policy (Dividend Yield, Dividend Per Share, payout sustainability).  
    - Mention Book Value and leverage considerations.  
    - Comment on Market Capitalization scale and stability.  

    5. **Risk Factors**  
    - Highlight volatility (Beta, 52-week range).  
    - Mention any financial vulnerabilities (high multiples, declining growth, low margins).  

    Be objective and data-driven. Do not make an explicit investment recommendation.    
    
    **Crucially, for each metric, provide context.** For example, don't just state the P/E ratio; 
    state whether it is high, low, or average for its specific sector (e.g., 'A P/E of 50 is high for an 
    industrial company but may be reasonable for a high-growth tech company.'). 
    This contextual judgment is the most important part of your analysis.
    **Key Metrics:**
    {chr(10).join([f'- {k}: {v}' for k, v in key_metrics.items()])}

    Additional Metrics:
    - Operating Margin: {overview.get("OperatingMarginTTM")}
    - Profit Margin: {overview.get("ProfitMargin")}
    - PEG Ratio: {overview.get("PEGRatio")}
    - Quarterly Revenue Growth (YoY): {overview.get("QuarterlyRevenueGrowthYOY")}
    - Quarterly Earnings Growth (YoY): {overview.get("QuarterlyEarningsGrowthYOY")}
    - Forward P/E: {overview.get("ForwardPE")}
    - Price to Book Ratio: {overview.get("PriceToBookRatio")}
    """
    response = financial_llm.invoke(prompt)
    return{"quantitative_analysis": response.content}


def analyze_sentiment(state: CapitalCompassState):
    """
    Analyzes the market sentiment based on news articles.

    Args:
        state: The current graph state.

    Returns:
        A dictionary with the qualitative analysis.
    """
    news_feed = state["news_data"].get("feed", [])

    # Format the top 20 news articles for the prompt
    formatted_news = []
    for article in news_feed[:20]:
        formatted_news.append(
            f"- Title: {article.get('title')}\n"
            f"  Summary: {article.get('summary')}\n"
            f"  Overall Sentiment: {article.get('overall_sentiment_label')}"
        )
    
    news_string = "\n\n".join(formatted_news)
    
    prompt = f"""
    You are a professional market news analyst. Review the following recent news articles and their sentiment labels.  
    Your goal is to extract **qualitative insights** about the company's market perception.  

    Structure your response into the following sections:

    1. **Overall Sentiment**  
    - Summarize sentiment as [Positive, Neutral, Negative].  
    - Support with an approximate balance (e.g., "6 positive vs 3 negative articles").  

    2. **Key Positive Themes**  
    - Highlight 2-3 major positive narratives (e.g., strong earnings, partnerships, new products, favorable analyst coverage).  

    3. **Key Negative Themes**  
    - Highlight 2-3 major risks (e.g., lawsuits, layoffs, competitive threats, regulatory concerns).  

    4. **Investor/Market Perception**  
    - Summarize how the market is perceiving the company in the short term.  
    - Note whether sentiment aligns with financial performance (optimistic, cautious, skeptical).  

    5. **Risks & Opportunities**  
    - Identify 1-2 potential risks from the news cycle.  
    - Identify 1-2 opportunities that could impact future performance.  

    Do not provide an explicit investment recommendation.  
    
    *For each key theme you identify, speculate on the potential business impact.** 
    For example, don't just say 'The company announced a new partnership'; explain that 
    'This partnership could open up a new revenue stream in the European market within the next 1-2 years.' 
    Connect the news to tangible business effects.

    **Recent News Articles:**
    {news_string}
    """
    response = sentiment_llm.invoke(prompt)
    return{"qualitative_analysis": response.content}

def critique_analysis(state: CapitalCompassState) -> dict:
    """
    Critiques the initial financial and sentiment analyses to find weaknesses.
    """
    
    quant_analysis = state["quantitative_analysis"]
    qual_analysis = state["qualitative_analysis"]

    prompt = f"""
    You are a skeptical "Red Team" analyst. Your job is to find weaknesses and contradictions in the following financial and news analyses.
    Do not agree with the analysis. Your only role is to challenge it.

    **Financial Analysis:**
    ---
    {quant_analysis}
    ---
    **News Sentiment Analysis:**
    ---
    {qual_analysis}
    ---

    Based on the above, provide 2-3 bullet points of critical counterarguments or overlooked risks. For example: "The financial analysis highlights strong revenue growth, but fails to address the declining profit margins." or "The news analysis is optimistic about the new product, but downplays the competitive threat from XYZ Corp mentioned in one article."
    """
    
    # You can use one of your existing LLMs for this
    response = financial_llm.invoke(prompt)
    return {"critique": response.content}


def generate_final_report(state: CapitalCompassState):
    """
    Synthesizes all analyses into a final investment report.

    Args:
        state: The current graph state.

    Returns:
        A dictionary with the final report.
    """
    
    quant_analysis = state["quantitative_analysis"]
    qual_analysis = state["qualitative_analysis"]
    critique = state['critique']
    
    prompt = f"""
    You are a decisive senior investment advisor for "Capital Compass", preparing a confidential briefing memo for a knowledgeable but busy client. Your analysis must be clear, data-driven, and lead to a definitive conclusion.

    **Financial Analysis:**
    ---
    {quant_analysis}
    ---

    **News Sentiment Analysis:**
    ---
    {qual_analysis}
    ---

    **Critical Counterarguments to Consider:**
    ---
    {critique} 
    ---
    
    **Final Investment Report:**
    Your primary task is to determine if the Bull Case decisively outweighs the Bear Case, or vice-versa. Based on this weighting, generate a professional investment report.

    **1. Final Recommendation**
    -   Your primary recommendation must be either **"Invest"** or **"Do Not Invest"**.
    -   You may only use **"Hold with Caution"** in the rare event that the bull and bear cases are in almost perfect equilibrium and you must explicitly justify why a decisive call cannot be made in the rationale.

    **2. Confidence & Horizon**
    - **Confidence:** [High, Medium, or Low]. Justify in one sentence.
    - **Horizon:** [Short-Term (1-6 months), Medium-Term (6-18 months), or Long-Term (18+ months)].

    **3. Executive Summary**
    - A 3-4 sentence paragraph summarizing the core recommendation, key financial health indicators (valuation & profitability), and the prevailing market sentiment.

    **4. Key Drivers & Rationale**
    - Provide 3-4 detailed bullet points. Each point must explain a key driver for your recommendation, supported by specific data (e.g., 'P/E of 35.5') or news themes (e.g., 'recent product launch').

    **5. Bull Case: Strengths & Opportunities**
    - Detail the company's positive aspects. Cite specific financial strengths (e.g., strong YoY revenue growth of 25%, high profit margins) and positive news themes (e.g., strategic partnerships, innovation).

    **6. Bear Case: Risks & Challenges**
    - Detail the company's negative aspects. Address specific financial risks (e.g., high valuation multiples relative to the sector, significant debt) and negative news themes (e.g., increased competition, regulatory concerns).

    **7. Valuation Context**
    - Briefly explain whether the company's key valuation multiples (P/E, Price/Book) appear high, low, or fair in the context of its industry sector and growth profile.

    **8. Concluding Remarks**
    - A single, forward-looking sentence to conclude the report.
    
    **Final Instruction:** Do not default to a neutral recommendation. The client expects a decisive, well-supported verdict. Make a call.
    """
    
    response = report_llm.invoke(prompt)
    return{"final_report": response.content}

