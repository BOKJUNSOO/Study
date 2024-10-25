#6) 비행탑승 경험 만족도 데이터
# target : satisfaction
# column drop . false

import pandas as pd
pd.options.display.max_columns = None

x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_test.csv")

# split id 
y_train_id = y_train["ID"]

x_train.drop(columns = ["ID","id"], inplace= True)
y_train.drop(columns = "ID", inplace= True)
x_test.drop(columns = ["ID","id"], inplace= True)

# object class
list = ["Gender","Customer Type","Type of Travel","Class"]

# encoder
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

for i in list:
    x_train[i] = pd.Series(encoder.fit_transform(x_train[i]))
    x_test[i] = pd.Series(encoder.fit_transform(x_train[i]))

y_train["satisfaction"] = pd.Series(encoder.fit_transform(y_train["satisfaction"]))

# null sum
mean = x_train["Arrival Delay in Minutes"].mean()
x_train["Arrival Delay in Minutes"] = x_train["Arrival Delay in Minutes"].fillna(mean)

mean = x_test["Arrival Delay in Minutes"].mean()
x_test["Arrival Delay in Minutes"] = x_test["Arrival Delay in Minutes"].fillna(mean)

# scaler
from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler = MinMaxScaler()
temp = x_train[["Flight Distance"]]
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_dis"})
x_train = pd.concat([x_train,temp], axis = 1)
x_train = x_train.drop(columns = "Flight Distance")

temp = x_test[["Flight Distance"]]
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_dis"})
x_test = pd.concat([x_test,temp], axis = 1)
x_test = x_test.drop(columns = "Flight Distance")

# split
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train,y_train,test_size= 0.3, random_state = 2024)


## model training
from sklearn.metrics import roc_auc_score

# Random Forest
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_TRAIN,Y_TRAIN)
y_test_pre = pd.DataFrame(model.predict(x_test)).rename(columns = {0:"satisfaction"}) #result

# model test
Y_PRE = pd.DataFrame(model.predict(X_TEST))
print("this is RandomForest: ",roc_auc_score(Y_TEST,Y_PRE))

# XGBOOST
from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(X_TRAIN,Y_TRAIN)
y_pre = pd.DataFrame(model.predict(x_test)).rename(columns = {0:"satisfaction"}) # result
Y_PRE = pd.DataFrame(model.predict(X_TEST))
print("this is xgboost:", roc_auc_score(Y_TEST,Y_PRE))

# select xgboost
result = pd.concat([y_train_id,y_pre],axis=1)
result = result.replace(0,"neutral or dissatisfied").replace(1,"satisfied")
# result.to_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\KaggleGit\분류\gogo.csv",index = True)


print("code is work")


