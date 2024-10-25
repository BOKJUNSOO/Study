# 킹카운티 주거지 가격예측
import pandas as pd

pd.options.display.max_columns = None
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/kingcountyprice/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/kingcountyprice/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/kingcountyprice/x_test.csv")

# drop columns
y_test_id = y_train["ID"]
y_train = y_train.drop(columns = "ID")

drop_list = ["id","ID","sqft_lot"]
for i in drop_list:
    x_train = x_train.drop(columns = i)
    x_test = x_test.drop(columns = i)

# preprocessing 
# 1) time series
x_train["date"] = pd.to_datetime(x_train["date"])
x_train["year"] = x_train["date"].dt.year
x_train["month"] = x_train["date"].dt.month
x_train["day"] = x_train.date.dt.day

# EDA WITH TIME SERIES
#temp = x_train[["year","month","day"]]
#stack = pd.concat([temp,y_train],axis =1)
#use year and month data 
#print(stack.groupby(["year"])["price"].sum())

drop_list = ["date","day"]
for i in drop_list:
    x_train = x_train.drop(columns = i)

x_test["date"] = pd.to_datetime(x_test["date"])
x_test["year"] = x_test["date"].dt.year
x_test["month"] = x_test["date"].dt.month
x_test = x_test.drop(columns = "date")


# preprocessing

# check corr
drop_list1 = ["sqft_living15","sqft_above"] # 다중공산성
#print(x_train[check_list1].corr()) drop : sqft_living15 / sqft_above
for i in drop_list1:
    x_train = x_train.drop(columns = i)
    x_test = x_test.drop(columns = i)

# scalering
from sklearn.preprocessing import MinMaxScaler , LabelEncoder
scaler = MinMaxScaler()
sclaer_list = ["sqft_living","sqft_lot15","sqft_basement"]
temp = x_train[sclaer_list]
temp = pd.DataFrame(scaler.fit_transform(temp))
x_train = pd.concat([x_train,temp], axis=1).rename(columns = {0:"new_live",
                                                              1:"new_lot"})
x_train = x_train.drop(columns = sclaer_list)

# test
temp = x_test[sclaer_list]
temp = pd.DataFrame(scaler.fit_transform(temp))
x_test = pd.concat([x_test,temp], axis=1).rename(columns = {0:"new_live",
                                                              1:"new_lot"})
x_test = x_test.drop(columns = sclaer_list)



# encoding 
encoding_list = ["zipcode","lat","yr_built"]
encoder = LabelEncoder()
for i in encoding_list:
    x_train[i] = pd.DataFrame(encoder.fit_transform(x_train[i]))
    x_test[i] = pd.DataFrame(encoder.fit_transform(x_test[i]))

#stack = pd.concat([x_train[["lat"]],y_train], axis= 1)

# 파생변수 / yr_renovated - 유무
condition = (x_train["yr_renovated"] == 0)
x_train["yr_renovated"].loc[condition] = 0
x_train["yr_renovated"].loc[~condition] = 1

condition = (x_test["yr_renovated"] == 0)
x_test["yr_renovated"].loc[condition] = 0
x_test["yr_renovated"].loc[~condition] = 1

# lets train..
from sklearn.model_selection import train_test_split
X_TRAIN,X_TEST, Y_TRAIN,Y_TEST = train_test_split(x_train,y_train,test_size= 0.3, random_state = 2024)

#
from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_TRAIN,Y_TRAIN)
y_pre = pd.DataFrame(model.predict(x_test)).rename(columns = {0:"price"})
Y_PRE = pd.DataFrame(model.predict(X_TEST))

from sklearn.metrics import r2_score
print("plz work!:", r2_score(Y_TEST,Y_PRE))
print("code is work!")
