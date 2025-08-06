import os
import sys

from dotenv import load_dotenv
import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url, trading_base_url


def get_the_account(paper_trading: bool) -> dict[str, any]:
    if paper_trading:
        url: str = f"{paper_trading_base_url}/account"
    else:
        url: str = f"{trading_base_url}/account"

    response_json: dict[str, any] = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


if __name__ == "__main__":
    print(get_the_account(paper_trading=True))
