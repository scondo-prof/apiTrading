import httpx

from alpaca_trading_api.config import headers, paper_trading_base_url

if __name__ == "__main__":
    print("start")

    response = httpx.request(method="GET", url=f"{paper_trading_base_url}/account", headers=headers).json()

    print(f"Response = {response}")
