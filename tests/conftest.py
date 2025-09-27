import pytest
from capital_compass.state import CapitalCompassState


sample_ticker = "NVDA"


mock_alphavantage_overview = {
  "overview_data": {
    "Symbol": "NVDA",
    "AssetType": "Common Stock",
    "Name": "NVIDIA Corporation",
    "Description": "NVIDIA Corporation is a leading American multinational technology company headquartered in Santa Clara, California, specializing in the design and manufacture of advanced graphics processing units (GPUs) primarily for gaming and professional applications. Renowned for its pioneering work in visual computing and AI technologies, NVIDIA also develops System on a Chip (SoC) solutions for mobile computing and automotive sectors, positioning itself at the forefront of innovation in autonomous driving and AI-driven applications. With a robust portfolio that spans across gaming, data centers, and AI infrastructure, NVIDIA continues to drive significant advancements in technology, catering to a rapidly evolving market landscape.",
    "CIK": "1045810",
    "Exchange": "NASDAQ",
    "Currency": "USD",
    "Country": "USA",
    "Sector": "TECHNOLOGY",
    "Industry": "SEMICONDUCTORS",
    "Address": "2788 SAN TOMAS EXPRESSWAY, SANTA CLARA, CA, UNITED STATES, 95051",
    "OfficialSite": "https://www.nvidia.com",
    "FiscalYearEnd": "January",
    "LatestQuarter": "2025-07-31",
    "MarketCapitalization": "4326218531000",
    "EBITDA": "98280997000",
    "PERatio": "50.48",
    "PEGRatio": "1.317",
    "BookValue": "4.113",
    "DividendPerShare": "0.04",
    "DividendYield": "0.0002",
    "EPS": "3.52",
    "RevenuePerShareTTM": "6.75",
    "ProfitMargin": "0.524",
    "OperatingMarginTTM": "0.608",
    "ReturnOnAssetsTTM": "0.531",
    "ReturnOnEquityTTM": "1.094",
    "RevenueTTM": "165217993000",
    "GrossProfitTTM": "115399999000",
    "DilutedEPSTTM": "3.52",
    "QuarterlyEarningsGrowthYOY": "0.612",
    "QuarterlyRevenueGrowthYOY": "0.556",
    "AnalystTargetPrice": "213.18",
    "AnalystRatingStrongBuy": "10",
    "AnalystRatingBuy": "47",
    "AnalystRatingHold": "6",
    "AnalystRatingSell": "1",
    "AnalystRatingStrongSell": "0",
    "TrailingPE": "50.48",
    "ForwardPE": "39.37",
    "PriceToSalesRatioTTM": "26.18",
    "PriceToBookRatio": "43.03",
    "EVToRevenue": "25.82",
    "EVToEBITDA": "41.33",
    "Beta": "2.102",
    "52WeekHigh": "184.55",
    "52WeekLow": "86.61",
    "50DayMovingAverage": "176.46",
    "200DayMovingAverage": "141.64",
    "SharesOutstanding": "24347000000",
    "SharesFloat": "23325084000",
    "PercentInsiders": "4.329",
    "PercentInstitutions": "68.978",
    "DividendDate": "2025-10-02",
    "ExDividendDate": "2025-09-11"
  }
}
    

