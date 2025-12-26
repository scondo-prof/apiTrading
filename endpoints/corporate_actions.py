import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_announcements(
    paper_trading: bool,
    ca_types: str = None,
    symbols: str = None,
    since: str = None,
    until: str = None,
    cusip: str = None,
    date_type: str = None,
) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getcorporateactionsannouncements
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        ca_types (str, optional): Comma-separated list of corporate action types to filter by. Defaults to None.
        symbols (str, optional): Comma-separated list of symbols to filter by. Defaults to None.
        since (str, optional): Filter announcements since this date (ISO 8601 format). Defaults to None.
        until (str, optional): Filter announcements until this date (ISO 8601 format). Defaults to None.
        cusip (str, optional): Filter by CUSIP identifier. Defaults to None.
        date_type (str, optional): Filter by date type (e.g., 'declaration_date', 'ex_date', 'record_date', 'payable_date'). Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing corporate action announcements matching the filter criteria.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/corporate_actions/announcements"
    else:
        pass

    params = {}
    if ca_types:
        params["ca_types"] = ca_types
    if symbols:
        params["symbols"] = symbols
    if since:
        params["since"] = since
    if until:
        params["until"] = until
    if cusip:
        params["cusip"] = cusip
    if date_type:
        params["date_type"] = date_type

    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


def get_announcement_by_id(paper_trading: bool, announcement_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getcorporateactionsannouncementsid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        announcement_id (str): The unique identifier for the corporate action announcement.

    Returns:
        dict[str, any]: A dictionary containing the detailed corporate action announcement information.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/corporate_actions/announcements/{announcement_id}"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


if __name__ == "__main__":
    print(get_announcements(paper_trading=True))
