import os
import sys

from dotenv import load_dotenv
import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url, trading_base_url


def get_assets(
    status: str, asset_class: str, exchange: str, attributes: list[str], paper_trading: bool
) -> dict[str, any]:
    if paper_trading:
        url: str = (
            f"{paper_trading_base_url}/assets?status={status};exchange={exchange};attributes={attributes};asset_class={asset_class}"
        )
    else:
        url: str = (
            f"{trading_base_url}/assets?status={status},asset_class={asset_class},exchange={exchange},attributes={attributes}"
        )

    response_json: dict[str, any] = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def get_asset_by_id_or_symbol():
    pass


def get_option_contracts():
    pass


def get_option_contract_by_id_or_symbol():
    pass


def get_us_treasuries():
    pass


if __name__ == "__main__":
    print(
        get_assets(
            status="active",
            asset_class="us_equity",
            exchange="NYSE",
            attributes=["ptp_no_exception", "ptp_with_exception", "ipo", "has_options", "options_late_close"],
            paper_trading=True,
        )
    )