mock_alphavantage_news = {
  "news_data": {
    "items": "50",
    "sentiment_score_definition": "x <= -0.35: Bearish; -0.35 < x <= -0.15: Somewhat-Bearish; -0.15 < x < 0.15: Neutral; 0.15 <= x < 0.35: Somewhat_Bullish; x >= 0.35: Bullish",
    "relevance_score_definition": "0 < x <= 1, with a higher score indicating higher relevance.",
    "feed": [
      {
        "title": "How Huawei and DeepSeek are helping China break reliance on US chips",
        "url": "https://www.scmp.com/tech/tech-war/article/3327025/home-grown-heroes-how-huawei-and-deepseek-are-helping-china-break-reliance-us-chips",
        "time_published": "20250927T020009",
        "authors": [
          "Ann Cao"
        ],
        "summary": "When Chinese artificial intelligence start-up DeepSeek unveiled an updated foundational model late in August, investors in Nvidia were stunned. Shares of the US chip giant slid, as market watchers grappled with news that the two-year-old start-up, which has developed models rivalling the world's ...",
        "banner_image": "https://img.i-scmp.com/cdn-cgi/image/fit=contain,width=1024,format=auto/sites/default/files/d8/images/canvas/2025/09/26/11bbd080-484c-4899-8f59-731400f9f2e9_1126e908.jpg",
        "source": "South China Morning Post",
        "category_within_source": "Money",
        "source_domain": "www.scmp.com",
        "topics": [
          {
            "topic": "Earnings",
            "relevance_score": "0.108179"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.108179"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.190112,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "BABA",
            "relevance_score": "0.024982",
            "ticker_sentiment_score": "0.0",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.149038",
            "ticker_sentiment_score": "0.076158",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "TCTZF",
            "relevance_score": "0.024982",
            "ticker_sentiment_score": "-0.074991",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "TSM",
            "relevance_score": "0.024982",
            "ticker_sentiment_score": "-0.030285",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Prediction: This Artificial Intelligence  ( AI )  Semiconductor Stock Will Join Nvidia, Microsoft, Apple, Alphabet, and Amazon in the $2 Trillion Club by 2028.  ( Hint: Not Broadcom ) ",
        "url": "https://www.fool.com/investing/2025/09/26/prediction-this-artificial-intelligence-ai-semicon/",
        "time_published": "20250926T233000",
        "authors": [
          "Stefon Walters"
        ],
        "summary": "When you're the industry leader by a large margin, growth is on your side.",
        "banner_image": "https://media.ycharts.com/charts/4b95665eb65d5d8f647c27017a06d738.png",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Earnings",
            "relevance_score": "0.95493"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.214378"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.312234,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.061003",
            "ticker_sentiment_score": "0.014015",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "TSM",
            "relevance_score": "0.12165",
            "ticker_sentiment_score": "0.129961",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Better Artificial Intelligence Stock: D-Wave Quantum vs. Nvidia",
        "url": "https://www.fool.com/investing/2025/09/26/better-artificial-intelligence-stock-d-wave-quantu/",
        "time_published": "20250926T213000",
        "authors": [
          "Robert Izquierdo"
        ],
        "summary": "These tech companies are all about pushing the boundaries of AI.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834470%2Fai_held_in_hand_performs_tasks-gettyimages-1466924677-1200x604-259c774.png&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Economy - Monetary",
            "relevance_score": "0.158519"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.316726"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.161647"
          }
        ],
        "overall_sentiment_score": 0.291351,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.410059",
            "ticker_sentiment_score": "0.277063",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "QBTS",
            "relevance_score": "0.189298",
            "ticker_sentiment_score": "0.181598",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "CoreWeave's Growth Story Gets a $6.3 Billion Lifeline: What Long-Term Investors Should Know",
        "url": "https://www.fool.com/investing/2025/09/26/coreweaves-growth-story-gets-a-63-billion-lifeline/",
        "time_published": "20250926T211500",
        "authors": [
          "Harsh Chauhan"
        ],
        "summary": "This cloud artificial intelligence (AI) infrastructure provider's latest deal could ensure years of solid growth.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834465%2Fpeople-discussing-monitor.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "IPO",
            "relevance_score": "0.158519"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.87644"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.918141"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.27882,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "CORZQ",
            "relevance_score": "0.046999",
            "ticker_sentiment_score": "0.005986",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "MSFT",
            "relevance_score": "0.046999",
            "ticker_sentiment_score": "0.133368",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "CRWV",
            "relevance_score": "0.590712",
            "ticker_sentiment_score": "0.386177",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "META",
            "relevance_score": "0.046999",
            "ticker_sentiment_score": "0.133368",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.362725",
            "ticker_sentiment_score": "0.291451",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Top Analyst Reports for NVIDIA, Berkshire Hathaway & Home Depot",
        "url": "https://www.zacks.com/research-daily/2757681/top-analyst-reports-for-nvidia-berkshire-hathaway-home-depot",
        "time_published": "20250926T210000",
        "authors": [
          "Mark Vickery"
        ],
        "summary": "Today's Research Daily features new research reports on 16 major stocks, including NVIDIA, Berkshire Hathaway, and Home Depot, as well as a micro-cap stock, BayFirst Financial.",
        "banner_image": "https://staticx-tuner.zacks.com/images/articles/main/c1/13186.jpg",
        "source": "Zacks Commentary",
        "category_within_source": "n/a",
        "source_domain": "www.zacks.com",
        "topics": [
          {
            "topic": "Retail & Wholesale",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.929393"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.576289"
          },
          {
            "topic": "Finance",
            "relevance_score": "0.333333"
          }
        ],
        "overall_sentiment_score": 0.164506,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "BAFN",
            "relevance_score": "0.074001",
            "ticker_sentiment_score": "0.132164",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.074001",
            "ticker_sentiment_score": "0.193771",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "HD",
            "relevance_score": "0.147366",
            "ticker_sentiment_score": "0.106886",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "BRK-A",
            "relevance_score": "0.074001",
            "ticker_sentiment_score": "0.137598",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Prediction: This Artificial Intelligence  ( AI )  Stock Will Be Worth More Than $5 Trillion by 2030  ( Hint: It's Not Nvidia or Apple ) ",
        "url": "https://www.fool.com/investing/2025/09/26/prediction-this-artificial-intelligence-ai-stock-w/",
        "time_published": "20250926T210000",
        "authors": [
          "Manali Pradhan"
        ],
        "summary": "Amazon could pleasantly surprise long-term investors.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834451%2Fanalyst_studying_charts_on_a_laptop.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Retail & Wholesale",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.360215"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.538269"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.333333"
          }
        ],
        "overall_sentiment_score": 0.185293,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "MSFT",
            "relevance_score": "0.03878",
            "ticker_sentiment_score": "0.0",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.03878",
            "ticker_sentiment_score": "0.0",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "ROKU",
            "relevance_score": "0.03878",
            "ticker_sentiment_score": "0.123096",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "AMZN",
            "relevance_score": "0.503947",
            "ticker_sentiment_score": "0.308648",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "What Is 1 of the Best Artificial Intelligence  ( AI )  Stocks to Buy Now?",
        "url": "https://www.fool.com/investing/2025/09/26/best-artificial-intelligence-ai-stock-buy-nvda/",
        "time_published": "20250926T205107",
        "authors": [
          "Neil Patel"
        ],
        "summary": "Investors must figure out ways to profit from the ongoing AI trend.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834847%2Fcomputer-with-ai-written-in-middle.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Earnings",
            "relevance_score": "0.614606"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.214378"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.49068,
        "overall_sentiment_label": "Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.2872",
            "ticker_sentiment_score": "0.335808",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Taiwan Semiconductor Options Trading: A Deep Dive into Market Sentiment - Taiwan Semiconductor  ( NYSE:TSM ) ",
        "url": "https://www.benzinga.com/insights/options/25/09/47900637/taiwan-semiconductor-options-trading-a-deep-dive-into-market-sentiment",
        "time_published": "20250926T200217",
        "authors": [
          "Benzinga Insights"
        ],
        "summary": "Deep-pocketed investors have adopted a bullish approach towards Taiwan Semiconductor ( NYSE: TSM ) , and it's something market players shouldn't ignore. Our tracking of public options records at Benzinga unveiled this significant move today.",
        "banner_image": "https://www.benzinga.com/next-assets/images/schema-image-default.png",
        "source": "Benzinga",
        "category_within_source": "Markets",
        "source_domain": "www.benzinga.com",
        "topics": [
          {
            "topic": "IPO",
            "relevance_score": "0.158519"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.316726"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.158519"
          },
          {
            "topic": "Finance",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.199751,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.077593",
            "ticker_sentiment_score": "0.147103",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "BCS",
            "relevance_score": "0.077593",
            "ticker_sentiment_score": "0.040817",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "TSM",
            "relevance_score": "0.229872",
            "ticker_sentiment_score": "0.243583",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "IREN Stock Is Trending Friday: What's Going On? - IREN  ( NASDAQ:IREN ) ",
        "url": "https://www.benzinga.com/trading-ideas/movers/25/09/47898448/iren-stock-is-trending-friday-whats-going-on",
        "time_published": "20250926T183240",
        "authors": [
          "Henry Khederian"
        ],
        "summary": "Shares of IREN Ltd ( NASDAQ: IREN ) are falling sharply Friday after JP Morgan downgraded the stock from Neutral to Underweight. The downgrade is injecting caution into a stock that has been on a meteoric rise, putting the brakes on a rally that has exceeded 500% over the past six months.",
        "banner_image": "https://cdn.benzinga.com/files/images/story/2025/09/26/IREN-Limited.jpeg?width=1200&height=800&fit=crop",
        "source": "Benzinga",
        "category_within_source": "News",
        "source_domain": "www.benzinga.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.999897"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.198083,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.07887",
            "ticker_sentiment_score": "0.064716",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Nvidia vs. AMD: Which Artificial Intelligence  ( AI )  Stock Is the Smarter Buy After Groq's $750 Million Equity Raise?",
        "url": "https://www.fool.com/investing/2025/09/26/nvidia-vs-amd-which-ai-stock-is-the-smarter-buy-af/",
        "time_published": "20250926T172600",
        "authors": [
          "Adam Spatacco"
        ],
        "summary": "Silicon Valley chip startup Groq just secured $750 million in funding at a $6.9 billion valuation.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834058%2Fgettyimages-2150878112.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.108179"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.283955,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "AMD",
            "relevance_score": "0.448842",
            "ticker_sentiment_score": "0.415187",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "MSFT",
            "relevance_score": "0.052801",
            "ticker_sentiment_score": "-0.091122",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "SSNLF",
            "relevance_score": "0.052801",
            "ticker_sentiment_score": "0.113624",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.49219",
            "ticker_sentiment_score": "0.319224",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "AVGO",
            "relevance_score": "0.052801",
            "ticker_sentiment_score": "0.109625",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "ASCCF",
            "relevance_score": "0.052801",
            "ticker_sentiment_score": "0.109625",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Why Is Intel Stock Jumping Today?",
        "url": "https://www.fool.com/investing/2025/09/26/why-is-intel-stock-jumping-today/",
        "time_published": "20250926T171707",
        "authors": [
          "Johnny Rice"
        ],
        "summary": "A month after the federal government took a 10% stake in Intel, President Trump is considering new tariffs.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F835289%2Fchipai.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.360215"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.234426,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.129516",
            "ticker_sentiment_score": "0.165635",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "AWON",
            "relevance_score": "0.129516",
            "ticker_sentiment_score": "0.0",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "INTC",
            "relevance_score": "0.85773",
            "ticker_sentiment_score": "0.467719",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "ON",
            "relevance_score": "0.129516",
            "ticker_sentiment_score": "0.189279",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Intel, Boeing Soar, Silver Hits $46 And Bitcoin Slips Below $110,000 - Apple  ( NASDAQ:AAPL ) ",
        "url": "https://www.benzinga.com/news/25/09/47896070/intel-boeing-wall-street-friday-stocks-today-bitcoin-silver-gold-september-26",
        "time_published": "20250926T170525",
        "authors": [
          "Piero Cingari"
        ],
        "summary": "Wall Street moved modestly higher by midday Friday, yet major indexes remain on pace to break a three-week winning streak. At midday, the S&P 500 was up 0.4% to 6,630, while the Nasdaq 100 gained 0.2% to 24,440. The Russell 2000, the benchmark small-cap index, rebounded 0.5%.",
        "banner_image": "https://cdn.benzinga.com/files/images/story/2025/09/26/Stock-exchange-building.jpeg?width=1200&height=800&fit=crop",
        "source": "Benzinga",
        "category_within_source": "News",
        "source_domain": "www.benzinga.com",
        "topics": [
          {
            "topic": "Economy - Monetary",
            "relevance_score": "0.158519"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.77141"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Finance",
            "relevance_score": "0.333333"
          }
        ],
        "overall_sentiment_score": 0.121508,
        "overall_sentiment_label": "Neutral",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.138066",
            "ticker_sentiment_score": "0.247837",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "AAPL",
            "relevance_score": "0.138066",
            "ticker_sentiment_score": "0.185714",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "INTC",
            "relevance_score": "0.272029",
            "ticker_sentiment_score": "0.342419",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "ORCL",
            "relevance_score": "0.138066",
            "ticker_sentiment_score": "0.057094",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "IVZ",
            "relevance_score": "0.069294",
            "ticker_sentiment_score": "0.192045",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "BA",
            "relevance_score": "0.138066",
            "ticker_sentiment_score": "0.053073",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "TSM",
            "relevance_score": "0.138066",
            "ticker_sentiment_score": "0.185714",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "CRYPTO:BTC",
            "relevance_score": "0.205807",
            "ticker_sentiment_score": "-0.231565",
            "ticker_sentiment_label": "Somewhat-Bearish"
          }
        ]
      },
      {
        "title": "Quantum Artificial Intelligence  ( AI )  Could Be the Next $10 Trillion Industry -- 2 Stocks to Own Now",
        "url": "https://www.fool.com/investing/2025/09/26/quantum-ai-could-be-the-next-10-trillion-industry/",
        "time_published": "20250926T161500",
        "authors": [
          "Adam Spatacco"
        ],
        "summary": "Quantum computing is swiftly becoming a new area of interest for artificial intelligence (AI) investors.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834073%2Fgettyimages-2156615862-11.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Real Estate & Construction",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          }
        ],
        "overall_sentiment_score": 0.349492,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "MSFT",
            "relevance_score": "0.058615",
            "ticker_sentiment_score": "0.120066",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "GOOG",
            "relevance_score": "0.174587",
            "ticker_sentiment_score": "0.084484",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.443626",
            "ticker_sentiment_score": "0.382084",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "IONQ",
            "relevance_score": "0.058615",
            "ticker_sentiment_score": "0.10099",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "RGTI",
            "relevance_score": "0.058615",
            "ticker_sentiment_score": "0.10099",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Why Is Nvidia  ( NVDA )  Down 1.4% Since Last Earnings Report?",
        "url": "https://www.zacks.com/stock/news/2757820/why-is-nvidia-nvda-down-14-since-last-earnings-report",
        "time_published": "20250926T153005",
        "authors": [
          "Zacks Equity Research"
        ],
        "summary": "Nvidia (NVDA) reported earnings 30 days ago. What's next for the stock? We take a look at earnings estimates for some clues.",
        "banner_image": "https://staticx-tuner.zacks.com/images/default_article_images/default196.jpg",
        "source": "Zacks Commentary",
        "category_within_source": "n/a",
        "source_domain": "www.zacks.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.967645"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.999955"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.142943,
        "overall_sentiment_label": "Neutral",
        "ticker_sentiment": [
          {
            "ticker": "MSFT",
            "relevance_score": "0.035189",
            "ticker_sentiment_score": "0.081426",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "GOOG",
            "relevance_score": "0.035189",
            "ticker_sentiment_score": "0.081426",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.372532",
            "ticker_sentiment_score": "0.159229",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Money manager Howard Rubin arrested on federal sex trafficking charges",
        "url": "https://www.cnbc.com/2025/09/26/howard-rubin-sex-trafficking-new-york-investment.html",
        "time_published": "20250926T152446",
        "authors": [],
        "summary": "Howard Rubin was sued in 2017 by two self-identified Playboy models and another model from Florida, who claimed they were beaten, sexually abused and raped.",
        "banner_image": "null",
        "source": "CNBC",
        "category_within_source": "Top News",
        "source_domain": "www.cnbc.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.158519"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": -0.159526,
        "overall_sentiment_label": "Somewhat-Bearish",
        "ticker_sentiment": [
          {
            "ticker": "PYPL",
            "relevance_score": "0.055236",
            "ticker_sentiment_score": "-0.040885",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.055236",
            "ticker_sentiment_score": "0.263986",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Consumers Splurge, Intel, GlobalFoundries, Lilly, Paccar, American Woodmark Benefit From New Tariffs - Apple  ( NASDAQ:AAPL ) ",
        "url": "https://www.benzinga.com/Opinion/25/09/47892647/consumers-splurge-intel-globalfoundries-lilly-paccar-american-woodmark-benefit-from-new-tariffs",
        "time_published": "20250926T150554",
        "authors": [
          "The Arora Report"
        ],
        "summary": "To gain an edge, this is what you need to know today. Please click here for a chart of SPDR S&P 500 ETF Trust ( NYSE: SPY ) which represents the benchmark stock market index S&P 500 ( SPX ) . 100% tariffs on pharmaceuticals unless the company is building a manufacturing plant in the U.S.",
        "banner_image": "https://www.benzinga.com/next-assets/images/schema-image-default.png",
        "source": "Benzinga",
        "category_within_source": "Markets",
        "source_domain": "www.benzinga.com",
        "topics": [
          {
            "topic": "Life Sciences",
            "relevance_score": "0.2"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.2"
          },
          {
            "topic": "Finance",
            "relevance_score": "0.2"
          },
          {
            "topic": "Economy - Monetary",
            "relevance_score": "0.158519"
          },
          {
            "topic": "Economy - Fiscal",
            "relevance_score": "0.158519"
          },
          {
            "topic": "Retail & Wholesale",
            "relevance_score": "0.2"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.999346"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.2"
          }
        ],
        "overall_sentiment_score": 0.185406,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "GOOG",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "0.101369",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "META",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "0.101369",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "0.101369",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "PCAR",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "0.0",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "AAPL",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "-0.267841",
            "ticker_sentiment_label": "Somewhat-Bearish"
          },
          {
            "ticker": "NVO",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "-0.009655",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "AMWD",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "0.0",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "IVZ",
            "relevance_score": "0.048919",
            "ticker_sentiment_score": "0.230091",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "MSFT",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "0.101369",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "TSLA",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "0.101369",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "LZB",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "0.039454",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "RH",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "0.039454",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "W",
            "relevance_score": "0.146025",
            "ticker_sentiment_score": "0.047674",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "LLY",
            "relevance_score": "0.146025",
            "ticker_sentiment_score": "-0.01155",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "CRYPTO:BTC",
            "relevance_score": "0.097655",
            "ticker_sentiment_score": "-0.192957",
            "ticker_sentiment_label": "Somewhat-Bearish"
          }
        ]
      },
      {
        "title": "Exploring The Competitive Space: NVIDIA Versus Industry Peers In Semiconductors & Semiconductor Equipment - NVIDIA  ( NASDAQ:NVDA ) ",
        "url": "https://www.benzinga.com/insights/news/25/09/47892271/exploring-the-competitive-space-nvidia-versus-industry-peers-in-semiconductors-amp-semiconductor-eq",
        "time_published": "20250926T150026",
        "authors": [
          "Benzinga Insights"
        ],
        "summary": "Amidst the fast-paced and highly competitive business environment of today, conducting comprehensive company analysis is essential for investors and industry enthusiasts.",
        "banner_image": "https://www.benzinga.com/next-assets/images/schema-image-default.png",
        "source": "Benzinga",
        "category_within_source": "Markets",
        "source_domain": "www.benzinga.com",
        "topics": [
          {
            "topic": "Earnings",
            "relevance_score": "0.95493"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.5855"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.271916,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.548003",
            "ticker_sentiment_score": "0.463612",
            "ticker_sentiment_label": "Bullish"
          }
        ]
      },
      {
        "title": "Chinese AI chip developer Moore Threads gets go-ahead for Shanghai IPO",
        "url": "https://www.scmp.com/tech/tech-trends/article/3327051/chinese-ai-chip-developer-moore-threads-gets-go-ahead-shanghai-ipo",
        "time_published": "20250926T145336",
        "authors": [
          "Ann Cao"
        ],
        "summary": "Moore Threads Technology, a Chinese developer of graphics processing units (GPUs), on Friday received approval for an initial public offering (IPO) on Shanghai's Nasdaq-style Star Market. Founded in 2020, Beijing-based Moore Threads plans to raise 8 billion yuan (US$1.1 billion) from its IPO, ...",
        "banner_image": "https://img.i-scmp.com/cdn-cgi/image/fit=contain,width=1024,format=auto/sites/default/files/d8/images/canvas/2025/09/26/0eef83d5-6320-46f9-9018-742396b9543a_965cbcd9.jpg",
        "source": "South China Morning Post",
        "category_within_source": "Business",
        "source_domain": "www.scmp.com",
        "topics": [
          {
            "topic": "IPO",
            "relevance_score": "0.838487"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.360215"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.136592,
        "overall_sentiment_label": "Neutral",
        "ticker_sentiment": [
          {
            "ticker": "AMD",
            "relevance_score": "0.279015",
            "ticker_sentiment_score": "0.074611",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.188193",
            "ticker_sentiment_score": "0.055979",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "TCTZF",
            "relevance_score": "0.094762",
            "ticker_sentiment_score": "0.06277",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Meet the Company Challenging Broadcom's AI Chip Dominance  ( Hint: It's Not Nvidia ) ",
        "url": "https://www.fool.com/investing/2025/09/26/meet-the-company-challenging-broadcoms-ai-chip/",
        "time_published": "20250926T135700",
        "authors": [
          "Harsh Chauhan"
        ],
        "summary": "This small AI company has the potential to take share away from Broadcom in custom AI chips.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834672%2Fperson-specs-integrated-circuit.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Earnings",
            "relevance_score": "0.999174"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.340397,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.215894",
            "ticker_sentiment_score": "0.198488",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "AVGO",
            "relevance_score": "0.726873",
            "ticker_sentiment_score": "0.566115",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "ASCCF",
            "relevance_score": "0.162802",
            "ticker_sentiment_score": "0.135194",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "MRVL",
            "relevance_score": "0.108958",
            "ticker_sentiment_score": "0.192836",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Alchip and Ayar Labs Unveil Co-Packaged Optics for AI Datacenter Scale-Up",
        "url": "https://www.benzinga.com/pressreleases/25/09/g47887552/alchip-and-ayar-labs-unveil-co-packaged-optics-for-ai-datacenter-scale-up",
        "time_published": "20250926T130000",
        "authors": [
          "Globe Newswire"
        ],
        "summary": "SAN JOSE, Calif., Sept. 26, 2025 ( GLOBE NEWSWIRE ) -- At the 2025 TSMC North America Open Innovation Platform® ( OIP ) Ecosystem Forum, Alchip Technologies, the high-performance ASIC leader, and Ayar Labs, a leader in co-packaged optics ( CPO ) for large-scale AI workloads, unveiled a CPO ...",
        "banner_image": "https://www.benzinga.com/next-assets/images/schema-image-default.png",
        "source": "Benzinga",
        "category_within_source": "General",
        "source_domain": "www.benzinga.com",
        "topics": [
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.684621"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.254361,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "HPQ",
            "relevance_score": "0.04531",
            "ticker_sentiment_score": "0.129706",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.04531",
            "ticker_sentiment_score": "0.129706",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "GFS",
            "relevance_score": "0.04531",
            "ticker_sentiment_score": "0.129706",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "ASCCF",
            "relevance_score": "0.04531",
            "ticker_sentiment_score": "0.145636",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "How To Trade SPY, Top Tech Stocks Using Technical Analysis",
        "url": "https://www.benzinga.com/Opinion/25/09/47887435/how-to-trade-spy-top-tech-stocks-using-technical-analysis-29",
        "time_published": "20250926T125001",
        "authors": [
          "RIPS"
        ],
        "summary": "Today's economic calendar for Friday, September 26, 2025, wraps up the week with several key releases. At 8:30 AM ET, the Core PCE Price Index for August will be the main focus, offering critical insight into inflation trends.",
        "banner_image": "https://www.benzinga.com/next-assets/images/schema-image-default.png",
        "source": "Benzinga",
        "category_within_source": "Trading",
        "source_domain": "www.benzinga.com",
        "topics": [
          {
            "topic": "Economy - Monetary",
            "relevance_score": "0.451494"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.214378"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": -0.009797,
        "overall_sentiment_label": "Neutral",
        "ticker_sentiment": [
          {
            "ticker": "MSFT",
            "relevance_score": "0.109289",
            "ticker_sentiment_score": "-0.074284",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.145364",
            "ticker_sentiment_score": "0.031081",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "AAPL",
            "relevance_score": "0.145364",
            "ticker_sentiment_score": "0.069375",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "TSLA",
            "relevance_score": "0.145364",
            "ticker_sentiment_score": "0.003845",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Why Iren Stock Surged Higher This Week",
        "url": "https://www.fool.com/investing/2025/09/26/why-iren-stock-surged-higher-this-week/",
        "time_published": "20250926T123327",
        "authors": [
          "Howard Smith"
        ],
        "summary": "Wall Street is lining up in support of Iren Limited stock.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F835133%2Fdata-center-campus.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Blockchain",
            "relevance_score": "0.158519"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.266143"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.175898,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.246582",
            "ticker_sentiment_score": "0.106919",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "SPGI",
            "relevance_score": "0.124809",
            "ticker_sentiment_score": "0.155407",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Is Micron Stock the Best Buy Now?",
        "url": "https://www.fool.com/investing/2025/09/26/is-micron-stock-the-best-buy-now/",
        "time_published": "20250926T122700",
        "authors": [
          "Manali Pradhan"
        ],
        "summary": "Investing in companies with strong growth drivers and a durable competitive advantage can be a smart way to build wealth over the long term.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834932%2Fperson-in-specs-looking-at-a-line-chart-on-a-laptop.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Earnings",
            "relevance_score": "0.998311"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.614606"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.314321,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "MU",
            "relevance_score": "0.075279",
            "ticker_sentiment_score": "0.217811",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.037681",
            "ticker_sentiment_score": "0.209718",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "AVGO",
            "relevance_score": "0.037681",
            "ticker_sentiment_score": "0.209718",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "TSM",
            "relevance_score": "0.037681",
            "ticker_sentiment_score": "0.201753",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "FOREX:AMD",
            "relevance_score": "0.329307",
            "ticker_sentiment_score": "0.20167",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "BlackBerry Q2 Earnings & Revenue Beat Estimates, Up Y/Y, Stock Rises",
        "url": "https://www.zacks.com/stock/news/2757472/blackberry-q2-earnings-revenue-beat-estimates-up-yy-stock-rises",
        "time_published": "20250926T121400",
        "authors": [
          "Zacks Investment Research"
        ],
        "summary": "BB posts Q2 earnings and revenue beat, lifts outlook on strong QNX growth and solid Secure Communications wins.",
        "banner_image": "https://staticx-tuner.zacks.com/images/articles/main/75/2558.jpg",
        "source": "Zacks Commentary",
        "category_within_source": "n/a",
        "source_domain": "www.zacks.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.161647"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "1.0"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.180172,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "BB",
            "relevance_score": "0.275091",
            "ticker_sentiment_score": "0.153992",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "RYCEF",
            "relevance_score": "0.035086",
            "ticker_sentiment_score": "0.154175",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "CRWV",
            "relevance_score": "0.070105",
            "ticker_sentiment_score": "-0.063629",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.070105",
            "ticker_sentiment_score": "0.230217",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "GWRE",
            "relevance_score": "0.070105",
            "ticker_sentiment_score": "0.043151",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Robotics Demand Rises: Will Jetson Thor Unlock a New Market for NVDA?",
        "url": "https://www.zacks.com/stock/news/2757470/robotics-demand-rises-will-jetson-thor-unlock-a-new-market-for-nvda",
        "time_published": "20250926T121300",
        "authors": [
          "Anirudha Bhagat"
        ],
        "summary": "NVIDIA sees robotics as its next growth frontier, with the new Jetson Thor platform poised to drive adoption across industries.",
        "banner_image": "https://staticx-tuner.zacks.com/images/articles/main/93/534.jpg",
        "source": "Zacks Commentary",
        "category_within_source": "n/a",
        "source_domain": "www.zacks.com",
        "topics": [
          {
            "topic": "Earnings",
            "relevance_score": "0.614606"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.275076,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "AMD",
            "relevance_score": "0.330876",
            "ticker_sentiment_score": "0.306165",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.65287",
            "ticker_sentiment_score": "0.454362",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "QCOM",
            "relevance_score": "0.202366",
            "ticker_sentiment_score": "0.121988",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "A Healthcare Debate: Progyny vs. Hims & Hers",
        "url": "https://www.fool.com/investing/2025/09/26/a-healthcare-debate-progyny-vs-hims-hers/",
        "time_published": "20250926T120500",
        "authors": [
          "Motley Fool Staff"
        ],
        "summary": "Motley Fool analysts take a look.",
        "banner_image": "https://g.foolcdn.com/editorial/images/835056/the-great-rule-breakers-healthcare-debate-progyny-or-hims-hers.jpg",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Life Sciences",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Retail & Wholesale",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.999994"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.684621"
          }
        ],
        "overall_sentiment_score": 0.187507,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NFLX",
            "relevance_score": "0.012725",
            "ticker_sentiment_score": "0.13868",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.164253",
            "ticker_sentiment_score": "0.124775",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "CMG",
            "relevance_score": "0.012725",
            "ticker_sentiment_score": "0.13868",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "INTC",
            "relevance_score": "0.139265",
            "ticker_sentiment_score": "0.11053",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "PGNY",
            "relevance_score": "0.025447",
            "ticker_sentiment_score": "-0.069755",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Top-Performing ETF Areas of Q3",
        "url": "https://www.zacks.com/stock/news/2757464/top-performing-etf-areas-of-q3",
        "time_published": "20250926T120000",
        "authors": [
          "Sanghamitra Saha"
        ],
        "summary": "Small caps led Q3 gains, while other standout ETF areas are Bitcoin mining (WGMI, MNRS), cannabis (MSOS, WEED), Ethereum (ETH, ETHW) and rare earths (REMX).",
        "banner_image": "https://staticx-tuner.zacks.com/images/articles/main/bd/484.jpg",
        "source": "Zacks Commentary",
        "category_within_source": "n/a",
        "source_domain": "www.zacks.com",
        "topics": [
          {
            "topic": "Economy - Monetary",
            "relevance_score": "0.451494"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.976671"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Energy & Transportation",
            "relevance_score": "0.5"
          },
          {
            "topic": "Blockchain",
            "relevance_score": "0.158519"
          }
        ],
        "overall_sentiment_score": 0.133123,
        "overall_sentiment_label": "Neutral",
        "ticker_sentiment": [
          {
            "ticker": "BABA",
            "relevance_score": "0.053509",
            "ticker_sentiment_score": "-0.04579",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.053509",
            "ticker_sentiment_score": "-0.04579",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "LAC",
            "relevance_score": "0.106778",
            "ticker_sentiment_score": "0.121633",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "CRYPTO:BTC",
            "relevance_score": "0.159569",
            "ticker_sentiment_score": "0.125236",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "CRYPTO:ETH",
            "relevance_score": "0.262805",
            "ticker_sentiment_score": "0.180474",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "The AI Stock Market Bubble: Why It Hasn't Burst Yet and What's Keeping Valuations High - NVIDIA  ( NASDAQ:NVDA ) ",
        "url": "https://www.benzinga.com/opinion/25/09/47885908/the-ai-stock-market-bubble-why-it-hasnt-burst-yet-and-whats-keeping-valuations-high",
        "time_published": "20250926T111602",
        "authors": [
          "Luis Flavio"
        ],
        "summary": "As AI stocks continue to defy gravity, investors are grappling with a fundamental question: Is this another dot-com bubble waiting to burst, or are we witnessing the birth of a new market paradigm? The answer, according to market analysts, lies somewhere in between. The case for an AI bubble is ...",
        "banner_image": "https://www.benzinga.com/next-assets/images/schema-image-default.png",
        "source": "Benzinga",
        "category_within_source": "Markets",
        "source_domain": "www.benzinga.com",
        "topics": [
          {
            "topic": "Economy - Monetary",
            "relevance_score": "0.451494"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.977154"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.858979"
          }
        ],
        "overall_sentiment_score": 0.175225,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.095771",
            "ticker_sentiment_score": "0.003216",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "4 Reasons for Q4 to Start on a Strong Note: ETFs to Play",
        "url": "https://www.zacks.com/stock/news/2757448/4-reasons-for-q4-to-start-on-a-strong-note-etfs-to-play",
        "time_published": "20250926T111600",
        "authors": [
          "Sanghamitra Saha"
        ],
        "summary": "Bet on Wall Street Q4 tailwinds -- strong GDP data, holiday sales, AI boom & earnings growth. These have put the spotlight on IWM, XLF, XLY & XLE.",
        "banner_image": "https://staticx-tuner.zacks.com/images/articles/main/50/348.jpg",
        "source": "Zacks Commentary",
        "category_within_source": "n/a",
        "source_domain": "www.zacks.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.999862"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.769861"
          },
          {
            "topic": "Real Estate & Construction",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.270551,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "BABA",
            "relevance_score": "0.041039",
            "ticker_sentiment_score": "0.040421",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "CRWV",
            "relevance_score": "0.041039",
            "ticker_sentiment_score": "0.128857",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.122685",
            "ticker_sentiment_score": "0.048168",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "IONQ",
            "relevance_score": "0.041039",
            "ticker_sentiment_score": "0.031859",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Prediction: This Will Be Nvidia's Stock Price in 2026",
        "url": "https://www.fool.com/investing/2025/09/26/prediction-this-will-be-nvidias-stock-price-in-202/",
        "time_published": "20250926T104500",
        "authors": [
          "Harsh Chauhan"
        ],
        "summary": "Nvidia stock has witnessed some volatility in 2025, but it has still managed to deliver respectable gains to investors.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834907%2Fperson-smiling-computer-charts.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.980922"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.365926"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.236339,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "MSFT",
            "relevance_score": "0.055881",
            "ticker_sentiment_score": "0.059027",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "CRWV",
            "relevance_score": "0.055881",
            "ticker_sentiment_score": "0.059027",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "GOOG",
            "relevance_score": "0.055881",
            "ticker_sentiment_score": "0.059027",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.673559",
            "ticker_sentiment_score": "0.451651",
            "ticker_sentiment_label": "Bullish"
          }
        ]
      },
      {
        "title": "The Best Stocks to Invest $50,000 in Right Now",
        "url": "https://www.fool.com/investing/2025/09/26/the-best-stocks-to-invest-50000-in-right-now/",
        "time_published": "20250926T103500",
        "authors": [
          "John Ballard"
        ],
        "summary": "These companies are the top dogs in chips, physical AI, and software.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834677%2Fai-computer-chip.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Earnings",
            "relevance_score": "0.891286"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.365926"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.292786,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "OPTGF",
            "relevance_score": "0.125025",
            "ticker_sentiment_score": "0.118324",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.363093",
            "ticker_sentiment_score": "0.199958",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "TSLA",
            "relevance_score": "0.28648",
            "ticker_sentiment_score": "0.250578",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Better Artificial Intelligence Stock: Palantir vs. Nvidia",
        "url": "https://www.fool.com/investing/2025/09/26/better-artificial-intelligence-stock-palantir-vs-n/",
        "time_published": "20250926T103000",
        "authors": [
          "Robert Izquierdo"
        ],
        "summary": "Both tech companies are crushing it in AI, but one is a better bet for investors, thanks to a key factor.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834686%2Fai_robot_watching_stocks_rise-gettyimages-1389207041-1201x800-9b9f185.png&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.266143"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.980716"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.337341,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.607595",
            "ticker_sentiment_score": "0.468323",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "PLTR",
            "relevance_score": "0.104683",
            "ticker_sentiment_score": "0.223022",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Should TCW Transform 500 ETF  ( VOTE )  Be on Your Investing Radar?",
        "url": "https://www.zacks.com/stock/news/2757420/should-tcw-transform-500-etf-vote-be-on-your-investing-radar",
        "time_published": "20250926T102002",
        "authors": [
          "Zacks Equity Research"
        ],
        "summary": "Style Box ETF report for VOTE ...",
        "banner_image": "https://staticx-tuner.zacks.com/images/default_article_images/default158.jpg",
        "source": "Zacks Commentary",
        "category_within_source": "n/a",
        "source_domain": "www.zacks.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "1.0"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Finance",
            "relevance_score": "0.333333"
          }
        ],
        "overall_sentiment_score": 0.180334,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "MSFT",
            "relevance_score": "0.141726",
            "ticker_sentiment_score": "0.136424",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.141726",
            "ticker_sentiment_score": "0.136424",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "AAPL",
            "relevance_score": "0.141726",
            "ticker_sentiment_score": "0.136424",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "MORN",
            "relevance_score": "0.071145",
            "ticker_sentiment_score": "0.0",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Is SoFi Select 500 ETF  ( SFY )  a Strong ETF Right Now?",
        "url": "https://www.zacks.com/stock/news/2757428/is-sofi-select-500-etf-sfy-a-strong-etf-right-now",
        "time_published": "20250926T102002",
        "authors": [
          "Zacks Equity Research"
        ],
        "summary": "Smart Beta ETF report for ...",
        "banner_image": "https://staticx-tuner.zacks.com/images/default_article_images/default40.jpg",
        "source": "Zacks Commentary",
        "category_within_source": "n/a",
        "source_domain": "www.zacks.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.997874"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Finance",
            "relevance_score": "0.333333"
          }
        ],
        "overall_sentiment_score": 0.297847,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "MSFT",
            "relevance_score": "0.1331",
            "ticker_sentiment_score": "0.131966",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.1331",
            "ticker_sentiment_score": "0.131966",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "AVGO",
            "relevance_score": "0.1331",
            "ticker_sentiment_score": "0.131966",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "IVZ",
            "relevance_score": "0.1331",
            "ticker_sentiment_score": "0.233719",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Should Vanguard Growth ETF  ( VUG )  Be on Your Investing Radar?",
        "url": "https://www.zacks.com/stock/news/2757421/should-vanguard-growth-etf-vug-be-on-your-investing-radar",
        "time_published": "20250926T102002",
        "authors": [
          "Zacks Equity Research"
        ],
        "summary": "Style Box ETF report for VUG ...",
        "banner_image": "https://staticx-tuner.zacks.com/images/default_article_images/default320.jpg",
        "source": "Zacks Commentary",
        "category_within_source": "n/a",
        "source_domain": "www.zacks.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.999999"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.310843"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Finance",
            "relevance_score": "0.333333"
          }
        ],
        "overall_sentiment_score": 0.298442,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "MSFT",
            "relevance_score": "0.126784",
            "ticker_sentiment_score": "0.128889",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.126784",
            "ticker_sentiment_score": "0.128889",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "AAPL",
            "relevance_score": "0.126784",
            "ticker_sentiment_score": "0.128889",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "IVZ",
            "relevance_score": "0.126784",
            "ticker_sentiment_score": "0.119029",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Billionaires Are Buying These 3 Unstoppable AI Stocks Shaping the Future of Technology",
        "url": "https://www.fool.com/investing/2025/09/26/billionaires-are-buying-3-unstoppable-ai-stocks/",
        "time_published": "20250926T100000",
        "authors": [
          "Keithen Drury"
        ],
        "summary": "Artificial intelligence investing still has a long growth runway.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F832967%2Ftwo-people-in-suits-looking-at-data.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Retail & Wholesale",
            "relevance_score": "0.5"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.996023"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.684621"
          }
        ],
        "overall_sentiment_score": 0.295654,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.622414",
            "ticker_sentiment_score": "0.494322",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "AMZN",
            "relevance_score": "0.365294",
            "ticker_sentiment_score": "0.312006",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "TSM",
            "relevance_score": "0.107978",
            "ticker_sentiment_score": "0.234087",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "BigBear.ai vs. SoundHound AI: What's the Better Artificial Intelligence  ( AI )  Stock to Buy Today?",
        "url": "https://www.fool.com/investing/2025/09/26/bigbearai-holdings-vs-soundhound-ai-whats-the-bett/",
        "time_published": "20250926T095000",
        "authors": [
          "David Jagielski"
        ],
        "summary": "These two tech stocks have been popular investments with retail investors and they're both up more than 200% in the past 12 months.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834100%2Fpeople-reviewing-a-report-on-a-computer.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.87644"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.360215"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.248139,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.061473",
            "ticker_sentiment_score": "-0.00902",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "PLTR",
            "relevance_score": "0.061473",
            "ticker_sentiment_score": "0.203132",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "SOUN",
            "relevance_score": "0.30021",
            "ticker_sentiment_score": "0.200934",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Billionaire David Tepper Is Loading Up on These 3 Artificial Intelligence  ( AI )  Stocks That Have Increased 158% or More",
        "url": "https://www.fool.com/investing/2025/09/26/billionaire-david-tepper-is-loading-up-on-these-3/",
        "time_published": "20250926T094500",
        "authors": [
          "Keithen Drury"
        ],
        "summary": "Following the smart money in AI is a wise thing to do.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F832961%2Fconsultant-explanining-in-a-meeting-room-with-a-laptop.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Retail & Wholesale",
            "relevance_score": "0.5"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.98396"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.360215"
          }
        ],
        "overall_sentiment_score": 0.338416,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "AMD",
            "relevance_score": "0.055621",
            "ticker_sentiment_score": "0.21096",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.324495",
            "ticker_sentiment_score": "0.329927",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "AVGO",
            "relevance_score": "0.055621",
            "ticker_sentiment_score": "0.21096",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "AMZN",
            "relevance_score": "0.423251",
            "ticker_sentiment_score": "0.273203",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Want to Invest in Quantum Computing? 3 Stocks That Are Great Buys Right Now",
        "url": "https://www.fool.com/investing/2025/09/26/want-to-invest-in-quantum-computing-3-stocks-that/",
        "time_published": "20250926T093000",
        "authors": [
          "Keithen Drury"
        ],
        "summary": "Taking a balanced approach to quantum computing investing is a smart idea.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F831516%2Fimage-of-quantum-computing.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.990999"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Real Estate & Construction",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.333333"
          }
        ],
        "overall_sentiment_score": 0.255823,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "GOOG",
            "relevance_score": "0.093108",
            "ticker_sentiment_score": "0.117485",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.479954",
            "ticker_sentiment_score": "0.431304",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "IONQ",
            "relevance_score": "0.230017",
            "ticker_sentiment_score": "0.098423",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "3 Leading Tech Stocks to Buy in 2025",
        "url": "https://www.fool.com/investing/2025/09/26/3-leading-tech-stocks-to-buy-in-2025/",
        "time_published": "20250926T092000",
        "authors": [
          "Justin Pope"
        ],
        "summary": "These companies are key players in artificial intelligence and should continue to deliver through 2025 and beyond.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834549%2Fkeyboard-tech-idea.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.999365"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.682689"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.237812,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "IBM",
            "relevance_score": "0.357049",
            "ticker_sentiment_score": "0.179657",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.105372",
            "ticker_sentiment_score": "0.113888",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "TSM",
            "relevance_score": "0.105372",
            "ticker_sentiment_score": "0.101484",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "2 Breakout Growth Stocks You Can Buy and Hold for the Next Decade",
        "url": "https://www.fool.com/investing/2025/09/26/breakout-growth-stocks-buy-and-hold-nvda-meta/",
        "time_published": "20250926T090500",
        "authors": [
          "Geoffrey Seiler"
        ],
        "summary": "Nvidia and Meta Platforms are well positioned to be long-term winners.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834561%2Fgettyimages-2078917109.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.77141"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.360215"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.339582,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "META",
            "relevance_score": "0.250386",
            "ticker_sentiment_score": "0.427881",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.423504",
            "ticker_sentiment_score": "0.351703",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "AVGO",
            "relevance_score": "0.063594",
            "ticker_sentiment_score": "0.1241",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Meet the Newest Artificial Intelligence  ( AI )  Stock to Join Nvidia, Microsoft, and Apple in the $3 Trillion Club",
        "url": "https://www.fool.com/investing/2025/09/26/artificial-intelligence-ai-stock-nvda-msft-goog/",
        "time_published": "20250926T090000",
        "authors": [
          "Adam Levy"
        ],
        "summary": "It might not take very much longer for it to reach $4 trillion.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834499%2Fgettyimages-rocket-chart-higher.jpeg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.980922"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.875462"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.115178,
        "overall_sentiment_label": "Neutral",
        "ticker_sentiment": [
          {
            "ticker": "MSFT",
            "relevance_score": "0.097259",
            "ticker_sentiment_score": "0.02889",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "GOOG",
            "relevance_score": "0.240014",
            "ticker_sentiment_score": "0.023942",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.097259",
            "ticker_sentiment_score": "0.02889",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "AAPL",
            "relevance_score": "0.286082",
            "ticker_sentiment_score": "-0.043724",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Is Nvidia Stock an Undervalued Artificial Intelligence  ( AI )  Stock to Buy?",
        "url": "https://www.fool.com/investing/2025/09/26/is-nvidia-stock-an-undervalued-artificial-intellig/",
        "time_published": "20250926T090000",
        "authors": [
          "CFA",
          "Parkev Tatevosian"
        ],
        "summary": "Nvidia's share price has increased so significantly in recent years that investors are concerned it is overvalued.",
        "banner_image": "https://g.foolcdn.com/avatar/2046799619/large.ashx",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": -0.095459,
        "overall_sentiment_label": "Neutral",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.798255",
            "ticker_sentiment_score": "-0.329138",
            "ticker_sentiment_label": "Somewhat-Bearish"
          }
        ]
      },
      {
        "title": "What AMD Shareholders Should Know About Recent Updates",
        "url": "https://www.fool.com/investing/2025/09/26/what-amd-shareholders-should-know-about-recent-upd/",
        "time_published": "20250926T090000",
        "authors": [
          "Jose Najarro"
        ],
        "summary": "Advanced Micro Devices' competition heats up after a recent partnership between Nvidia and Intel.",
        "banner_image": "https://g.foolcdn.com/editorial/images/835090/amd-headquarters-santa-clara-with-amd-logo-on-building_amd_advance.jpg",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.360215"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": -0.111522,
        "overall_sentiment_label": "Neutral",
        "ticker_sentiment": [
          {
            "ticker": "AMD",
            "relevance_score": "0.719473",
            "ticker_sentiment_score": "-0.330896",
            "ticker_sentiment_label": "Somewhat-Bearish"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.719473",
            "ticker_sentiment_score": "-0.330896",
            "ticker_sentiment_label": "Somewhat-Bearish"
          },
          {
            "ticker": "GD",
            "relevance_score": "0.170878",
            "ticker_sentiment_score": "0.116833",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "INTC",
            "relevance_score": "0.719473",
            "ticker_sentiment_score": "-0.330896",
            "ticker_sentiment_label": "Somewhat-Bearish"
          }
        ]
      },
      {
        "title": "Nvidia-OpenAI Deal Sparks 'Circular' Investment Concerns, Says Analyst: 'Incremental Worries Around...' - NVIDIA  ( NASDAQ:NVDA ) , Oracle  ( NYSE:ORCL ) ",
        "url": "https://www.benzinga.com/markets/tech/25/09/47884026/nvidia-openai-deal-sparks-circular-investment-concerns-says-analyst-incremental-worries-around",
        "time_published": "20250926T085936",
        "authors": [
          "Namrata Sen"
        ],
        "summary": "Nvidia Corporation's ( NASDAQ: NVDA ) recent investment in OpenAI has sparked investor concerns that the startup might buy Nvidia chips, creating a \"circular\" investment loop and raising questions about the move's rationale and potential impact on Nvidia's stock.",
        "banner_image": "https://cdn.benzinga.com/files/images/story/2025/09/26/In-This-Photo-The-Logo-Of-Nvidia-With-Th.jpeg?width=1200&height=800&fit=crop",
        "source": "Benzinga",
        "category_within_source": "Markets",
        "source_domain": "www.benzinga.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.99793"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.108179"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Finance",
            "relevance_score": "0.333333"
          }
        ],
        "overall_sentiment_score": 0.154479,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "CRWV",
            "relevance_score": "0.087185",
            "ticker_sentiment_score": "0.101413",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.874686",
            "ticker_sentiment_score": "0.257829",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "ORCL",
            "relevance_score": "0.173333",
            "ticker_sentiment_score": "-0.05452",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "BAC",
            "relevance_score": "0.087185",
            "ticker_sentiment_score": "0.079447",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "1 Spectacular Semiconductor Stock  ( Besides Nvidia and AMD )  to Buy Hand Over Fist Before 2026",
        "url": "https://www.fool.com/investing/2025/09/26/1-spectacular-semiconductor-stock-besides-nvidia-a/",
        "time_published": "20250926T085900",
        "authors": [
          "Anthony Di Pizio"
        ],
        "summary": "Despite broad gains over the last few years, investors can still find value in the semiconductor space.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834920%2Fa-digital-render-of-a-circuit-board-with-a-chip-in-the-center-inscribed-with-the-letters-ai.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Earnings",
            "relevance_score": "0.999696"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.161647"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "1.0"
          }
        ],
        "overall_sentiment_score": 0.205968,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "AMD",
            "relevance_score": "0.256179",
            "ticker_sentiment_score": "0.159623",
            "ticker_sentiment_label": "Somewhat-Bullish"
          },
          {
            "ticker": "MU",
            "relevance_score": "0.104002",
            "ticker_sentiment_score": "0.097783",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.305058",
            "ticker_sentiment_score": "0.183298",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      },
      {
        "title": "Prediction: 2 Stocks That Will Be Worth More Than BigBear.ai 5 Years From Now",
        "url": "https://www.fool.com/investing/2025/09/26/prediction-2-stocks-worth-more-bigbear-ai/",
        "time_published": "20250926T084200",
        "authors": [
          "Keith Speights"
        ],
        "summary": "BigBear.ai is bigger than both of these AI-focused companies now. That could change.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834947%2Fman-pointing-to-ai-on-display.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Life Sciences",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.333333"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.214378"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.333333"
          }
        ],
        "overall_sentiment_score": 0.215736,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "NVDA",
            "relevance_score": "0.114137",
            "ticker_sentiment_score": "0.121048",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "RXRX",
            "relevance_score": "0.114137",
            "ticker_sentiment_score": "0.085474",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "DBD",
            "relevance_score": "0.384608",
            "ticker_sentiment_score": "0.35133",
            "ticker_sentiment_label": "Bullish"
          },
          {
            "ticker": "SNY",
            "relevance_score": "0.114137",
            "ticker_sentiment_score": "0.083173",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Prediction: 2 Artificial Intelligence  ( AI )  Stocks That Will Be Worth More Than Palantir By the End of 2026",
        "url": "https://www.fool.com/investing/2025/09/26/artificial-intelligence-ai-stocks-worth-palantir/",
        "time_published": "20250926T081500",
        "authors": [
          "Adam Levy"
        ],
        "summary": "There's still a ton of growth potential for these two industry giants.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834565%2Fgetty-images-investing-screen-analysis-investor-growth-stocks-1200x800-5b2df79.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.995077"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.955357"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.185839,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "BABA",
            "relevance_score": "0.121037",
            "ticker_sentiment_score": "-0.009512",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.040484",
            "ticker_sentiment_score": "-0.108544",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "PDD",
            "relevance_score": "0.040484",
            "ticker_sentiment_score": "0.0",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "PLTR",
            "relevance_score": "0.080865",
            "ticker_sentiment_score": "0.065088",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "A $450 Billion Opportunity: Is Serve Robotics Stock a Buy Right Now?",
        "url": "https://www.fool.com/investing/2025/09/26/a-450-billion-opportunity-serve-robotics-buy-now/",
        "time_published": "20250926T081100",
        "authors": [
          "Anthony Di Pizio"
        ],
        "summary": "Serve Robotics' stock plunged after Nvidia sold its stake in the company at the end of 2024, but the company has an enormous long-term opportunity.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834904%2Fa-pair-of-autonomous-food-delivery-robots-waiting-on-the-sidewalk.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Financial Markets",
            "relevance_score": "0.989041"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          },
          {
            "topic": "Earnings",
            "relevance_score": "0.992549"
          },
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.142495,
        "overall_sentiment_label": "Neutral",
        "ticker_sentiment": [
          {
            "ticker": "SERV",
            "relevance_score": "0.180124",
            "ticker_sentiment_score": "0.003073",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.267315",
            "ticker_sentiment_score": "0.0",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "UBER",
            "relevance_score": "0.135602",
            "ticker_sentiment_score": "0.0826",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "PLTR",
            "relevance_score": "0.045396",
            "ticker_sentiment_score": "-0.142145",
            "ticker_sentiment_label": "Neutral"
          }
        ]
      },
      {
        "title": "Don't Overthink AI -- ETFs Could Be the Safest Long-Term Play",
        "url": "https://www.fool.com/investing/2025/09/26/dont-overthink-ai-etfs-could-be-the-safest-long-te/",
        "time_published": "20250926T081000",
        "authors": [
          "Adria Cimino"
        ],
        "summary": "This is a way to immediately jump into the AI growth story.",
        "banner_image": "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Feditorial%2Fimages%2F834052%2Fgettyimages-1323758599.jpg&op=resize&w=700",
        "source": "Motley Fool",
        "category_within_source": "n/a",
        "source_domain": "www.fool.com",
        "topics": [
          {
            "topic": "Technology",
            "relevance_score": "0.5"
          },
          {
            "topic": "Financial Markets",
            "relevance_score": "0.998932"
          },
          {
            "topic": "Manufacturing",
            "relevance_score": "0.5"
          }
        ],
        "overall_sentiment_score": 0.318601,
        "overall_sentiment_label": "Somewhat-Bullish",
        "ticker_sentiment": [
          {
            "ticker": "META",
            "relevance_score": "0.05654",
            "ticker_sentiment_score": "0.101922",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "NVDA",
            "relevance_score": "0.112797",
            "ticker_sentiment_score": "0.117832",
            "ticker_sentiment_label": "Neutral"
          },
          {
            "ticker": "AAPL",
            "relevance_score": "0.05654",
            "ticker_sentiment_score": "0.156957",
            "ticker_sentiment_label": "Somewhat-Bullish"
          }
        ]
      }
    ]
  }
}
    

