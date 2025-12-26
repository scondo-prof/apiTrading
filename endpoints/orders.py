import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def create_order(paper_trading: bool, order_data: dict) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/postorder
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        order_data (dict): Dictionary containing order parameters such as symbol, qty, side, type, time_in_force, etc.

    Returns:
        dict[str, any]: A dictionary containing the created order details including order ID, status, and order information.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/orders"
    else:
        pass

    response_json = httpx.request(method="POST", url=url, headers=headers, json=order_data).json()

    return response_json


def get_all_orders(
    paper_trading: bool,
    status: str = None,
    limit: int = None,
    nested: bool = None,
    after: str = None,
    until: str = None,
    direction: str = None,
    symbols: str = None,
) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getorders
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        status (str, optional): Filter orders by status (e.g., 'open', 'closed', 'all'). Defaults to None.
        limit (int, optional): Maximum number of orders to return. Defaults to None.
        nested (bool, optional): If true, returns nested objects. Defaults to None.
        after (str, optional): Filter orders submitted after this date (ISO 8601 format). Defaults to None.
        until (str, optional): Filter orders submitted until this date (ISO 8601 format). Defaults to None.
        direction (str, optional): The chronological order of response based on the submission time. 'asc' or 'desc'. Defaults to None.
        symbols (str, optional): Comma-separated list of symbols to filter by. Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing a list of orders matching the filter criteria.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/orders"
    else:
        pass

    params = {}
    if status:
        params["status"] = status
    if limit:
        params["limit"] = limit
    if nested is not None:
        params["nested"] = nested
    if after:
        params["after"] = after
    if until:
        params["until"] = until
    if direction:
        params["direction"] = direction
    if symbols:
        params["symbols"] = symbols

    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


def delete_all_orders(paper_trading: bool) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/deleteorders
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).

    Returns:
        dict[str, any]: A dictionary containing information about the cancelled orders.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/orders"
    else:
        pass

    response_json = httpx.request(method="DELETE", url=url, headers=headers).json()

    return response_json


def get_order_by_client_order_id(paper_trading: bool, client_order_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getorderbyclientorderid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        client_order_id (str): The client order ID used when placing the order.

    Returns:
        dict[str, any]: A dictionary containing the order details for the specified client order ID.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/orders:by_client_order_id"
    else:
        pass

    params = {"client_order_id": client_order_id}
    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


def get_order_by_id(paper_trading: bool, order_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getorderbyid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        order_id (str): The unique identifier for the order.

    Returns:
        dict[str, any]: A dictionary containing the order details including status, symbol, quantity, and execution information.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/orders/{order_id}"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def replace_order_by_id(paper_trading: bool, order_id: str, order_data: dict) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/patchorderbyid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        order_id (str): The unique identifier for the order to replace.
        order_data (dict): Dictionary containing the updated order parameters (qty, limit_price, stop_price, etc.).

    Returns:
        dict[str, any]: A dictionary containing the updated order details.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/orders/{order_id}"
    else:
        pass

    response_json = httpx.request(method="PATCH", url=url, headers=headers, json=order_data).json()

    return response_json


def delete_order_by_id(paper_trading: bool, order_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/deleteorderbyid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        order_id (str): The unique identifier for the order to cancel.

    Returns:
        dict[str, any]: A dictionary containing information about the cancelled order.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/orders/{order_id}"
    else:
        pass

    response_json = httpx.request(method="DELETE", url=url, headers=headers).json()

    return response_json


if __name__ == "__main__":
    print(get_all_orders(paper_trading=True))
