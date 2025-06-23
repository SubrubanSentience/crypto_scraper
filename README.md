# 🪙 Crypto Price Scraper

A simple yet powerful command-line tool that fetches real-time cryptocurrency prices using the [CoinGecko API](https://www.coingecko.com/en/api). Built with Python, this tool is ideal for crypto enthusiasts, analysts, and freelance clients who need quick and structured price data.

---

## 🚀 Features

- ✅ Get prices for **any coin** supported by CoinGecko
- ✅ Fetch **top N coins** by market cap (`--top`)
- ✅ Output to **CSV or JSON** format
- ✅ CLI-friendly with **custom flags**
- ✅ Saves files with **timestamped filenames**

---

## 🧪 Example Usage

### 📌 Get prices for specific coins

```bash
python crypto_scraper.py --coins bitcoin ethereum dogecoin

python crypto_scraper.py --top 10

python crypto_scraper.py --coins bitcoin ethereum --json

python crypto_scraper.py --top 5 --no-csv

MIT License © 2025 Jacob Peters — Subruban Sentience

