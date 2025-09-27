import pytest
from capital_compass.agents.analysis_agents import (analyze_sentiment, analyze_financials, analyze_websearch, critique_analysis, generate_final_report)


class TestAnalysisAgents:
    """Test cases for analysis agent functions."""
    
    def test_analyze_financials(self, sample_state):
        
        result = analyze_financials(sample_state)
        
        assert "Valuation" in result["quantitative_analysis"]
        assert "Profitability" in result["quantitative_analysis"]
        assert "Growth Trends" in result["quantitative_analysis"]
        assert "Financial Strength" in result["quantitative_analysis"]
        assert "Risk Factors" in result["quantitative_analysis"]
        
    def test_analyze_sentiment(self, sample_state):
        
        result = analyze_sentiment(sample_state)
        
        assert "Overall Sentiment" in result["qualitative_analysis"]
        assert "Key Positive Themes" in result["qualitative_analysis"]
        assert "Key Negative Themes" in result["qualitative_analysis"]
        assert "Investor/Market Perception" in result["qualitative_analysis"]
        assert "Risks & Opportunities" in result["qualitative_analysis"]
        
    def test_analyze_websearch(self, sample_state):
        
        result = analyze_websearch(sample_state)
        
        assert "Overall Consensus Rating" in result["websearch_analysis"]
        assert "Consensus Price Target" in result["websearch_analysis"]
        assert "Recent Analyst Activity" in result["websearch_analysis"]
        
    def test_critique_analysis(self, sample_state):
        
        result = critique_analysis(sample_state)
        
        assert "Core Opportunity" in result["critique"]
        assert "Significant Risk" in result["critique"]
        
    def test_generate_final_report(self, sample_state):
        
        result = generate_final_report(sample_state)
        
        assert "Final Recommendation" in result["final_report"]
        assert "Confidence & Horizon" in result["final_report"]
        assert "Executive Summary" in result["final_report"]
        assert "Key Drivers & Rationale" in result["final_report"]
        assert "Bull Case: Strengths & Opportunities" in result["final_report"]
        assert "Bear Case: Risks & Challenges" in result["final_report"]
        assert "Valuation Context" in result["final_report"]
        assert "Concluding Remarks" in result["final_report"]
        

        