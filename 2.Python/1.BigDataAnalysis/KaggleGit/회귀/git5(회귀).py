# 대학원 입학 가능성 데이터
import pandas as pd
pd.options.display.max_columns = None
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/admission/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/admission/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/admission/x_test.csv")

y_test_id = y_train["ID"]
x_train = x_train.drop(columns = "ID")
x_test = x_test.drop(columns = "ID")
y_train = y_train.drop(columns = "ID")

# encoding
list = ["Research"]

# scaler
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
scaler_list = ["GRE Score","TOEFL Score"]
temp = x_train[scaler_list]
scaler = MinMaxScaler()
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_gre",
                                                                  1:"new_tofel"})
x_train = pd.concat([x_train,temp], axis = 1)
x_train = x_train.drop(columns = scaler_list)

temp = x_test[scaler_list]
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_gre",
                                                                  1:"new_tofel"})
x_test = pd.concat([x_test,temp], axis = 1)
x_test = x_test.drop(columns = scaler_list)

x_train = x_train.drop(columns = "Serial No.")
x_test = x_test.drop(columns = "Serial No.")


from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST , Y_TRAIN, Y_TEST = train_test_split(x_train, y_train, test_size = 0.3 , random_state= 2024)

from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
#
model1 = RandomForestRegressor()
model1.fit(X_TRAIN,Y_TRAIN)
y_test_pre = pd.DataFrame(model1.predict(x_test)).rename(columns = {0:"goal"})
Y_PRE = pd.DataFrame(model1.predict(X_TEST)).rename(columns = {0:"goal"})
label = pd.DataFrame(model1.predict(X_TRAIN)).rename(columns = {0:"goal"})
#
model2 = XGBRegressor()
model2.fit(X_TRAIN,Y_TRAIN)
y_test_pre2 = pd.DataFrame(model2.predict(x_test)).rename(columns = {0:"goal"})
Y_PRE2 = pd.DataFrame(model2.predict(X_TEST)).rename(columns = {0:"goal"})
label2 = pd.DataFrame(model2.predict(X_TRAIN)).rename(columns = {0:"goal"})

from sklearn.metrics import r2_score
print("RandomForest label score :",r2_score(label,Y_TRAIN))
print("RandomForest model score :",r2_score(Y_TEST,Y_PRE))
print()
print("XGBOOST label score :", r2_score(label2,Y_TRAIN))
print("XGBOOST model score :", r2_score(Y_TEST, Y_PRE2))





