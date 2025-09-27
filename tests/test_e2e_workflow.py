import pytest

# Import the compiled LangGraph app to be tested
from capital_compass.graph import app

# A list of expected section headers in the final report
EXPECTED_SECTIONS = [
    "Confidence & Horizon",
    "Executive Summary",
    "Key Drivers & Rationale",
    "Bull Case",
    "Bear Case",
    "Valuation Context",
    "Concluding Remarks",
]

# A list of valid recommendations
VALID_RECOMMENDATIONS = ["Invest", "Do Not Invest", "Hold with Caution"]

@pytest.mark.e2e
def test_full_graph_invocation_e2e():
    """
    Runs a full end-to-end test of the Capital Compass graph with a live ticker.
    This test makes real API calls and is expected to be slow.
    
    It verifies that:
    1. The graph runs to completion without crashing.
    2. The final report is generated and is not empty.
    3. The final report has the expected structure (all sections are present).
    4. The recommendation is one of the valid, allowed options.
    """
    # Arrange: Define the initial state with a real, valid ticker
    initial_state = {"company_ticker": "MSFT"}
    
    # Act: Invoke the full LangGraph application
    # We expect this to take some time as it makes multiple API calls
    final_state = app.invoke(initial_state, {"recursion_limit": 10})
    
    # Assert: Perform checks on the final output
    
    # 1. Ensure the final state and report exist
    assert final_state is not None
    final_report = final_state.get("final_report")
    assert final_report is not None, "Final report should exist in the final state."
    assert isinstance(final_report, str), "Final report should be a string."
    assert len(final_report) > 100, "Final report should not be an empty or short string."
    
    # 2. Check for the structural integrity of the report
    for section in EXPECTED_SECTIONS:
        assert f"**{section}**" in final_report, f"Section '{section}' is missing from the report."

    # 3. Validate the recommendation
    # Extract the first line after the "Final Recommendation" header
    try:
        recommendation_line = final_report.split("Final Recommendation**")[1].strip().split('\n')[0].strip()
        assert recommendation_line in VALID_RECOMMENDATIONS, \
            f"Recommendation '{recommendation_line}' is not one of the valid options."
    except IndexError:
        pytest.fail("Could not parse the 'Final Recommendation' from the report.")