mock_websearch = {
  "output": {
    "query": "Latest analyst ratings and consensus price target for NVDA",
    "follow_up_questions": "null",
    "answer": "null",
    "images": [],
    "results": [
      {
        "url": "https://www.benzinga.com/quote/NVDA/analyst-ratings",
        "title": "NVIDIA Analyst Ratings and Price Targets | NASDAQ:NVDA",
        "content": "NVIDIA Corp has a consensus price target of $211.18 based on the ratings of 34 analysts. The high is $250 issued by Loop Capital on June 25, 2025.",
        "score": 0.9589434,
        "raw_content": "null"
      },
      {
        "url": "https://www.marketbeat.com/stocks/NASDAQ/NVDA/forecast/",
        "title": "NVIDIA (NVDA) Stock Forecast and Price Target 2025 - MarketBeat",
        "content": "NVDA Analyst Ratings Over Time ; Consensus Price Target, $209.82, $194.31, $175.78, $142.10 ; Forecasted Upside, 17.75% Upside, 7.00% Upside, 11.43% Upside, 14.56",
        "score": 0.9400512,
        "raw_content": "null"
      },
      {
        "url": "https://stockanalysis.com/stocks/nvda/forecast/",
        "title": "NVIDIA (NVDA) Stock Forecast & Analyst Price Targets",
        "content": "Stock Price Forecast​​ The 42 analysts that cover NVIDIA stock have a consensus rating of \"Strong Buy\" and an average price target of $205.31, which forecasts a",
        "score": 0.9385817,
        "raw_content": "null"
      },
      {
        "url": "https://www.tipranks.com/stocks/nvda/forecast",
        "title": "Nvidia (NVDA) Stock Forecast, Price Targets and Analysts Predictions",
        "content": "Nvidia has a consensus rating of Strong Buy which is based on 37 buy ratings, 2 hold ratings and 1 sell ratings. The average price target for Nvidia is 212.00.",
        "score": 0.93295,
        "raw_content": "null"
      },
      {
        "url": "https://www.investing.com/equities/nvidia-corp-consensus-estimates",
        "title": "Nvidia (NVDA) Stock Forecast & Price Target - Investing.com",
        "content": "According to projections from 56 analysts, the average 12-month price target for NVIDIA is 213.18357, with a high estimate of 270 and a low estimate of 100.",
        "score": 0.8846886,
        "raw_content": "null"
      },
      {
        "url": "https://www.marketwatch.com/investing/stock/nvda/analystestimates",
        "title": "NVIDIA Corp. Analyst Estimates - NVDA - MarketWatch",
        "content": "Average Recommendation, Buy. Average Target Price, 218.28. Number Of Ratings, 66. FY Report Date, 1/2026. Last Quarter's Earnings, 1.05.",
        "score": 0.85624856,
        "raw_content": "null"
      },
      {
        "url": "https://www.marketscreener.com/quote/stock/NVIDIA-CORPORATION-57355629/consensus/",
        "title": "NVIDIA Corporation: Target Price Consensus and Analysts ...",
        "content": "Analysts' Consensus ; Mean consensus. BUY ; Number of Analysts. 63 ; Last Close Price. 177.69USD ; Average target price. 213.18USD ; Spread / Average Target. +19.97%.",
        "score": 0.85421735,
        "raw_content": "null"
      },
      {
        "url": "https://www.cnn.com/markets/stocks/NVDA",
        "title": "NVDA Stock Quote Price and Forecast - CNN",
        "content": "66 analyst ratings. buy 91%; hold 8%; sell 2%. We're sorry, but this information is temporarily unavailable. 1-year stock price forecast. High",
        "score": 0.67706895,
        "raw_content": "null"
      },
      {
        "url": "https://www.wsj.com/market-data/quotes/NVDA/research-ratings?gaa_at=eafs&gaa_n=ASWzDAiIXbosAj41JG_xL9DCuVWeFVevR16RVU_wwE644KdKVGK8TWRARczo&gaa_ts=68d790cf&gaa_sig=weQ68DtP4dPaHeSS1hBQa85pnYkCY4P7LFhTKo1ShtYNLrxMBRqJIVhGPPlsdWbsK8PNU34P2vEcVRrGHQCAag%3D%3D",
        "title": "NVDA | NVIDIA Corp. Analyst Estimates & Ratings - WSJ",
        "content": "NVIDIA Corp. analyst ratings, historical stock prices, earnings estimates & actuals. NVDA updated stock price target summary.",
        "score": 0.65861565,
        "raw_content": "null"
      },
      {
        "url": "https://finance.yahoo.com/quote/NVDA/analysis/",
        "title": "NVIDIA Corporation (NVDA) Analyst Ratings, Estimates & Forecasts",
        "content": "See NVIDIA Corporation (NVDA) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades.",
        "score": 0.55912215,
        "raw_content": "null"
      }
    ],
    "response_time": 1.27,
    "request_id": "8e74a82e-b577-4e8d-b352-d3f56ceb8aa0"
  }
}
    

