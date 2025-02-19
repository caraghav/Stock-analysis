# -*- coding: utf-8 -*-
"""Copy of app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-YDmJEIjSIDhoi8ndPXYTo9YiHKbXZUO
"""

pip install streamlit yfinance pandas

import streamlit as st
import yfinance as yf
import pandas as pd

# Streamlit App Title
st.title("📈 Stock Fundamental Analysis App")

# User input for stock symbol
ticker = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL, TSLA, MSFT):", "AAPL")

# Fetch Stock Data from Yahoo Finance
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    financials = {
        "Company Name": info.get("longName", "N/A"),
        "Market Cap": info.get("marketCap", "N/A"),
        "Current Price": info.get("currentPrice", "N/A"),
        "EPS (Earnings Per Share)": info.get("trailingEps", "N/A"),
        "P/E Ratio": info.get("trailingPE", "N/A"),
        "Dividend Yield": info.get("dividendYield", "N/A"),
        "Revenue": info.get("totalRevenue", "N/A"),
        "Net Income": info.get("netIncomeToCommon", "N/A"),
        "Book Value": info.get("bookValue", "N/A"),
        "Debt to Equity Ratio": info.get("debtToEquity", "N/A"),
        "52-Week High": info.get("fiftyTwoWeekHigh", "N/A"),
        "52-Week Low": info.get("fiftyTwoWeekLow", "N/A"),
    }
    return financials

# Display the fetched data
if st.button("Analyze Stock"):
    try:
        stock_data = fetch_stock_data(ticker)
        st.subheader(f"📊 Fundamental Analysis for {ticker}")
        df = pd.DataFrame(stock_data.items(), columns=["Metric", "Value"])
        st.table(df)

        # Financial Analysis Insights
        st.subheader("📌 Key Insights")
        if stock_data["P/E Ratio"] != "N/A" and stock_data["EPS (Earnings Per Share)"] != "N/A":
            if stock_data["P/E Ratio"] < 15:
                st.success("✅ The stock is undervalued based on P/E ratio.")
            elif stock_data["P/E Ratio"] > 25:
                st.warning("⚠️ The stock may be overvalued based on P/E ratio.")
            else:
                st.info("ℹ️ The stock is fairly valued.")

        if stock_data["Dividend Yield"] != "N/A":
            if stock_data["Dividend Yield"] > 0.02:
                st.success("✅ This stock has a good dividend yield.")
            else:
                st.warning("⚠️ Low dividend yield, consider other investments if dividends matter.")

        if stock_data["Debt to Equity Ratio"] != "N/A" and stock_data["Debt to Equity Ratio"] > 1:
            st.error("⚠️ High debt-to-equity ratio, indicating financial risk.")

    except Exception as e:
        st.error(f"Error fetching data: {e}")

# Footer
st.markdown("💡 *Data sourced from Yahoo Finance. Always do your own research before investing.*")

git status


