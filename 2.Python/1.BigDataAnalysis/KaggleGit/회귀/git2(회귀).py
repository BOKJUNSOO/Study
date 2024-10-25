import pandas as pd
pd.options.display.max_columns = None

x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/carsprice/X_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/carsprice/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/carsprice/X_test.csv")

# drop id
y_test_id = y_train["carID"]
y_train.drop(columns = 'carID', inplace = True)
x_train.drop(columns = 'carID', inplace = True)
x_test.drop(columns= "carID", inplace = True)

# encoding
list = ["brand", "model","year","transmission","fuelType"]

# data
temp = x_train[list] # new data frame
data = pd.concat([temp,y_train], axis = 1)
for i in list:
    #print(data.groupby([i])["price"].sum()) # 모든 독립변수 포함
    pass

# print(x_train.corr()) # 다중공산성 해결
 
# LabelEncoding
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for i in list:
    x_train[i] = pd.Series(encoder.fit_transform(x_train[i]))
    x_test[i] = pd.Series(encoder.fit_transform(x_test[i]))

# StandardScaler
ss_list = ["mileage","tax","mpg"]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
temp = x_train[ss_list]
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_mileage",
                                                                  1:"new_tax",
                                                                  2:"new_mpg"})
x_train = pd.concat([x_train,temp], axis = 1)
x_train.drop(columns = ss_list , inplace = True)

temp = x_test[ss_list]
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_mileage",
                                                                  1:"new_tax",
                                                                  2:"new_mpg"})
x_test = pd.concat([x_test,temp], axis = 1)
x_test.drop(columns = ss_list , inplace = True)

# split
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train, y_train, test_size = 0.3, random_state = 2024)

# train
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_TRAIN, Y_TRAIN)
y_predict = pd.DataFrame(model.predict(x_test)).rename(columns = {0:"G3"})
result = pd.concat([y_test_id,y_predict], axis = 1)

# 평가
from sklearn.metrics import r2_score
Y_PREDICT = model.predict(X_TEST)
print("random_forest_r2_score : ",r2_score(Y_TEST, Y_PREDICT))

# another model
from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_TRAIN,Y_TRAIN)
Y_PREDICT = model.predict(X_TEST)
print("XGBR_r2_score",r2_score(Y_TEST,Y_PREDICT))

# 예측 결과 저장
#result.to_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\회귀\result.csv")



"""
# 이상치 확인
def outlier(df,column):
        mean = df[column].mean()
        std = df[column].std()
        lowest = mean - (std * 1.5)
        highest = mean + (std * 1.5)
        print("max_scal : ", highest,
              "min_scal : ", lowest)
        high_outlier = df.loc[df[column] >= highest].iloc[:,0]
        low_outlier = df.loc[df[column] <= lowest].iloc[:,0]
        return high_outlier, low_outlier
check_list = ["mileage","tax","mpg","engineSize"]
for i in check_list:
    outlier(x_train, i)
print(type(x_train.loc[x_train["mileage"] >= 30].iloc[:,0]))
print(pd.Series(outlier(x_train,"mileage")).head())

temp = x_train[check_list]

status = temp.describe().T
IQR = status["75%"] - status["25%"]
max_scaler = status["75%"] + 1.5*IQR
min_scaler = status["25%"] - 1.5*IQR
"""
# max_scaler 보다 큰 값 대체 --> mileage : 83293.125 / tax : 157.7 / mpg :77.7 / engineSize : 4.6 
# min_scaler 보다 작은 값 대체 --> tax : 137.5 / mpg : 15.3 /
