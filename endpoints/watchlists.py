import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_all_watchlists(paper_trading: bool) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getwatchlists
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).

    Returns:
        dict[str, any]: A dictionary containing a list of all watchlists with their IDs, names, and symbols.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def create_watchlist(paper_trading: bool, name: str, symbols: list[str] = None) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/postwatchlist
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        name (str): The name of the watchlist to create.
        symbols (list[str], optional): List of asset symbols to include in the watchlist. Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing the created watchlist details including ID, name, and symbols.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists"
    else:
        pass

    data = {"name": name}
    if symbols:
        data["symbols"] = symbols

    response_json = httpx.request(method="POST", url=url, headers=headers, json=data).json()

    return response_json


def get_watchlist_by_id(paper_trading: bool, watchlist_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getwatchlistbyid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        watchlist_id (str): The unique identifier for the watchlist.

    Returns:
        dict[str, any]: A dictionary containing the watchlist details including ID, name, and list of symbols.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists/{watchlist_id}"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def update_watchlist_by_id(
    paper_trading: bool, watchlist_id: str, name: str = None, symbols: list[str] = None
) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/putwatchlistbyid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        watchlist_id (str): The unique identifier for the watchlist to update.
        name (str, optional): The new name for the watchlist. Defaults to None.
        symbols (list[str], optional): The new list of symbols for the watchlist. Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing the updated watchlist details.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists/{watchlist_id}"
    else:
        pass

    data = {}
    if name:
        data["name"] = name
    if symbols:
        data["symbols"] = symbols

    response_json = httpx.request(method="PUT", url=url, headers=headers, json=data).json()

    return response_json


def add_asset_to_watchlist(paper_trading: bool, watchlist_id: str, symbol: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/postwatchlistbyid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        watchlist_id (str): The unique identifier for the watchlist.
        symbol (str): The asset symbol to add to the watchlist.

    Returns:
        dict[str, any]: A dictionary containing the updated watchlist with the new symbol added.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists/{watchlist_id}"
    else:
        pass

    data = {"symbol": symbol}
    response_json = httpx.request(method="POST", url=url, headers=headers, json=data).json()

    return response_json


def delete_watchlist_by_id(paper_trading: bool, watchlist_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/deletewatchlistbyid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        watchlist_id (str): The unique identifier for the watchlist to delete.

    Returns:
        dict[str, any]: A dictionary containing confirmation of the deleted watchlist.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists/{watchlist_id}"
    else:
        pass

    response_json = httpx.request(method="DELETE", url=url, headers=headers).json()

    return response_json


def get_watchlist_by_name(paper_trading: bool, name: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getwatchlistbyname
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        name (str): The name of the watchlist to retrieve.

    Returns:
        dict[str, any]: A dictionary containing the watchlist details including ID, name, and list of symbols.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists:by_name"
    else:
        pass

    params = {"name": name}
    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


def update_watchlist_by_name(paper_trading: bool, name: str, symbols: list[str] = None) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/putwatchlistbyname
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        name (str): The name of the watchlist to update.
        symbols (list[str], optional): The new list of symbols for the watchlist. Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing the updated watchlist details.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists:by_name"
    else:
        pass

    data = {}
    if symbols:
        data["symbols"] = symbols

    params = {"name": name}
    response_json = httpx.request(method="PUT", url=url, headers=headers, params=params, json=data).json()

    return response_json


def add_asset_to_watchlist_by_name(paper_trading: bool, name: str, symbol: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/postwatchlistbyname
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        name (str): The name of the watchlist to add the symbol to.
        symbol (str): The asset symbol to add to the watchlist.

    Returns:
        dict[str, any]: A dictionary containing the updated watchlist with the new symbol added.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists:by_name"
    else:
        pass

    data = {"symbol": symbol}
    params = {"name": name}
    response_json = httpx.request(method="POST", url=url, headers=headers, params=params, json=data).json()

    return response_json


def delete_watchlist_by_name(paper_trading: bool, name: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/deletewatchlistbyname
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        name (str): The name of the watchlist to delete.

    Returns:
        dict[str, any]: A dictionary containing confirmation of the deleted watchlist.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists:by_name"
    else:
        pass

    params = {"name": name}
    response_json = httpx.request(method="DELETE", url=url, headers=headers, params=params).json()

    return response_json


def delete_symbol_from_watchlist(paper_trading: bool, watchlist_id: str, symbol: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/deletesymbolfromwatchlist
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        watchlist_id (str): The unique identifier for the watchlist.
        symbol (str): The asset symbol to remove from the watchlist.

    Returns:
        dict[str, any]: A dictionary containing confirmation of the symbol removal.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/watchlists/{watchlist_id}/{symbol}"
    else:
        pass

    response_json = httpx.request(method="DELETE", url=url, headers=headers).json()

    return response_json


if __name__ == "__main__":
    print(get_all_watchlists(paper_trading=True))
