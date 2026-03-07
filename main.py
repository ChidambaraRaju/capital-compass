
import streamlit as st
import re
from capital_compass.graph import app  # Import the compiled LangGraph app
from capital_compass.exceptions import APIClientError
from capital_compass.tools.alpha_vantage_client import search_company_by_name

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

# Initialize session state for selected ticker
if "selected_ticker" not in st.session_state:
    st.session_state.selected_ticker = None

if "search_results" not in st.session_state:
    st.session_state.search_results = None

# Create tabs for ticker and company name search
search_tabs = st.tabs(["By Ticker", "By Company Name"])

# Tab 1: Direct Ticker Input (existing flow)
with search_tabs[0]:
    st.subheader("Direct Ticker Input")
    ticker = st.text_input(
        "Enter a stock ticker symbol (e.g., AAPL, NVDA, TSLA)",
        value="NVDA",
        max_chars=10,
        key="ticker_input",
        help="Provide the ticker symbol for the company you want to analyze."
    ).upper()

# Tab 2: Company Name Search (new flow)
with search_tabs[1]:
    st.subheader("Search by Company Name")
    st.write("Enter company name (e.g., Apple, Microsoft, Tesla)")

    col1, col2, col3 = st.columns([4, 1, 1])

    with col1:
        search_query = st.text_input(
            label="Company Name",
            label_visibility="collapsed",
            placeholder="Type company name...",
            key="company_search_input",
            help="Enter full or partial company name to search for the ticker symbol."
        )

    with col2:
        search_button = st.button("Search", type="primary", key="search_company_btn")

    with col3:
        clear_button = st.button("Clear", key="clear_search_btn")

    # Handle search button click
    if search_button and search_query:
        if not search_query.strip():
            st.warning("Please enter a company name to search.")
        else:
            with st.spinner("Searching companies..."):
                try:
                    results = search_company_by_name(search_query)
                    st.session_state.search_results = results

                    if not results:
                        st.warning("No companies found. Try a different search term.")
                    else:
                        st.success(f"Found {len(results)} matching company/companies")

                except APIClientError as e:
                    st.error(f"Search failed: {e}")

    # Display search results in an expander for cleaner UI
    if st.session_state.search_results:
        with st.expander("📋 Search Results", expanded=False):
            # Display results as selectable list with better formatting
            for i, company in enumerate(st.session_state.search_results, 1):
                match_score = company.get('matchScore', 'N/A')
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"**{company.get('name', 'N/A')}**")
                    st.caption(f"{company.get('symbol', 'N/A')} • {company.get('region', 'N/A')}")
                with col2:
                    st.metric("Match", f"{match_score}")
                with col3:
                    if i == 1:
                        st.markdown("🥇 **Best Match**")
                    else:
                        st.markdown(f"#{i}")

        # Company selection dropdown - NO AUTO-SELECTION (moved outside expander)
        # Add a None option at the beginning
        select_options = [None] + st.session_state.search_results

        selected_company = st.selectbox(
            "Select a company to analyze:",
            options=select_options,
            format_func=lambda x: (
                "Choose a company..." if x is None
                else f"{x.get('name', 'N/A')} ({x.get('symbol', 'N/A')})"
            ),
            key="company_select",
            help="Choose a company from the search results to analyze",
            label_visibility="visible"
        )

        # Only update session state when user explicitly selects a company (not None)
        if selected_company and selected_company.get('symbol'):
            st.session_state.selected_ticker = selected_company.get('symbol')
            st.info(f"✅ Selected: **{selected_company.get('name')}** ({selected_company.get('symbol')})")

    # Handle clear button
    if clear_button:
        st.session_state.search_results = None
        st.session_state.selected_ticker = None
        st.rerun()

# --- Analysis Trigger ---

# Determine which ticker to analyze:
# - If user selected from search, use selected_ticker (must not be None)
# - Otherwise, use direct ticker input from "By Ticker" tab
search_ticker = st.session_state.get('selected_ticker')
ticker_to_analyze = search_ticker if search_ticker else ticker

st.markdown("---")

if st.button("Generate Investment Report", type="primary", key="generate_report_btn"):
    # 1. Pre Validation: Check the ticker format before calling the API
    # This regex checks for 1-5 uppercase letters, optionally followed by a dot and 1-2 letters (for non-US exchanges)
    if not re.match(r"^[A-Z]{1,5}(\.[A-Z]{1,2})?$", ticker_to_analyze):
        st.error("Invalid ticker format. Please enter a valid stock symbol (e.g., 'AAPL', 'MSFT').")
    # 2. If search results are present and user hasn't selected a company
    elif st.session_state.search_results and not search_ticker:
        st.warning("Please select a company from the search results to proceed with the analysis.")
    # 3. Validate non-empty input (only applies when not using search results)
    elif not ticker_to_analyze and not st.session_state.search_results:
        st.warning("Please enter a stock ticker in the 'By Ticker' tab.")
    else:
        # 3. Run the LangGraph agent with a loading spinner
        with st.spinner(f"Analyzing {ticker_to_analyze}... This may take a moment."):
            try:
                # 4. Define the initial state and invoke the graph
                initial_state = {"company_ticker": ticker_to_analyze}
                final_state = app.invoke(initial_state, {"recursion_limit": 10})

                # 5. Display the final report
                st.markdown("---")
                st.subheader(f"Investment Report for {ticker_to_analyze}")
                st.markdown(final_state.get("final_report", "No report was generated."))

            except APIClientError as e:
                # 6. Handle specific API errors gracefully
                st.error(f"Failed to fetch data: {e}")
            except Exception as e:
                # 7. Handle other unexpected errors
                st.error(f"An unexpected error occurred: {e}")