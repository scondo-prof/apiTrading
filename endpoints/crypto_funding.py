import os
import sys

import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_crypto_funding_wallets(paper_trading: bool) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getwalletcryptofundings
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).

    Returns:
        dict[str, any]: A dictionary containing crypto funding wallet information.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/wallet/crypto/fundings"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def get_crypto_funding_transfers(paper_trading: bool, limit: int = None, offset: int = None) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getwalletcryptofundingstransfers
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        limit (int, optional): Maximum number of transfers to return. Defaults to None.
        offset (int, optional): Number of transfers to skip before returning results. Defaults to None.

    Returns:
        dict[str, any]: A dictionary containing a list of crypto funding transfers.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/wallet/crypto/fundings/transfers"
    else:
        pass

    params = {}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset

    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


def create_crypto_withdrawal(paper_trading: bool, withdrawal_data: dict) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/postwalletcryptofundingswithdrawals
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        withdrawal_data (dict): Dictionary containing withdrawal parameters such as symbol, amount, destination_address, etc.

    Returns:
        dict[str, any]: A dictionary containing information about the created crypto withdrawal request.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/wallet/crypto/fundings/withdrawals"
    else:
        pass

    response_json = httpx.request(method="POST", url=url, headers=headers, json=withdrawal_data).json()

    return response_json


def get_crypto_funding_transfer_by_id(paper_trading: bool, transfer_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getwalletcryptofundingstransferstransferid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        transfer_id (str): The unique identifier for the crypto funding transfer.

    Returns:
        dict[str, any]: A dictionary containing the detailed crypto funding transfer information.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/wallet/crypto/fundings/transfers/{transfer_id}"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def get_whitelisted_addresses(paper_trading: bool) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getwalletcryptoaddresses
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).

    Returns:
        dict[str, any]: A dictionary containing a list of whitelisted crypto addresses.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/wallet/crypto/addresses"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def create_whitelisted_address(paper_trading: bool, address_data: dict) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/postwalletcryptoaddresses
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        address_data (dict): Dictionary containing address parameters such as symbol, address, label, etc.

    Returns:
        dict[str, any]: A dictionary containing information about the created whitelisted address.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/wallet/crypto/addresses"
    else:
        pass

    response_json = httpx.request(method="POST", url=url, headers=headers, json=address_data).json()

    return response_json


def delete_whitelisted_address(paper_trading: bool, address_id: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/deletewalletcryptoaddressesaddressid
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        address_id (str): The unique identifier for the whitelisted address to delete.

    Returns:
        dict[str, any]: A dictionary containing confirmation of the deleted whitelisted address.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/wallet/crypto/addresses/{address_id}"
    else:
        pass

    response_json = httpx.request(method="DELETE", url=url, headers=headers).json()

    return response_json


def get_estimated_gas_fee(paper_trading: bool, symbol: str, destination_address: str, amount: str) -> dict[str, any]:
    """
    Link to Documentation: https://docs.alpaca.markets/reference/getwalletcryptofundingestimate
    Args:
        paper_trading (bool): Whether to use paper trading endpoint (True) or live trading endpoint (False).
        symbol (str): The cryptocurrency symbol (e.g., 'BTC', 'ETH').
        destination_address (str): The destination crypto address for the withdrawal.
        amount (str): The amount of cryptocurrency to withdraw.

    Returns:
        dict[str, any]: A dictionary containing the estimated gas fee for the proposed crypto withdrawal.
    """
    if paper_trading:
        url = f"{paper_trading_base_url}/wallet/crypto/fundings/estimate"
    else:
        pass

    params = {"symbol": symbol, "destination_address": destination_address, "amount": amount}

    response_json = httpx.request(method="GET", url=url, headers=headers, params=params).json()

    return response_json


if __name__ == "__main__":
    print(get_crypto_funding_wallets(paper_trading=True))
