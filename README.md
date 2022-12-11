# Financial Planning Tool
Prototype application to support the assessment of Personal Finances, and forecast adequate Retirement Plans based on 
cryptocurrencies, stocks, and bonds.

## Personal Finance Planner
Use this tool to visualize an individual's savings composed by investments in shares and cryptocurrencies, and determine 
if the money saved thus far is enough as an emergency fund.

## Retirement Planning Tool
Given an in initial investment amount, use this tool to fetch historical closing prices for a retirement portfolio 
composed of stocks and bonds. Then visualise the projected performance of the portfolio at 30 years.

## Assumptions
- The average household income for each individual is $12,000.
- Every individual has a savings portfolio composed of cryptocurrencies, stocks and bonds:
  - Amount of crypto assets: `1.2` BTC and `5.3` ETH. 
  - Amount of shares in stocks and bonds: `50` SPY (stocks) and `200` AGG (bonds).
- An ideal Emergency Fund should be equal to three times the monthly income.
- Retirement calculations based on an initial investment of `$20,000` at `30` years for a `40/60` portfolio: `60%` in 
  stocks (`SPY`) and `40%` in bonds (`AGG`).
- Early Retirement calculations based on a larger initial investment at `5` and `10` years for a more aggressive portfolio 
  strategy.

## Technical Environment
This tool utilises two APIs:
- The **Alpaca Markets API** to pull historical stocks and bonds information. [AlpacaDOCS](https://alpaca.markets/docs/)
- The **Alternative Free Crypto API** to retrieve Bitcoin and Ethereum prices. [Documentation](https://alternative.me/crypto/api/)

And the [MCForecastTools toolkit](Resources/MCForecastTools.py)

### API keys
Please note this tool requires API keys to perform successful operations with the Alpaca Markets and Alternative Free 
Crypto APIs. After you clone this repository and check out this code, you must create an `.env` file on the root directory 
with the corresponding keys.

Sample `.env` file:
```
ALPACA_API_KEY="YOUR_KEY_HERE"
ALPACA_SECRET_KEY="YOUR_KEY_HERE"
```