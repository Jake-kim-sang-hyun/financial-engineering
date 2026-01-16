"""
금융 데이터 수집 모듈
Financial Data Fetcher Module
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from typing import Optional, List, Union


def get_stock_data(
    tickers: Union[str, List[str]],
    start: Optional[str] = None,
    end: Optional[str] = None,
    period: str = "1y"
) -> pd.DataFrame:
    """
    주식 데이터를 Yahoo Finance에서 가져옵니다.

    Parameters
    ----------
    tickers : str or list
        종목 코드 (예: "AAPL" 또는 ["AAPL", "MSFT"])
    start : str, optional
        시작 날짜 (YYYY-MM-DD 형식)
    end : str, optional
        종료 날짜 (YYYY-MM-DD 형식)
    period : str, default "1y"
        기간 (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)

    Returns
    -------
    pd.DataFrame
        OHLCV 데이터

    Examples
    --------
    >>> df = get_stock_data("AAPL", period="6mo")
    >>> df = get_stock_data(["AAPL", "MSFT"], start="2023-01-01", end="2023-12-31")
    """
    if start and end:
        data = yf.download(tickers, start=start, end=end, progress=False)
    else:
        data = yf.download(tickers, period=period, progress=False)

    return data


def get_korean_stock_data(
    ticker: str,
    start: Optional[str] = None,
    end: Optional[str] = None,
    period: str = "1y"
) -> pd.DataFrame:
    """
    한국 주식 데이터를 가져옵니다.

    Parameters
    ----------
    ticker : str
        종목 코드 (예: "005930" 삼성전자)
        코스피: .KS 접미사
        코스닥: .KQ 접미사

    Examples
    --------
    >>> df = get_korean_stock_data("005930")  # 삼성전자
    """
    # 숫자만 있으면 코스피로 간주
    if ticker.isdigit():
        ticker = f"{ticker}.KS"

    return get_stock_data(ticker, start=start, end=end, period=period)


def get_crypto_data(
    symbols: Union[str, List[str]],
    start: Optional[str] = None,
    end: Optional[str] = None,
    period: str = "1y"
) -> pd.DataFrame:
    """
    암호화폐 데이터를 가져옵니다.

    Parameters
    ----------
    symbols : str or list
        심볼 (예: "BTC-USD" 또는 ["BTC-USD", "ETH-USD"])

    Examples
    --------
    >>> df = get_crypto_data("BTC-USD", period="6mo")
    """
    return get_stock_data(symbols, start=start, end=end, period=period)


if __name__ == "__main__":
    # 테스트
    print("Apple 주가 데이터 (최근 1개월):")
    df = get_stock_data("AAPL", period="1mo")
    print(df.tail())
