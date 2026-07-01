<div align="center">

![image alt](https://github.com/vivekrajput22/CodeAlpha_Stock-Portfolio-Tracker/blob/b1552dc253d7164c9251ba83f2d84282165fe80d/banner.png)

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/Type-CLI%20Tool-orange?style=for-the-badge)

*No external libraries. No API keys. Just pure Python.*

</div>

---

## ✨ Features

| | |
|---|---|
| 💰 | Hardcoded dictionary of stock symbols & prices |
| ⌨️ | Interactive input — enter symbols & quantities on the fly |
| 🧮 | Automatic value & total investment calculation |
| 🖥️ | Clean, formatted console summary |
| 💾 | Export results to `.txt` or `.csv` |

---

## 🧠 How It Works

<div align="center">
<img src="images/flow_diagram.png" alt="Program flow diagram" width="100%"/>
</div>

## 🔑 Key Concepts Used

```
📦 Dictionaries    →  storing stock prices & building the portfolio
🔄 Input / Output  →  reading input, printing formatted output
➕ Arithmetic       →  price × quantity, running totals
📁 File Handling   →  writing .txt and .csv output files
```

---

## ⚙️ Requirements

- 🐍 **Python 3.6+**
- 📚 Built-in modules only — `csv`, `datetime` (nothing to `pip install`!)

---

## 🚀 How to Run

**1️⃣ Open a terminal** in the folder containing `stock_portfolio_tracker.py`

**2️⃣ Run the script**

```bash
python3 stock_portfolio_tracker.py
```

**3️⃣ Follow the prompts**

- 📋 View the list of available stocks & prices
- ✍️ Enter a stock symbol (e.g. `AAPL`), then its quantity
- 🔁 Repeat for as many stocks as you like
- ✅ Type `done` when finished
- 💾 Choose to save as `txt`, `csv`, or skip

---

## 🎬 Example Session

<div align="center">
<img src="images/terminal_demo.png" alt="Terminal demo screenshot" width="650"/>
</div>

<details>
<summary>📄 View as plain text</summary>

```text
Enter stock symbol (or 'done' to finish): AAPL
Enter quantity of AAPL: 10
  ✔ Added 10 share(s) of AAPL.

Enter stock symbol (or 'done' to finish): TSLA
Enter quantity of TSLA: 5
  ✔ Added 5 share(s) of TSLA.

Enter stock symbol (or 'done' to finish): done

═════════════════════════════════════════════
 PORTFOLIO SUMMARY
═════════════════════════════════════════════
Symbol  Qty     Price     Value
─────────────────────────────────────────────
AAPL    10      $180      $1800
TSLA    5       $250      $1250
─────────────────────────────────────────────
💰 TOTAL INVESTMENT VALUE: $3,050.00
═════════════════════════════════════════════

Save results to a file? (txt / csv / no): txt
✔ Summary saved to 'portfolio_summary.txt'
```

</details>

---

## 🏷️ Available Stock Symbols

| Symbol | Price / Share |
|:------:|:--------------:|
| 🍎 AAPL  | $180 |
| ⚡ TSLA  | $250 |
| 🔍 GOOGL | $140 |
| 🪟 MSFT  | $410 |
| 📦 AMZN  | $185 |
| 🎬 NFLX  | $640 |
| 📘 META  | $480 |

> ✏️ Want more stocks? See [Customizing Stock Prices](#-customizing-stock-prices) below.

---

## 🛠️ Customizing Stock Prices

Edit the `STOCK_PRICES` dictionary near the top of `stock_portfolio_tracker.py`:

```python
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    # add more here...
}
```

---

## 📂 Output Files

| File | Description |
|------|--------------|
| 📝 `portfolio_summary.txt` | Plain-text summary with timestamp |
| 📊 `portfolio_summary.csv` | Spreadsheet-friendly CSV with a total row |

<div align="center">
<img src="images/output_preview.png" alt="Sample CSV and TXT output preview" width="100%"/>
</div>

Both files are saved in the same folder where the script is run.

---

## 💡 Possible Extensions

- 🌐 Pull live stock prices from a real API
- 📅 Track purchase dates & calculate gain/loss over time
- 💱 Support multiple currencies
- 🖼️ Build a GUI using `tkinter`

---

<div align="center">

**Made with 🐍 Python — Happy Investing! 📈**

</div>
