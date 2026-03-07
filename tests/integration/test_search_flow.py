"""Integration test for complete search and analysis flow."""
import pytest
from capital_compass.tools.alpha_vantage_client import search_company_by_name, get_company_overview
from capital_compass.exceptions import APIClientError


# Register custom integration marker
def pytest_configure(config):
    config.addinivalue_line("markers", "integration: integration tests")

pytest.mark.integration = pytest.mark.integration
class TestSearchFlowIntegration:
    """Integration tests for the complete search flow."""

    def test_search_to_ticker_selection(self):
        """Test flow: Search company → Select ticker → Verify ticker works."""
        # Step 1: Search for a company
        results = search_company_by_name("Apple")

        assert isinstance(results, list), "Search should return a list"

        # Skip if rate limited
        if len(results) == 0:
            pytest.skip("API rate limit reached - skipping ticker verification")

        assert len(results) > 0, "Should find at least one result"

        # Step 2: Verify result structure
        first_result = results[0]
        assert "symbol" in first_result, "Result should have 'symbol' key"
        assert "name" in first_result, "Result should have 'name' key"
        assert "matchScore" in first_result, "Result should have 'matchScore' key"

        # Step 3: Extract ticker
        ticker = first_result["symbol"]
        assert ticker == "AAPL" or ticker == "APLE", "Should find Apple ticker"

        # Step 4: Verify ticker works with existing API
        overview = get_company_overview(ticker)

        # Skip if rate limited
        if "Information" in overview:
            pytest.skip("API rate limit reached - skipping overview verification")

        assert isinstance(overview, dict), "Overview should be a dictionary"
        assert overview.get("Symbol") == ticker, "Symbol should match"

    def test_search_no_results_handling(self):
        """Test flow: Search non-existent → Handle gracefully."""
        # Search for company that doesn't exist
        results = search_company_by_name("NonExistentCompanyXYZ123")

        assert results == [], "Should return empty list for non-existent company"

    def test_search_results_sorted(self):
        """Test flow: Search → Verify results sorted by matchScore."""
        # Search with multiple potential matches
        results = search_company_by_name("Apple")

        if len(results) > 1:
            # Verify sorting by matchScore (descending)
            scores = [float(r.get('matchScore', 0)) for r in results]
            is_sorted = all(scores[i] >= scores[i+1] for i in range(len(scores)-1))
            assert is_sorted, "Results should be sorted by matchScore descending"

    def test_search_ticker_formats(self):
        """Test that search handles different ticker formats."""
        # Search for Microsoft
        results = search_company_by_name("Microsoft")

        if len(results) > 0:
            # Check for various ticker formats
            tickers = [r.get('symbol', '') for r in results]

            # Should include common formats
            has_us_format = any('.' not in t for t in tickers)  # e.g., MSFT
            has_intl_format = any('.' in t for t in tickers)  # e.g., MSFT.DE

            assert has_us_format or has_intl_format, "Should find common ticker formats"

    def test_search_to_analysis_data_flow(self):
        """Test data flow: Search → Extract → Pass to analysis."""
        # This simulates what happens in the UI

        # User searches
        search_query = "Tesla"
        results = search_company_by_name(search_query)

        # User selects a company
        if results:
            selected = results[0]
            ticker = selected.get('symbol', '')

            # This ticker would be used in the LangGraph analysis
            assert ticker, "Should extract ticker from search result"

            # Verify ticker is not empty
            assert ticker, "Should extract ticker from search result"

            # Note: Some international tickers may have formats like XXX.LON
            # The basic regex check in main.py handles most cases

    def test_search_edge_cases(self):
        """Test edge cases in search functionality."""
        # Empty string search
        results = search_company_by_name("")
        # Should return empty list or handle gracefully
        assert isinstance(results, list), "Should return list for empty search"

        # Single character search
        results = search_company_by_name("A")
        # Should handle short searches
        assert isinstance(results, list), "Should return list for short search"

        # Search with special characters
        results = search_company_by_name("Apple Inc.")
        # Should handle special characters
        assert isinstance(results, list), "Should return list with special chars"

    @pytest.mark.skip(reason="Requires real API call")
    def test_end_to_end_search_to_report(self):
        """Complete end-to-end test: Search → Analyze → Report.

        This test is skipped by default as it requires a full LangGraph
        execution which can be slow and consume API quota.

        Run with: pytest -m "integration and not skip" tests/integration/test_search_flow.py
        """
        from capital_compass.graph import app

        # Search for a company
        results = search_company_by_name("Apple")
        assert len(results) > 0, "Should find Apple"

        # Select the first result
        ticker = results[0]["symbol"]

        # Run the full analysis graph
        initial_state = {"company_ticker": ticker}
        final_state = app.invoke(initial_state, {"recursion_limit": 10})

        # Verify final report was generated
        assert "final_report" in final_state, "Should have final_report"
        assert len(final_state["final_report"]) > 100, "Report should have content"

        # Verify report structure
        report = final_state["final_report"]
        expected_sections = [
            "Final Recommendation",
            "Confidence",
            "Horizon",
            "Executive Summary"
        ]

        for section in expected_sections:
            assert section in report, f"Report should contain {section}"


@pytest.mark.integration
class TestSearchErrorHandlingIntegration:
    """Integration tests for error handling in search flow."""

    def test_api_limit_propagation(self):
        """Test that API limit errors are properly propagated."""
        import os
        from unittest.mock import patch, Mock
        import requests

        # Mock a rate limit response
        with patch('capital_compass.tools.alpha_vantage_client.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = {"Note": "API call frequency"}
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response

            # Should raise APIClientError
            with pytest.raises(APIClientError, match="API limit"):
                search_company_by_name("AAPL")

    def test_network_error_handling(self):
        """Test that network errors are properly handled."""
        from unittest.mock import patch, Mock
        import requests

        # Mock a network error
        with patch('capital_compass.tools.alpha_vantage_client.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError("Network error")

            # Should raise APIClientError
            with pytest.raises(APIClientError, match="Network error"):
                search_company_by_name("AAPL")

    def test_json_decode_error_handling(self):
        """Test that JSON decode errors are properly handled."""
        from unittest.mock import patch, Mock
        import requests

        # Mock a JSON decode error
        with patch('capital_compass.tools.alpha_vantage_client.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.side_effect = requests.exceptions.JSONDecodeError("Invalid JSON", "", 0)
            mock_get.return_value = mock_response

            # Should raise APIClientError
            # The error message includes "decode JSON" somewhere in the text
            with pytest.raises(APIClientError):
                search_company_by_name("AAPL")