mock_analyze_financials =  """
**NVIDIA Corporation - Financial-Health Snapshot**  
*(All figures are as of the latest filing; sector-level benchmarks are drawn from the broader U.S. Technology industry, where average P/E ≈ 25-30, forward-P/E ≈ 22-28, PEG ≈ 1.0, P/B ≈ 6-8, and dividend yields are typically 0.5-2% for mature tech names.)*  

---

## 1. Valuation  

| Metric | NVIDIA | Typical Tech-Sector Range | Interpretation |
|--------|--------|---------------------------|----------------|
| **Current P/E** | **50.48** | 25-30 (mid-range) | **High** - the market is pricing earnings at roughly double the sector median, reflecting expectations of outsized future growth. |
| **Forward P/E** | **39.37** | 22-28 | Still **elevated**, but the decline from current P/E signals that analysts expect earnings to accelerate enough to narrow the gap. |
| **PEG Ratio** | **1.317** | ~1.0 (fair value) | Slightly **above** the “fair-value” benchmark, implying the current price may be a bit rich relative to the 56 % YoY revenue growth. |
| **Price-to-Book (P/B)** | **43.03** | 6-8 | **Very high** - investors are paying a premium for intangible assets (IP, brand, growth potential) far above the book value. |
| **Price-to-Sales (P/S)** - not supplied, but given the market cap (~$4.3 T) and 2023 revenue (~$26 B), implied P/S ≈ 165, which is **extremely lofty** for any tech firm. |

**Valuation Take-away**  
- The multiples are **substantially above** sector averages, indicating that the market already baked-in strong growth expectations.  
- The forward-P/E compression and a PEG modestly above 1 suggest the stock may be **fairly valued** if the company sustains its current growth trajectory, but it remains **overvalued** relative to historical tech norms.

---

## 2. Profitability  

| Metric | NVIDIA | Tech-Sector Context | Insight |
|--------|--------|----------------------|---------|
| **Operating Margin** | **60.8 %** | 20-30 % (typical) | **Exceptional** - reflects a highly scalable, high-margin business (AI chips, data-center GPUs). |
| **Profit Margin** | **52.4 %** | 15-25 % | **Outstanding** - net earnings are more than half of revenue, far above peers. |
| **Return on Equity (ROE)** | **109 %** (1.094) | 15-20 % | **Astronomical** - indicates the firm generates more than a dollar of profit for every dollar of equity, a result of both high margins and a relatively modest equity base (large market cap vs. book). |
| **EPS** | **$3.52** | N/A (absolute) | Growing EPS (see trend below) underpins the high P/E. |

**Profitability Take-away**  
- NVIDIA's margins and ROE are **among the best in the technology universe**, confirming that the premium valuation is supported by genuine earnings power.  
- The sustainability of these margins hinges on continued demand for AI-centric hardware and the ability to protect pricing power against emerging competition.

---

## 3. Growth Trends  

| Metric | NVIDIA | Industry Lens | Assessment |
|--------|--------|---------------|------------|
| **Quarterly Revenue Growth YoY** | **55.6 %** | Tech revenue growth averages 10-20 %; AI-focused peers (e.g., AMD) are in the 30-40 % range. | **Rapid acceleration** - revenue is expanding at a pace that far outstrips the broader sector. |
| **Quarterly Earnings Growth YoY** | **61.2 %** | Similar to revenue, most large-cap tech firms post 15-25 % earnings growth. | **Strong earnings acceleration** - earnings are growing even faster than revenue, indicating margin expansion. |
| **Revenue per Share** - not disclosed, but implied by high EPS and revenue growth, it is also climbing sharply. | | | **Accelerating** - both top-line and bottom-line metrics are rising at >50 % YoY, a clear sign of a growth engine still in expansion mode. |
| **Industry Trend** | AI-hardware demand is exploding, driven by data-center, generative-AI, and autonomous-vehicle workloads. | The sector is shifting from commodity GPUs to specialized AI accelerators, favoring firms with leading architectures (e.g., NVIDIA's H100, GH200). | NVIDIA is **well-positioned** to capture a large share of this secular shift. |

**Growth Take-away**  
- Growth is **accelerating**, not merely stable. The combination of >50 % YoY revenue and earnings growth places NVIDIA ahead of most technology peers.  
- If the AI spending wave continues, the growth rates could remain elevated for several years, but they are also **sensitive to macro-level AI-capex cycles**.

---

## 4. Financial Strength  

| Metric | NVIDIA | Context | Observation |
|--------|--------|---------|-------------|
| **Dividend Yield** | **0.02 %** | Most mature tech firms pay 0.5-2 %; many high-growth names pay nothing. | **Near-zero payout** - the company is reinvesting virtually all cash back into the business, consistent with a growth-oriented capital allocation policy. |
| **Dividend per Share** | Negligible | — | No meaningful dividend stream to assess sustainability. |
| **Book Value per Share** | Implied by P/B of 43 → Book ≈ $4.5 (approx.) | Low relative to market price; typical tech P/B 6-8. | The market values intangible assets (IP, brand, ecosystem) far above the balance-sheet book. |
| **Leverage** - not provided (no debt ratios), but NVIDIA historically carries **low net debt** and strong cash generation, giving it a solid balance sheet. | — | The high market cap relative to book suggests equity is abundant; any debt load is likely modest. |
| **Market Capitalization** | **$4.33 T** | Places NVIDIA among the **largest U.S. tech companies** (top-5 by market value). | Size provides pricing power and access to cheap capital, but also makes the stock highly visible to macro-risk factors. |
| **Liquidity / Share-price range** | 52-week low $86.61, high $184.55 (≈ +113 % swing) | Tech stocks often exhibit 30-70 % ranges; a >100 % swing signals **high volatility**. | The wide range reflects both market enthusiasm for AI and periodic profit-taking. |

**Financial-Strength Take-away**  
- **Balance-sheet quality** is strong (low debt, massive cash flow), enabling continued R&D and strategic acquisitions.  
- The **dividend policy** is deliberately minimal; investors are compensated via share-price appreciation rather than cash yield.  
- The **enormous market cap** gives the company a “too-big-to-fail” perception, but also means any valuation correction can be sizable in absolute dollars.

---

## 5. Risk Factors  

| Risk Element | Detail | Implication |
|--------------|--------|-------------|
| **Valuation Premium** | P/E ≈ 50, P/B ≈ 43, implied P/S > 150. | Any slowdown in AI spend or a shift to cheaper competitors could trigger a sharp re-rating. |
| **Beta / Volatility** | 52-week range of 86.6-184.5 (≈ +113 % swing). | The stock is **highly volatile**; price moves can be amplified by macro-economic news, interest-rate changes, or sector sentiment. |
| **Growth Dependency** | Revenue & earnings growth >50 % YoY. | A deceleration (e.g., slower AI-capex, supply-chain constraints) would disproportionately affect earnings multiples. |
| **Margin Sensitivity** | Operating margin 60 % is partly due to premium pricing; competitive pressure could erode it. | Entry of new AI-chip players (e.g., custom silicon from cloud providers) could compress pricing and margins. |
| **Concentration Risk** | A large share of revenue derives from data-center GPUs. | Over-reliance on a single product line makes the company vulnerable to demand swings in that segment. |
| **Regulatory / Geopolitical** | Export controls on advanced semiconductors (e.g., to China) could limit market size. | Potential curtailment of sales to key growth markets would affect top-line growth. |

Overall, the **primary risk** is that the market's lofty expectations are already baked into the price; any deviation from the current growth trajectory could lead to a disproportionate price correction.

---

## Key Strengths  

1. **Exceptional Profitability** - Operating margin of **60.8 %** and net profit margin of **52.4 %** are far above the technology average, underpinning strong cash generation.  
2. **Accelerating Growth** - **55 % YoY revenue growth** and **61 % YoY earnings growth** demonstrate a rapidly expanding business, driven by the AI-hardware boom.  
3. **Robust Return on Equity** - **ROE > 100 %** signals that shareholders are receiving more than a dollar of profit for every dollar of equity, reflecting both high margins and efficient capital use.  

*These three pillars—margin strength, high-speed growth, and extraordinary ROE—are the chief financial engines supporting NVIDIA's current market valuation.*"""


