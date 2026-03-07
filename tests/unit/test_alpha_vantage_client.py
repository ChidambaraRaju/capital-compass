"""Unit tests for Alpha Vantage API client."""
import pytest
from unittest.mock import patch, Mock
import requests

from capital_compass.tools.alpha_vantage_client import (
    search_company_by_name,
    get_company_overview,
    get_news_sentiment
)
from capital_compass.exceptions import APIClientError


class TestSearchCompanyByName:
    """Test suite for search_company_by_name function."""

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_success(self, mock_get):
        """Test successful company search with multiple results."""
        # Mock API response
        mock_response = Mock()
        mock_response.json.return_value = {
            "bestMatches": [
                {
                    "1. symbol": "AAPL",
                    "2. name": "Apple Inc.",
                    "3. type": "Equity",
                    "4. region": "United States",
                    "5. marketOpen": "09:30",
                    "6. marketClose": "16:00",
                    "7. timezone": "UTC-05",
                    "8. currency": "USD",
                    "9. matchScore": "1.0000"
                },
                {
                    "1. symbol": "APLE",
                    "2. name": "Apple Hospitality REIT Inc.",
                    "3. type": "Equity",
                    "4. region": "United States",
                    "5. marketOpen": "09:30",
                    "6. marketClose": "16:00",
                    "7. timezone": "UTC-05",
                    "8. currency": "USD",
                    "9. matchScore": "0.8889"
                },
                {
                    "1. symbol": "AAPL34.SAO",
                    "2. name": "Apple Inc.",
                    "3. type": "Equity",
                    "4. region": "Brazil",
                    "5. marketOpen": "10:00",
                    "6. marketClose": "17:55",
                    "7. timezone": "UTC-03",
                    "8. currency": "BRL",
                    "9. matchScore": "0.7143"
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call function
        results = search_company_by_name("Apple")

        # Verify results
        assert len(results) == 3
        assert results[0]["symbol"] == "AAPL"
        assert results[0]["name"] == "Apple Inc."
        assert results[0]["type"] == "Equity"
        assert results[0]["region"] == "United States"
        assert results[0]["marketOpen"] == "09:30"
        assert results[0]["marketClose"] == "16:00"
        assert results[0]["timezone"] == "UTC-05"
        assert results[0]["currency"] == "USD"
        assert results[0]["matchScore"] == "1.0000"

        # Verify mock was called with correct URL
        mock_get.assert_called_once()
        call_args = mock_get.call_args[0][0]
        assert "SYMBOL_SEARCH" in call_args
        assert "keywords=Apple" in call_args

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_no_results(self, mock_get):
        """Test handling of no search results."""
        mock_response = Mock()
        mock_response.json.return_value = {"bestMatches": []}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call function
        results = search_company_by_name("NonExistentCompany")

        # Verify empty list returned
        assert results == []

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_api_rate_limit(self, mock_get):
        """Test handling of API rate limit."""
        mock_response = Mock()
        mock_response.json.return_value = {"Note": "API call frequency"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Should raise APIClientError
        with pytest.raises(APIClientError, match="API limit"):
            search_company_by_name("AAPL")

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_network_error(self, mock_get):
        """Test handling of network errors."""
        mock_get.side_effect = requests.exceptions.ConnectionError("Network down")

        # Should raise APIClientError
        with pytest.raises(APIClientError, match="Network error"):
            search_company_by_name("AAPL")

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_json_decode_error(self, mock_get):
        """Test handling of invalid JSON response."""
        mock_response = Mock()
        mock_response.json.side_effect = requests.exceptions.JSONDecodeError("Invalid JSON", "", 0)
        mock_get.return_value = mock_response

        # Should raise APIClientError with Network error prefix
        with pytest.raises(APIClientError, match="Network error"):
            search_company_by_name("AAPL")

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_sorting_by_match_score(self, mock_get):
        """Test that results are sorted by matchScore descending."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "bestMatches": [
                {
                    "1. symbol": "MSFT",
                    "2. name": "Microsoft Corporation",
                    "9. matchScore": "0.5000"
                },
                {
                    "1. symbol": "AAPL",
                    "2. name": "Apple Inc.",
                    "9. matchScore": "1.0000"
                },
                {
                    "1. symbol": "GOOGL",
                    "2. name": "Alphabet Inc.",
                    "9. matchScore": "0.7500"
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call function
        results = search_company_by_name("test")

        # Verify sorted order (highest matchScore first)
        assert results[0]["symbol"] == "AAPL"
        assert results[0]["matchScore"] == "1.0000"
        assert results[1]["symbol"] == "GOOGL"
        assert results[1]["matchScore"] == "0.7500"
        assert results[2]["symbol"] == "MSFT"
        assert results[2]["matchScore"] == "0.5000"

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_handles_alternative_key_format(self, mock_get):
        """Test handling of both numbered and non-numbered key formats."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "bestMatches": [
                {
                    "1. symbol": "AAPL",
                    "2. name": "Apple Inc.",
                    "9. matchScore": "0.9500"
                },
                # Mix of numbered and non-numbered keys
                {
                    "symbol": "MSFT",
                    "name": "Microsoft",
                    "type": "Equity",
                    "region": "US",
                    "matchScore": "0.9000"
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call function
        results = search_company_by_name("test")

        # Verify both formats are normalized correctly
        assert len(results) == 2
        assert results[0]["symbol"] == "AAPL"
        assert results[1]["symbol"] == "MSFT"

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_special_characters(self, mock_get):
        """Test that search handles spaces and special characters."""
        mock_response = Mock()
        mock_response.json.return_value = {"bestMatches": []}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Search with spaces and special characters
        search_company_by_name("Apple Inc.")

        # Verify URL is constructed with the keywords
        mock_get.assert_called_once()
        call_url = mock_get.call_args[0][0]
        assert "SYMBOL_SEARCH" in call_url
        assert "keywords=" in call_url

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_empty_best_matches(self, mock_get):
        """Test handling when API returns empty bestMatches."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "bestMatches": []
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        results = search_company_by_name("test")

        assert results == []

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_missing_best_matches_key(self, mock_get):
        """Test handling when bestMatches key is missing."""
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        results = search_company_by_name("test")

        # Should return empty list, not error
        assert results == []

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_http_error(self, mock_get):
        """Test handling of HTTP errors."""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        # Should raise APIClientError
        with pytest.raises(APIClientError, match="Network error"):
            search_company_by_name("AAPL")

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_search_timeout(self, mock_get):
        """Test handling of timeout errors."""
        mock_get.side_effect = requests.exceptions.Timeout("Request timed out")

        # Should raise APIClientError
        with pytest.raises(APIClientError, match="Network error"):
            search_company_by_name("AAPL")


class TestGetCompanyOverview:
    """Unit tests for get_company_overview function."""

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_overview_success(self, mock_get):
        """Test successful company overview fetch."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "Symbol": "AAPL",
            "Name": "Apple Inc.",
            "Sector": "Technology"
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = get_company_overview("AAPL")

        assert result["Symbol"] == "AAPL"
        assert result["Name"] == "Apple Inc."
        assert result["Sector"] == "Technology"

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_overview_invalid_ticker(self, mock_get):
        """Test handling of invalid ticker."""
        mock_response = Mock()
        mock_response.json.return_value = {"Error Message": "Invalid API call"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        with pytest.raises(APIClientError, match="not found or is invalid"):
            get_company_overview("INVALID")

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_overview_rate_limit(self, mock_get):
        """Test handling of API rate limit."""
        mock_response = Mock()
        mock_response.json.return_value = {"Note": "API call frequency"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        with pytest.raises(APIClientError, match="API limit"):
            get_company_overview("AAPL")


class TestGetNewsSentiment:
    """Unit tests for get_news_sentiment function."""

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_news_success(self, mock_get):
        """Test successful news sentiment fetch."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "feed": [
                {"title": "Test Article", "summary": "Test summary"}
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = get_news_sentiment("AAPL")

        assert "feed" in result
        assert len(result["feed"]) == 1

    @patch('capital_compass.tools.alpha_vantage_client.requests.get')
    def test_news_rate_limit(self, mock_get):
        """Test handling of API rate limit."""
        mock_response = Mock()
        mock_response.json.return_value = {"Note": "API call frequency"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        with pytest.raises(APIClientError, match="API limit"):
            get_news_sentiment("AAPL")
