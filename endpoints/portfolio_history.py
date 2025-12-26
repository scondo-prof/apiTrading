import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_account_portfolio_history(
    paper_trading: bool, period: str = None, timeframe: str = None, end_date: str = None, extended_hours: bool = None
) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getaccountportfoliohistory
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        period (str, optional): The duration of the historical data (e.g., '1D', '1W', '1M', '1A'). Defaults to None.
        timeframe (str, optional): The resolution of time window (e.g., '1Min', '5Min', '15Min', '1H', '1D'). Defaults to None.
        end_date (str, optional): The end date of the historical data (ISO 8601 format). Defaults to None.
        extended_hours (bool, optional): Whether to include extended hours data. Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing portfolio history data including equity, profit/loss, and timestamp information.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/account/portfolio/history"
    else:
        pass

    params = {}
    if period:
        params["period"] = period
    if timeframe:
        params["timeframe"] = timeframe
    if end_date:
        params["end_date"] = end_date
    if extended_hours is not None:
        params["extended_hours"] = extended_hours

    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


if __name__ == "__main__":
    print(get_account_portfolio_history(paper_trading=True))
