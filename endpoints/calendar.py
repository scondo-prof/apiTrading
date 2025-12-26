import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_market_calendar(paper_trading: bool, start: str = None, end: str = None) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getcalendar
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        start (str, optional): Start date for the calendar query (YYYY-MM-DD format). Defaults to None.
        end (str, optional): End date for the calendar query (YYYY-MM-DD format). Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing market calendar information including trading days, holidays, and market hours.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/calendar"
    else:
        pass

    params = {}
    if start:
        params["start"] = start
    if end:
        params["end"] = end

    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


if __name__ == "__main__":
    print(get_market_calendar(paper_trading=True))
