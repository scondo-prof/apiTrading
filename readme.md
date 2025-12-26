# Alpaca Trading API Wrapper

A modular Python wrapper for the Alpaca Markets Trading API, designed for easy deployment as serverless cloud functions with API Gateway integration.

## Purpose

This repository provides a clean, modular interface to interact with the Alpaca Trading API. It abstracts the HTTP request/response cycle into organized endpoint modules, making it easy to build trading applications, automate strategies, or integrate Alpaca's trading capabilities into larger systems.

## Repository Layout

The repository is structured to support serverless deployment patterns, particularly with cloud functions (AWS Lambda, Google Cloud Functions, Azure Functions) behind an API Gateway:

```
apiTrading/
├── config.py              # Configuration and API credentials management
├── main.py                # Example usage/demo script
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── endpoints/            # Modular endpoint modules
    ├── accounts.py
    ├── account_activities.py
    ├── account_configurations.py
    ├── assets.py
    ├── calendar.py
    ├── clock.py
    ├── corporate_actions.py
    ├── crypto_funding.py
    ├── option_contracts.py
    ├── orders.py
    ├── portfolio_history.py
    ├── positions.py
    └── watchlists.py
```

## Architecture: Cloud Functions & API Gateway Ready

This structure is specifically designed to be easily adopted by cloud functions with an API Gateway for several reasons:

1. **Modular Endpoints**: Each endpoint module is self-contained and can be deployed as an individual cloud function. This allows for:

   - Independent scaling of different API operations
   - Granular access control through API Gateway
   - Cost optimization by only invoking necessary functions
   - Easy maintenance and updates to specific endpoints

2. **Shared Configuration**: The `config.py` module centralizes API credentials and base URLs, allowing all endpoint functions to share the same configuration while maintaining flexibility for environment-specific settings.

3. **Stateless Design**: Each function is stateless and makes direct HTTP requests to Alpaca's API, making them perfect for serverless architectures where state management is not available.

4. **Independent Execution**: Each endpoint module can be imported and executed independently, allowing API Gateway routes to map directly to specific endpoint functions without dependencies on other modules.

5. **Minimal Dependencies**: The lightweight dependency footprint (primarily `httpx` for HTTP requests) ensures fast cold starts and efficient resource usage in cloud function environments.

## Repository Contents

### Configuration (`config.py`)

- Manages API authentication headers
- Configures base URLs for paper and live trading environments
- Loads environment variables for API credentials

### Endpoint Modules (`endpoints/`)

Each module corresponds to a group of related Alpaca API endpoints:

- **`accounts.py`**: Account information and details
- **`account_activities.py`**: Account activity history and transaction records
- **`account_configurations.py`**: Account settings and trading configurations
- **`assets.py`**: Asset information, symbols, and trading permissions
- **`calendar.py`**: Market calendar and trading days
- **`clock.py`**: Current market clock status
- **`corporate_actions.py`**: Corporate action announcements
- **`crypto_funding.py`**: Cryptocurrency funding operations and wallet management
- **`option_contracts.py`**: Options contract information and details
- **`orders.py`**: Order management (create, retrieve, update, cancel)
- **`portfolio_history.py`**: Portfolio performance and historical data
- **`positions.py`**: Position management and tracking
- **`watchlists.py`**: Watchlist creation and management

Each endpoint function includes:

- Comprehensive docstrings with links to Alpaca API documentation
- Parameter descriptions aligned with official API documentation
- Support for both paper trading and live trading environments
- Type hints for better code clarity and IDE support

### Example Usage (`main.py`)

Demonstrates basic usage patterns for the endpoint modules.

## Getting Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   Create a `.env` file with your Alpaca API credentials:

   ```
   APCA_API_KEY_ID=your_key_id
   APCA_API_SECRET_KEY=your_secret_key
   ```

3. Import and use endpoint modules:

   ```python
   from endpoints.accounts import get_the_account

   account_info = get_the_account(paper_trading=True)
   print(account_info)
   ```

## Cloud Function Deployment Example

Each endpoint module can be deployed as a separate cloud function. For example, an AWS Lambda function for getting account information:

```python
from endpoints.accounts import get_the_account

def lambda_handler(event, context):
    paper_trading = event.get('paper_trading', True)
    result = get_the_account(paper_trading=paper_trading)
    return {
        'statusCode': 200,
        'body': result
    }
```

## Documentation

Each function includes detailed docstrings with:

- Links to the corresponding Alpaca API documentation
- Parameter descriptions
- Return value documentation

For the complete Alpaca API documentation, visit: [https://docs.alpaca.markets/](https://docs.alpaca.markets/)

## License

This project is provided as-is for use with the Alpaca Markets API.
