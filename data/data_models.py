# data/data_models.py

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class FundamentalAnalysisResult:
    roe: float
    debt_to_equity: float
    net_income: float
    total_assets: float
    # Add more fields as necessary

@dataclass
class TechnicalAnalysisResult:
    moving_averages: Dict[str, float]
    rsi: float
    support_levels: List[float]
    resistance_levels: List[float]
    # Add more fields as necessary

@dataclass
class AnalysisReport:
    ticker: str
    fundamental_analysis: FundamentalAnalysisResult
    technical_analysis: TechnicalAnalysisResult
    generated_at: str
    status: str
