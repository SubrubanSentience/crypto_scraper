#!/usr/bin/env python3
"""
crypto_scraper.py
Author: Jacob Peters (Subruban Sentience)
Description: CLI tool to fetch real-time cryptocurrency prices using CoinGecko API.
"""

import argparse
import requests
import pandas as pd
import datetime
import sys
import json

def fetch_prices(crypto_ids):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(crypto_ids),
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None
    return response.json()

def fetch_top_coins(n):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": n,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("❌ Failed to fetch top coins")
        sys.exit(1)
    data = response.json()
    return [coin['id'] for coin in data]

def save_to_csv(data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"crypto_prices_{timestamp}.csv"
    
    df = pd.DataFrame([
        {"Cryptocurrency": key.upper(), "Price (USD)": value["usd"]}
        for key, value in data.items()
    ])
    
    df.to_csv(filename, index=False)
    print(f"✅ Saved to {filename}")

def save_to_json(data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"crypto_prices_{timestamp}.json"
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"✅ Saved to {filename}")

def main():
    parser = argparse.ArgumentParser(
        description="📈 Real-time Crypto Price Scraper using CoinGecko API"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--coins", nargs="+",
        help="List of cryptocurrency IDs (e.g., bitcoin ethereum dogecoin)"
    )
    group.add_argument(
        "--top", type=int, metavar="N",
        help="Fetch top N cryptocurrencies by market cap"
    )
    parser.add_argument(
        "--no-csv", action="store_true",
        help="Don't save to CSV or JSON, just print to terminal"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Save output to JSON instead of CSV"
    )

    args = parser.parse_args()

    if args.top:
        crypto_ids = fetch_top_coins(args.top)
    else:
        if not args.coins:
            print("❌ Please specify coin IDs or use --top")
            sys.exit(1)
        crypto_ids = args.coins

    data = fetch_prices(crypto_ids)

    if not data:
        print("❌ No data returned. Check your coin IDs.")
        sys.exit(1)

    print("\n🪙 Real-Time Prices (USD):")
    for coin, info in data.items():
        print(f"  {coin.upper():<12} - ${info['usd']:,.2f}")

    if not args.no_csv:
        if args.json:
            save_to_json(data)
        else:
            save_to_csv(data)

if __name__ == "__main__":
    main()
