import yfinance as yf
import pandas as pd

# 여러 종목 시세 데이터 다운로드
data = yf.download(
    tickers = [
        'MSFT',
    ]
    , start = "1986-03-13"
    , end = '2024-07-07' 
    , interval = '1d'
)
print(data
      ,type(data)
      ,sep = '\n')


data.to_csv(r'C:\Users\brian\Desktop\JUNSOO\de_2024\data\msftFinance.csv' , encoding = "euc-kr")


