import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_all_open_positions(paper_trading: bool) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getpositions
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).

    Returns:
        dict[str, any]: A dictionary containing a list of all open positions with details such as symbol, qty, market value, and unrealized P/L.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/positions"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def close_all_positions(paper_trading: bool, cancel_orders: bool = False) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/deletepositions
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        cancel_orders (bool, optional): If true, cancels all open orders before closing positions. Defaults to False.

    Returns:
        dict[str, any]: A dictionary containing information about the closed positions.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/positions"
    else:
        pass

    params = {}
    if cancel_orders:
        params["cancel_orders"] = cancel_orders

    response_json = httpx.request(method="DELETE", url=url, headers=headers, params=params).json()

    return response_json


def get_open_position(paper_trading: bool, symbol_or_asset_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getpositionbysymbol
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        symbol_or_asset_id (str): The asset symbol (e.g., 'AAPL') or asset ID for the position.

    Returns:
        dict[str, any]: A dictionary containing the position details including qty, market value, average entry price, and unrealized P/L.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/positions/{symbol_or_asset_id}"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def close_position(
    paper_trading: bool, symbol_or_asset_id: str, qty: float = None, percentage: float = None
) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/deletepositionbysymbol
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        symbol_or_asset_id (str): The asset symbol (e.g., 'AAPL') or asset ID for the position to close.
        qty (float, optional): The number of shares to close. If not specified, closes the entire position. Defaults to None.
        percentage (float, optional): The percentage of the position to close (0-100). If not specified, closes the entire position. Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing information about the closed position.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/positions/{symbol_or_asset_id}"
    else:
        pass

    params = {}
    if qty:
        params["qty"] = qty
    if percentage:
        params["percentage"] = percentage

    response_json = httpx.request(method="DELETE", url=url, headers=headers, params=params).json()

    return response_json


def exercise_options_position(paper_trading: bool, symbol_or_asset_id: str, qty: int) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/postpositionbyoptionsymbol
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        symbol_or_asset_id (str): The options symbol or asset ID for the position to exercise.
        qty (int): The number of contracts to exercise.

    Returns:
        dict[str, any]: A dictionary containing information about the exercised options position.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/positions/{symbol_or_asset_id}/exercise"
    else:
        pass

    data = {"qty": qty}
    response_json = httpx.request(method="POST", url=url, headers=headers, json=data).json()

    return response_json


if __name__ == "__main__":
    print(get_all_open_positions(paper_trading=True))