mock_analyze_sentiment =  """
### **1. Overall Sentiment**  
- **Summary**: **Positive**.  
- **Balance**: 14 "Somewhat-Bullish" articles, 1 "Bullish," 3 "Neutral," and 1 "Somewhat-Bearish." The overwhelming majority of news reinforces optimism about AI and semiconductor sectors.  

---

### **2. Key Positive Themes**  
1. **Rise of Chinese AI Semiconductor Competitors**  
   - **Example**: Huawei and DeepSeek’s progress in AI chip development threatens US dominance, signaling a diversification of global supply chains.  
   - **Business Impact**: While posing a risk to US firms like Nvidia in the short term, this trend could spur innovation and investment in alternative technologies, creating new market opportunities for companies like Moore Threads (Chinese GPU developer) and global partners.  

2. **Strategic Growth in AI Infrastructure**  
   - **Example**: CoreWeave’s $6.3B funding deal and Alchip-Ayar Labs’ co-packaged optics (CPO) for AI datacenters highlight advancements in scalable, high-performance infrastructure.  
   - **Business Impact**: These partnerships could accelerate demand for AI cloud services and datacenter hardware, driving long-term revenue growth for involved companies and enablers like CoreWeave and TSM (Taiwan Semiconductor).  

3. **Analyst Optimism and Long-Term Projections**  
   - **Example**: Analysts predict AI stocks (e.g., NVIDIA, Amazon) could reach $2–$5T valuations by 2028–2030, with quantum AI emerging as a $10T sector.  
   - **Business Impact**: Such projections validate investor confidence, likely attracting capital to AI-related ventures and fostering M&A activity in the sector.  

---

### **3. Key Negative Themes**  
1. **Competitive Pressures from Non-Nvidia Players**  
   - **Example**: Groq’s $750M equity raise and Moore Threads’ IPO signal rising competition in AI chips, challenging NVIDIA and Broadcom’s dominance.  
   - **Business Impact**: These firms could erode market share for incumbents, particularly in custom AI chips, forcing price wars or innovation sprints.  

2. **Regulatory and Geopolitical Risks**  
   - **Example**: Tariff policies (e.g., 100% tariffs on non-US pharmaceuticals) and Trump-era trade rhetoric create uncertainty for global semiconductor supply chains.  
   - **Business Impact**: Sudden policy shifts could disrupt manufacturing costs and partnerships, particularly for companies reliant on cross-border operations (e.g., Intel, TSM).  

3. **Downgrades and Earnings Volatility**  
   - **Example**: IREN’s 500% rally followed by a JP Morgan downgrade highlights market sensitivity to short-term sentiment swings.  
   - **Business Impact**: Over-reliance on speculative momentum could lead to sharp corrections if fundamentals fail to meet expectations.  

---

### **4. Investor/Market Perception**  
- **Short-Term Sentiment**: **Cautious Optimism**.  
  - The market is generally bullish on AI semiconductors but wary of short-term volatility due to competitive threats (e.g., DeepSeek) and geopolitical risks.  
- **Alignment with Financial Performance**:  
  - **Optimistic** for companies with clear growth narratives (e.g., CoreWeave, TSM), but **skeptical** about overvalued stocks (e.g., IREN) lacking sustained fundamentals.  

---

### **5. Risks & Opportunities**  
- **Risks**:  
  1. **Chinese Tech Dominance**: Chinese firms like DeepSeek and Moore Threads could accelerate the decoupling of global semiconductor markets, reducing revenue opportunities for US-based peers.  
  2. **Regulatory Overreach**: Tariff policies or export controls could disrupt supply chains and inflate operational costs for global players.  

- **Opportunities**:  
  1. **Quantum AI Innovation**: Early movers in quantum computing (e.g., D-Wave) may capture market share in the next $10T industry, despite current niche status.  
  2. **Cloud AI Infrastructure Expansion**: CoreWeave’s growth and CPO developments position firms to benefit from surging demand for AI datacenters.  

---

### **Most Positive Theme**: **The Emergence of AI Cloud Infrastructure** (e.g., CoreWeave, CPO technology) signals a structural shift toward scalable, high-performance solutions, creating a multi-year growth runway.  
### **Most Significant Risk**: **Geopolitical Fragmentation**, particularly China’s push to replace US semiconductors, could destabilize global markets and stifle cross-border R&D collaboration.
"""


