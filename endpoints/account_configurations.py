import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_account_configurations(paper_trading: bool) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getaccountconfigurations
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).

    Returns:
        dict[str, any]: A dictionary containing account configuration settings including day trading buying power, fractional trading, etc.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/account/configurations"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def update_account_configurations(paper_trading: bool, config_data: dict) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/patchaccountconfigurations
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        config_data (dict): Dictionary containing configuration parameters to update (e.g., dtbp_check, fractional_trading, etc.).

    Returns:
        dict[str, any]: A dictionary containing the updated account configuration settings.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/account/configurations"
    else:
        pass

    response_json = httpx.request(method="PATCH", url=url, headers=headers, json=config_data).json()

    return response_json


if __name__ == "__main__":
    print(get_account_configurations(paper_trading=True))
