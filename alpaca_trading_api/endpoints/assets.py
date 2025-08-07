import json
import os
import sys

from dotenv import load_dotenv
import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import headers, paper_trading_base_url, trading_base_url


def get_assets(
    status: str = "Active",
    asset_class: str = "us_equity",
    exchange: str = "NYSE",
    attributes: list[str] = ["ptp_no_exception", "ptp_with_exception", "ipo", "has_options", "options_late_close"],
    paper_trading: bool = True,
) -> list[dict[str, any]]:
    if paper_trading:
        url: str = (
            f"{paper_trading_base_url}/assets?status={status};exchange={exchange};attributes={attributes};asset_class={asset_class}"
        )
    else:
        url: str = (
            f"{trading_base_url}/assets?status={status},asset_class={asset_class},exchange={exchange},attributes={attributes}"
        )

    response_json: list[dict[str, any]] = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def get_asset_by_id_or_symbol(symbol_or_asset_id: str, paper_trading: bool = True) -> dict[str, any]:
    if paper_trading:
        url: str = f"{paper_trading_base_url}/assets/{symbol_or_asset_id}"
    else:
        url: str = f"{trading_base_url}/assets/{symbol_or_asset_id}"

    response_json: dict[str, any] = httpx.request(method="GET", url=url, headers=headers).json()

    return response_json


def get_option_contracts(
    underlying_symbols: str,
    root_symbol: str,
    paper_trading: bool = True,
    show_deliverables: bool = True,
    status: str = "active",
    expiration_date: str = None,
    expiration_date_gte: str = None,
    expiration_date_lte: str = None,
    type: str = "call",
    style: str = "american",
    strike_price_gte: int = None,
    strike_price_lte: int = None,
    page_token: str = None,
    limit: int = 100,
    ppind: bool = None,
) -> dict[str, any]:
    if paper_trading:
        url: str = f"{paper_trading_base_url}/options/contracts?underlying_symbols={underlying_symbols};root_symbol={root_symbol};paper_trading={paper_trading};show_deliverables={show_deliverables};status={status};type={type};style={style};limit={limit};"

    else:
        url: str = f"{trading_base_url}/options/contracts?underlying_symbols={underlying_symbols};root_symbol={root_symbol};paper_trading={paper_trading};show_deliverables={show_deliverables};status={status};type={type};style={style};limit={limit};"

    request_json = httpx.request(method="GET", url=url, headers=headers).json()

    with open("test.json", "w") as test_file:
        test_file.write(json.dumps(request_json))

    test_file.close()
    return request_json


def get_option_contract_by_id_or_symbol():
    pass


def get_us_treasuries():
    pass


if __name__ == "__main__":
    # print(
    #     get_assets()
    # )

    # print(get_asset_by_id_or_symbol(symbol_or_asset_id="BCH/USD", paper_trading=True))
