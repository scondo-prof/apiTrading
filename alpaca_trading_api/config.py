import os

from dotenv import load_dotenv

load_dotenv()

headers: dict[str, str] = {
    "APCA-API-KEY-ID": os.getenv("APCA_API_KEY_ID"),
    "APCA-API-SECRET-KEY": os.getenv("APCA_API_SECRET_KEY"),
}

paper_trading_base_url: str = "https://paper-api.alpaca.markets/v2"

trading_base_url: str = "https://api.alpaca.markets/v2"
