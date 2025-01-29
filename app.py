{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5eLRreprHR4BUKUDeSe/8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/caraghav/Stock-analysis/blob/main/app.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TVm4UlqnXasG",
        "outputId": "fe01b444-65fb-4b95-e84e-bb6bcb763589"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.41.1-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Requirement already satisfied: yfinance in /usr/local/lib/python3.11/dist-packages (0.2.52)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.11/dist-packages (2.2.2)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.1)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.1.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.25.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (17.0.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (13.9.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.3.3)\n",
            "Requirement already satisfied: multitasking>=0.0.7 in /usr/local/lib/python3.11/dist-packages (from yfinance) (0.0.11)\n",
            "Requirement already satisfied: lxml>=4.9.1 in /usr/local/lib/python3.11/dist-packages (from yfinance) (5.3.0)\n",
            "Requirement already satisfied: platformdirs>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from yfinance) (4.3.6)\n",
            "Requirement already satisfied: pytz>=2022.5 in /usr/local/lib/python3.11/dist-packages (from yfinance) (2024.2)\n",
            "Requirement already satisfied: frozendict>=2.3.4 in /usr/local/lib/python3.11/dist-packages (from yfinance) (2.4.6)\n",
            "Requirement already satisfied: peewee>=3.16.2 in /usr/local/lib/python3.11/dist-packages (from yfinance) (3.17.8)\n",
            "Requirement already satisfied: beautifulsoup4>=4.11.1 in /usr/local/lib/python3.11/dist-packages (from yfinance) (4.12.3)\n",
            "Requirement already satisfied: html5lib>=1.1 in /usr/local/lib/python3.11/dist-packages (from yfinance) (1.1)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.1)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.5)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.23.0)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.11/dist-packages (from beautifulsoup4>=4.11.1->yfinance) (2.6)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.11/dist-packages (from html5lib>=1.1->yfinance) (1.17.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.11/dist-packages (from html5lib>=1.1->yfinance) (0.5.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2024.12.14)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.22.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Downloading streamlit-1.41.1-py2.py3-none-any.whl (9.1 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.1/9.1 MB\u001b[0m \u001b[31m39.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m34.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m5.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.41.1 watchdog-6.0.0\n"
          ]
        }
      ],
      "source": [
        "pip install streamlit yfinance pandas"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import yfinance as yf\n",
        "import pandas as pd\n",
        "\n",
        "# Streamlit App Title\n",
        "st.title(\"📈 Stock Fundamental Analysis App\")\n",
        "\n",
        "# User input for stock symbol\n",
        "ticker = st.text_input(\"Enter Stock Ticker Symbol (e.g., AAPL, TSLA, MSFT):\", \"AAPL\")\n",
        "\n",
        "# Fetch Stock Data from Yahoo Finance\n",
        "def fetch_stock_data(ticker):\n",
        "    stock = yf.Ticker(ticker)\n",
        "    info = stock.info\n",
        "    financials = {\n",
        "        \"Company Name\": info.get(\"longName\", \"N/A\"),\n",
        "        \"Market Cap\": info.get(\"marketCap\", \"N/A\"),\n",
        "        \"Current Price\": info.get(\"currentPrice\", \"N/A\"),\n",
        "        \"EPS (Earnings Per Share)\": info.get(\"trailingEps\", \"N/A\"),\n",
        "        \"P/E Ratio\": info.get(\"trailingPE\", \"N/A\"),\n",
        "        \"Dividend Yield\": info.get(\"dividendYield\", \"N/A\"),\n",
        "        \"Revenue\": info.get(\"totalRevenue\", \"N/A\"),\n",
        "        \"Net Income\": info.get(\"netIncomeToCommon\", \"N/A\"),\n",
        "        \"Book Value\": info.get(\"bookValue\", \"N/A\"),\n",
        "        \"Debt to Equity Ratio\": info.get(\"debtToEquity\", \"N/A\"),\n",
        "        \"52-Week High\": info.get(\"fiftyTwoWeekHigh\", \"N/A\"),\n",
        "        \"52-Week Low\": info.get(\"fiftyTwoWeekLow\", \"N/A\"),\n",
        "    }\n",
        "    return financials\n",
        "\n",
        "# Display the fetched data\n",
        "if st.button(\"Analyze Stock\"):\n",
        "    try:\n",
        "        stock_data = fetch_stock_data(ticker)\n",
        "        st.subheader(f\"📊 Fundamental Analysis for {ticker}\")\n",
        "        df = pd.DataFrame(stock_data.items(), columns=[\"Metric\", \"Value\"])\n",
        "        st.table(df)\n",
        "\n",
        "        # Financial Analysis Insights\n",
        "        st.subheader(\"📌 Key Insights\")\n",
        "        if stock_data[\"P/E Ratio\"] != \"N/A\" and stock_data[\"EPS (Earnings Per Share)\"] != \"N/A\":\n",
        "            if stock_data[\"P/E Ratio\"] < 15:\n",
        "                st.success(\"✅ The stock is undervalued based on P/E ratio.\")\n",
        "            elif stock_data[\"P/E Ratio\"] > 25:\n",
        "                st.warning(\"⚠️ The stock may be overvalued based on P/E ratio.\")\n",
        "            else:\n",
        "                st.info(\"ℹ️ The stock is fairly valued.\")\n",
        "\n",
        "        if stock_data[\"Dividend Yield\"] != \"N/A\":\n",
        "            if stock_data[\"Dividend Yield\"] > 0.02:\n",
        "                st.success(\"✅ This stock has a good dividend yield.\")\n",
        "            else:\n",
        "                st.warning(\"⚠️ Low dividend yield, consider other investments if dividends matter.\")\n",
        "\n",
        "        if stock_data[\"Debt to Equity Ratio\"] != \"N/A\" and stock_data[\"Debt to Equity Ratio\"] > 1:\n",
        "            st.error(\"⚠️ High debt-to-equity ratio, indicating financial risk.\")\n",
        "\n",
        "    except Exception as e:\n",
        "        st.error(f\"Error fetching data: {e}\")\n",
        "\n",
        "# Footer\n",
        "st.markdown(\"💡 *Data sourced from Yahoo Finance. Always do your own research before investing.*\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "phqMz9WsXpSz",
        "outputId": "fe800761-e33a-4dbe-cafc-43c36481e91e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-01-29 09:23:07.940 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.122 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-01-29 09:23:08.124 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.128 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.130 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.132 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.134 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.135 Session state does not function when running a script without `streamlit run`\n",
            "2025-01-29 09:23:08.136 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.137 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.139 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.140 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.143 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.144 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.145 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.147 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-01-29 09:23:08.148 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "git status"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 109
        },
        "id": "JXgGUq6IYNDY",
        "outputId": "7ae45258-34f2-4be8-c343-50ba531cab49"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-3-d93c8dd246e3>, line 1)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-3-d93c8dd246e3>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    git status\u001b[0m\n\u001b[0m        ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "uWDUv0gYY1vc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "5hZ3QNP0ZC97"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
