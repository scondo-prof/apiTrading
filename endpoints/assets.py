import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_assets(paper_trading: bool, asset_class: str = None, status: str = None) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/get-v2-assets
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        asset_class (str, optional): Filter assets by asset class (e.g., 'us_equity', 'crypto'). Defaults to None.
        status (str, optional): Filter assets by status (e.g., 'active', 'inactive'). Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing a list of assets with their details including symbol, name, status, and trading permissions.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/assets"
    else:
        pass

    params = {}
    if asset_class:
        params["asset_class"] = asset_class
    if status:
        params["status"] = status

    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


def get_asset_by_id_or_symbol(paper_trading: bool, symbol_or_asset_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/get-v2-assets-symbol-or-assetid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        symbol_or_asset_id (str): The asset symbol (e.g., 'AAPL') or asset ID.

    Returns:
        dict[str, any]: A dictionary containing the asset details including symbol, name, status, asset class, and trading permissions.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/assets/{symbol_or_asset_id}"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


if __name__ == "__main__":
    print(get_assets(paper_trading=True))
