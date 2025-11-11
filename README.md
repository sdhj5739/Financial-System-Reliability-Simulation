# Financial System Reliability Simulation

This project explores how **financial market volatility** affects **system reliability** using principles from **systems engineering** and **data analytics**.

---

## Overview
- Downloads real stock data using the Yahoo Finance API (`yfinance`)
- Simulates probabilistic system failures based on market volatility
- Calculates key reliability metrics:
  - Uptime Ratio  
  - Failure Rate  
  - Mean Time Between Failures (MTBF)
- Models reliability decay \( R(t) = e^{-λt} \)
- Visualizes trends in reliability and volatility

---

## Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- yFinance  

---

## How to Run

1. Clone or download this repository  
2. Install required packages:
   ```bash
   pip install yfinance pandas numpy matplotlib
