import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_market_clock(paper_trading: bool) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getclock
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).

    Returns:
        dict[str, any]: A dictionary containing the current market clock information including timestamp and whether the market is open.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/clock"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


if __name__ == "__main__":
    print(get_market_clock(paper_trading=True))