mock_analyze_webserach = """
**Overall Consensus Rating:** Strong Buy  

**Consensus Price Target:** Approximately $212.00 (average of the listed analyst targets)  

**Recent Analyst Activity:** Not found  

**Most Positive Theme:** Broad analyst optimism reflected in a Strong Buy consensus and high price‑target levels.  

**Most Significant Risk:** Presence of sell ratings and a low end‑target near $100 indicating downside valuation risk.
"""


mock_critique_analyze = """
**Core Opportunity**  
- The explosive, > 50% YoY revenue and earnings growth driven by dominant AI‑chip demand (high‑margin, 60%+ operating margin) positions the company as the clear market leader in a secular AI‑infrastructure wave, underpinning strong analyst optimism and a “Strong Buy” consensus.

**Significant Risk**  
- The stock trades at an extremely rich multiple (P/E ≈ 50, P/B ≈ 43); any slowdown in AI‑spending or competitive pressure—especially from emerging Chinese chip makers—could trigger a sharp valuation correction."""

@pytest.fixture
def sample_state():
    return CapitalCompassState(
    company_ticker = sample_ticker,
    overview_data = mock_alphavantage_overview,
    news_data = mock_alphavantage_news,
    web_search_data = mock_websearch,
    quantitative_analysis = mock_analyze_financials,
    qualitative_analysis = mock_analyze_sentiment,
    websearch_analysis = mock_analyze_webserach,
    critique = mock_critique_analyze,
    )