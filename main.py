
import streamlit as st
import re
from capital_compass.graph import app  # Import the compiled LangGraph app
from capital_compass.exceptions import APIClientError

# --- Page Configuration ---
st.set_page_config(
    page_title="Capital Compass",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Sidebar Content ---
with st.sidebar:
    st.image("assets/logo.png", width=200)
    st.header("About Capital Compass")
    st.info(
        "Capital Compass is an AI-powered investment research tool that "
        "synthesizes financial data and market news to generate a comprehensive "
        "investment report for any given stock ticker."
    )
    st.markdown("---")
    st.subheader("Technology Stack")
    st.markdown(
        """
        - **UI:** Streamlit
        - **Orchestration:** LangGraph
        - **LLMs:** Groq (Multi-model)
        - **Data:** Alpha Vantage
        """
    )

# --- Main Application UI ---
st.title("Capital Compass 🧭")
st.markdown("Your AI-powered co-pilot for investment research. Enter a stock ticker to begin.")
st.info("This is an AI-generated report and should not be considered financial advice. Always conduct your own research and consult with a professional financial advisor.")

# --- User Input ---
ticker = st.text_input(
    "Enter a stock ticker symbol (e.g., AAPL, NVDA, TSLA)",
    value="NVDA",
    max_chars=10,
    help="Provide the ticker symbol for the company you want to analyze."
).upper()

# --- Analysis Trigger ---
if st.button("Generate Investment Report", type="primary"):
    # 1. Pre Validation: Check the ticker format before calling the API
    # This regex checks for 1-5 uppercase letters, optionally followed by a dot and 1-2 letters (for non-US exchanges)
    if not re.match(r"^[A-Z]{1,5}(\.[A-Z]{1,2})?$", ticker):
        st.error("Invalid ticker format. Please enter a valid stock symbol (e.g., 'AAPL', 'MSFT').")
    # 2. Validate non-empty input
    elif not ticker:
        st.warning("Please enter a stock ticker to proceed.")
    else:
        # 3. Run the LangGraph agent with a loading spinner
        with st.spinner(f"Analyzing {ticker}... This may take a moment."):
            try:
                # 4. Define the initial state and invoke the graph
                initial_state = {"company_ticker": ticker}
                final_state = app.invoke(initial_state, {"recursion_limit": 10})
                
                # 5. Display the final report
                st.markdown("---")
                st.subheader(f"Investment Report for {ticker}")
                st.markdown(final_state.get("final_report", "No report was generated."))

            except APIClientError as e:
                # 6. Handle specific API errors gracefully
                st.error(f"Failed to fetch data: {e}")
            except Exception as e:
                # 7. Handle other unexpected errors
                st.error(f"An unexpected error occurred: {e}")