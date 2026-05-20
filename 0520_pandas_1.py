import pandas as pd
stock1=pd.Series([120, 80, None , 60, 95, None , 110])
stock2=pd.Series([120, 80, None , 60, 95, None , 110],index=["Apple", "Banana", "Orange", "Mango", "Grape", "Peach", "Melon"])
stock3=([{'Apple': 120.0, 'Banana': 80.0, 'Orange': None, 'Mango': 60.0, 'Grape': 95.0, 'Peach': None, 'Melon': 110.0}])
print(stock1)
print(stock2)
print(stock3)
print("Banana 庫存: ", stock2["Banana"])
print("缺失值檢查")
print(stock2.isnull())
print("缺失數量",stock2.isnull().sum())

stock2.to_csv("0520_stock2.csv")