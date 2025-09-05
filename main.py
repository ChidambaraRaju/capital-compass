
import streamlit as st
from capital_compass.graph import app  # Import your compiled LangGraph app
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

# --- User Input ---
ticker = st.text_input(
    "Enter a stock ticker symbol (e.g., AAPL, NVDA, TSLA)",
    value="NVDA",
    max_chars=10,
    help="Provide the ticker symbol for the company you want to analyze."
).upper()

# --- Analysis Trigger ---
if st.button("Generate Investment Report", type="primary"):
    # 1. Validate Input
    if not ticker:
        st.warning("Please enter a stock ticker to proceed.")
    else:
        # 2. Run the LangGraph agent with a loading spinner
        with st.spinner(f"Analyzing {ticker}... This may take a moment."):
            try:
                # 3. Define the initial state and invoke the graph
                initial_state = {"company_ticker": ticker}
                final_state = app.invoke(initial_state, {"recursion_limit": 10})
                
                # 4. Display the final report
                st.markdown("---")
                st.subheader(f"Investment Report for {ticker}")
                st.markdown(final_state.get("final_report", "No report was generated."))

            except APIClientError as e:
                # 5. Handle specific API errors gracefully
                st.error(f"Failed to fetch data: {e}")
            except Exception as e:
                # 6. Handle other unexpected errors
                st.error(f"An unexpected error occurred: {e}")