"""
수익률 분석 모듈
Returns Analysis Module
"""

import pandas as pd
import numpy as np
from typing import Optional


def calculate_returns(
    prices: pd.Series,
    method: str = "simple"
) -> pd.Series:
    """
    수익률을 계산합니다.

    Parameters
    ----------
    prices : pd.Series
        가격 시계열
    method : str, default "simple"
        "simple": 단순 수익률 (r = (P1 - P0) / P0)
        "log": 로그 수익률 (r = ln(P1 / P0))

    Returns
    -------
    pd.Series
        수익률 시계열
    """
    if method == "simple":
        return prices.pct_change()
    elif method == "log":
        return np.log(prices / prices.shift(1))
    else:
        raise ValueError(f"Unknown method: {method}")


def calculate_cumulative_returns(returns: pd.Series) -> pd.Series:
    """
    누적 수익률을 계산합니다.

    Parameters
    ----------
    returns : pd.Series
        수익률 시계열

    Returns
    -------
    pd.Series
        누적 수익률
    """
    return (1 + returns).cumprod() - 1


def calculate_annualized_return(
    returns: pd.Series,
    periods_per_year: int = 252
) -> float:
    """
    연환산 수익률을 계산합니다.

    Parameters
    ----------
    returns : pd.Series
        일별 수익률
    periods_per_year : int, default 252
        연간 거래일 수

    Returns
    -------
    float
        연환산 수익률
    """
    total_return = (1 + returns).prod() - 1
    n_periods = len(returns)
    years = n_periods / periods_per_year

    return (1 + total_return) ** (1 / years) - 1


def calculate_volatility(
    returns: pd.Series,
    periods_per_year: int = 252
) -> float:
    """
    연환산 변동성을 계산합니다.

    Parameters
    ----------
    returns : pd.Series
        일별 수익률
    periods_per_year : int, default 252
        연간 거래일 수

    Returns
    -------
    float
        연환산 변동성
    """
    return returns.std() * np.sqrt(periods_per_year)


def calculate_sharpe_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.02,
    periods_per_year: int = 252
) -> float:
    """
    샤프 비율을 계산합니다.

    Parameters
    ----------
    returns : pd.Series
        일별 수익률
    risk_free_rate : float, default 0.02
        무위험 수익률 (연율)
    periods_per_year : int, default 252
        연간 거래일 수

    Returns
    -------
    float
        샤프 비율
    """
    ann_return = calculate_annualized_return(returns, periods_per_year)
    ann_vol = calculate_volatility(returns, periods_per_year)

    return (ann_return - risk_free_rate) / ann_vol


def calculate_max_drawdown(prices: pd.Series) -> float:
    """
    최대 낙폭(MDD)을 계산합니다.

    Parameters
    ----------
    prices : pd.Series
        가격 시계열

    Returns
    -------
    float
        최대 낙폭 (음수)
    """
    cummax = prices.cummax()
    drawdown = (prices - cummax) / cummax

    return drawdown.min()


def performance_summary(
    prices: pd.Series,
    risk_free_rate: float = 0.02
) -> pd.Series:
    """
    성과 요약을 반환합니다.

    Parameters
    ----------
    prices : pd.Series
        가격 시계열
    risk_free_rate : float, default 0.02
        무위험 수익률 (연율)

    Returns
    -------
    pd.Series
        성과 지표들
    """
    returns = calculate_returns(prices).dropna()

    summary = {
        "총 수익률": f"{((prices.iloc[-1] / prices.iloc[0]) - 1) * 100:.2f}%",
        "연환산 수익률": f"{calculate_annualized_return(returns) * 100:.2f}%",
        "연환산 변동성": f"{calculate_volatility(returns) * 100:.2f}%",
        "샤프 비율": f"{calculate_sharpe_ratio(returns, risk_free_rate):.2f}",
        "최대 낙폭": f"{calculate_max_drawdown(prices) * 100:.2f}%",
    }

    return pd.Series(summary)
