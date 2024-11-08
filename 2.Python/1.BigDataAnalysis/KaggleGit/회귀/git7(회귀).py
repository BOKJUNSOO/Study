import pandas as pd

pd.options.display.max_columns = None

x_train = pd.read_csv(r"https://raw.githubusercontent.com/Datamanim/datarepo/main/hyundai/x_train.csv")
y_train = pd.read_csv(r"https://raw.githubusercontent.com/Datamanim/datarepo/main/hyundai/y_train.csv")
x_test= pd.read_csv(r"https://raw.githubusercontent.com/Datamanim/datarepo/main/hyundai/x_test.csv")

y_id = y_train["ID"]
y_train = y_train.drop(columns = "ID")
x_train = x_train.drop(columns = "ID")
x_test = x_test.drop(columns = "ID")

print(x_train.head())