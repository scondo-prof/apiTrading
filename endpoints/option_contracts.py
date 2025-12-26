import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_option_contracts(
    paper_trading: bool,
    underlying_symbols: str = None,
    root_symbol: str = None,
    strike_price: float = None,
    expiration_date: str = None,
    expiration_date_gte: str = None,
    expiration_date_lte: str = None,
    type: str = None,
    style: str = None,
    limit: int = None,
    sort: str = None,
    page_token: str = None,
) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/get-v2-options-contracts
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        underlying_symbols (str, optional): Comma-separated list of underlying symbols to filter by (e.g., 'AAPL,MSFT'). Defaults to None.
        root_symbol (str, optional): The root symbol for the option contracts. Defaults to None.
        strike_price (float, optional): Filter contracts by strike price. Defaults to None.
        expiration_date (str, optional): Filter contracts by exact expiration date (YYYY-MM-DD format). Defaults to None.
        expiration_date_gte (str, optional): Filter contracts with expiration date greater than or equal to this date (YYYY-MM-DD format). Defaults to None.
        expiration_date_lte (str, optional): Filter contracts with expiration date less than or equal to this date (YYYY-MM-DD format). Defaults to None.
        type (str, optional): Filter contracts by option type ('call' or 'put'). Defaults to None.
        style (str, optional): Filter contracts by style ('american' or 'european'). Defaults to None.
        limit (int, optional): Maximum number of contracts to return. Defaults to None.
        sort (str, optional): Sort order for results. Defaults to None.
        page_token (str, optional): Token for pagination to retrieve the next page of results. Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing a list of option contracts matching the filter criteria.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/options/contracts"
    else:
        pass

    params = {}
    if underlying_symbols:
        params["underlying_symbols"] = underlying_symbols
    if root_symbol:
        params["root_symbol"] = root_symbol
    if strike_price:
        params["strike_price"] = strike_price
    if expiration_date:
        params["expiration_date"] = expiration_date
    if expiration_date_gte:
        params["expiration_date.gte"] = expiration_date_gte
    if expiration_date_lte:
        params["expiration_date.lte"] = expiration_date_lte
    if type:
        params["type"] = type
    if style:
        params["style"] = style
    if limit:
        params["limit"] = limit
    if sort:
        params["sort"] = sort
    if page_token:
        params["page_token"] = page_token

    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


def get_option_contract_by_id_or_symbol(paper_trading: bool, symbol_or_contract_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/get-v2-options-contracts-symbol-or-contractid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        symbol_or_contract_id (str): The option contract symbol or contract ID.

    Returns:
        dict[str, any]: A dictionary containing the option contract details including strike price, expiration date, type, and style.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/options/contracts/{symbol_or_contract_id}"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


if __name__ == "__main__":
    print(get_option_contracts(paper_trading=True))
