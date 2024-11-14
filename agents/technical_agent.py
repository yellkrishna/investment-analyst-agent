# agents/technical_agent.py

def technical_analysis_agent(ticker: str) -> dict:
    """
    Stubbed technical analysis agent returning mock data.

    Parameters:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: Mock technical analysis results.
    """
    # Mock data
    return {
        "moving_averages": {
            "ma20": 145.00,
            "ma50": 140.50,
        },
        "rsi": 60.5,
        "support_levels": [138.00, 135.00],
        "resistance_levels": [150.00, 155.00],
        # Additional mock indicators...
    }
