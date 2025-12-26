import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_account_activities(
    paper_trading: bool,
    activity_type: str = None,
    date: str = None,
    until: str = None,
    after: str = None,
    direction: str = None,
    page_size: int = None,
) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getaccountactivities
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        activity_type (str, optional): Filter by activity type (e.g., 'FILL', 'TRANS', 'DIV', etc.). Defaults to None.
        date (str, optional): Filter activities for a specific date (YYYY-MM-DD format). Defaults to None.
        until (str, optional): Filter activities up to this date (ISO 8601 format). Defaults to None.
        after (str, optional): Filter activities after this date (ISO 8601 format). Defaults to None.
        direction (str, optional): The chronological order of response based on the submission time. 'asc' or 'desc'. Defaults to None.
        page_size (int, optional): Maximum number of entries in the response. Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing account activities data.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/account/activities"
    else:
        pass

    params = {}
    if activity_type:
        params["activity_type"] = activity_type
    if date:
        params["date"] = date
    if until:
        params["until"] = until
    if after:
        params["after"] = after
    if direction:
        params["direction"] = direction
    if page_size:
        params["page_size"] = page_size

    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


def get_account_activities_by_type(
    paper_trading: bool,
    activity_type: str,
    date: str = None,
    until: str = None,
    after: str = None,
    direction: str = None,
    page_size: int = None,
) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getaccountactivitiesactivitytype
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        activity_type (str): The specific activity type to filter by (e.g., 'FILL', 'TRANS', 'DIV', etc.).
        date (str, optional): Filter activities for a specific date (YYYY-MM-DD format). Defaults to None.
        until (str, optional): Filter activities up to this date (ISO 8601 format). Defaults to None.
        after (str, optional): Filter activities after this date (ISO 8601 format). Defaults to None.
        direction (str, optional): The chronological order of response based on the submission time. 'asc' or 'desc'. Defaults to None.
        page_size (int, optional): Maximum number of entries in the response. Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing account activities data for the specified activity type.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/account/activities/{activity_type}"
    else:
        pass

    params = {}
    if date:
        params["date"] = date
    if until:
        params["until"] = until
    if after:
        params["after"] = after
    if direction:
        params["direction"] = direction
    if page_size:
        params["page_size"] = page_size

    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


if __name__ == "__main__":
    print(get_account_activities(paper_trading=True))
