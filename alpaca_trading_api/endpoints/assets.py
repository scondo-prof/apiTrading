import os
import sys

from dotenv import load_dotenv
import httpx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from alpaca_trading_api.config import headers, paper_trading_base_url


def get_assets():
    pass


def get_asset_by_id_or_symbol():
    pass


def get_option_contracts():
    pass


def get_option_contract_by_id_or_symbol():
    pass


def get__us_treasuries():
    pass
