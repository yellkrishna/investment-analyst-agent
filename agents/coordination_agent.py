# agents/coordination_agent.py

from datetime import datetime, timezone
from agents.fundamental_agent import fundamental_analysis_agent
from agents.technical_agent import technical_analysis_agent
from data.data_models import AnalysisReport

def coordination_agent(ticker: str, options: dict = None) -> dict:
    try:
        # Invoke agents
        fundamental_result = fundamental_analysis_agent(ticker)
        technical_result = technical_analysis_agent(ticker)
        
        # Build report
        report = {
            "ticker": ticker,
            "fundamental_analysis": fundamental_result,
            "technical_analysis": technical_result,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "status": "success"
        }
    except Exception as e:
        report = {
            "ticker": ticker,
            "fundamental_analysis": None,
            "technical_analysis": None,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "status": "error",
            "message": str(e)
        }
    return report

