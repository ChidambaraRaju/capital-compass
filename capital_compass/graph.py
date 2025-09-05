from langgraph.graph import StateGraph, END, START
from capital_compass.state import CapitalCompassState
from capital_compass.exceptions import APIClientError

# Import all the agent nodes
from capital_compass.agents.data_fetcher import fetch_overview_node, fetch_news_node
from capital_compass.agents.analysis_agents import analyze_financials, analyze_sentiment,critique_analysis, generate_final_report

# --- 1. Define the StateGraph ---
workflow = StateGraph(CapitalCompassState)

# --- 2. Add Nodes to the Graph ---
# Each node corresponds to a function or agent
workflow.add_node("fetch_overview", fetch_overview_node)
workflow.add_node("fetch_news", fetch_news_node)
workflow.add_node("analyze_financials", analyze_financials)
workflow.add_node("analyze_sentiment", analyze_sentiment)
workflow.add_node("critique_analysis", critique_analysis)
workflow.add_node("generate_final_report", generate_final_report)

# --- 3. Define the Edges to Control the Flow ---

workflow.add_edge(START, "fetch_overview")
workflow.add_edge(START, "fetch_news")

# After fetching, each branch moves to its respective analysis
workflow.add_edge("fetch_overview", "analyze_financials")
workflow.add_edge("fetch_news", "analyze_sentiment")

# After analysis, both branches converge to critique_analysis then critique_analysis to generate_final_report
workflow.add_edge("analyze_financials", "critique_analysis")
workflow.add_edge("analyze_sentiment", "critique_analysis")
workflow.add_edge("critique_analysis", "generate_final_report")


# The final report node is the end of the graph
workflow.add_edge("generate_final_report", END)

# --- 4. Compile the Graph into a Runnable App ---
app = workflow.compile()


# --- Self-Testing Block ---
# This allows you to run the graph directly from the command line for testing

if __name__ == "__main__":
    try:
        # Invoke the graph with the initial state
        # The second argument provides configuration for things like recursion limits
        final_state = app.invoke({"company_ticker": "NVDA"}, {"recursion_limit": 10})
            
        print("\n--- ✅ Final Report Generated ---")
        print(final_state.get("final_report", "No report was generated."))

    except APIClientError as e:
        print(f"\n--- ❌ An API Error Occurred ---")
        print(e)
    except Exception as e:
        print(f"\n--- ❌ An Unexpected Error Occurred ---")
        print(e)