import os
import sys

from dotenv import load_dotenv
import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url


def get_the_account(paper_trading: bool) -> dict[str, any]:
    if paper_trading:
        url = f"{paper_trading_base_url}/account"
    else:
        pass

    response_json = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


if __name__ == "__main__":
    print(get_the_account(paper_trading=True))
