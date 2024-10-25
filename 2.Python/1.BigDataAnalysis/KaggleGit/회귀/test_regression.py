import pandas as pd
x_train = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\bike_x_train.csv", encoding = "cp949")
y_train = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\bike_y_train.csv", encoding = "utf-8")
x_test = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\bike_x_test.csv", encoding = "cp949")

"""고객 10,866건에 대한 학습용 데이터를 이용하여 자전거 대여량 예측 모형을 만든다.
생성한예측 모형으로 평가용 데이터에 해당하는 6,493건의 자전거 대여량 예측값을 다음과 같은 csv 파일로 생성하시오"""
pd.options.display.max_columns = None

# 결측치 확인 - okay

# datetime 분리
x_train["datetime"] = pd.to_datetime(x_train["datetime"])
x_train["year"] = x_train["datetime"].dt.year
x_train["month"] = x_train["datetime"].dt.month
x_train["hour"] = x_train["datetime"].dt.hour
x_train["day"] = x_train["datetime"].dt.day_of_week
x_train.drop(columns = "datetime", inplace = True)

x_test["datetime"] = pd.to_datetime(x_test["datetime"])
x_test["year"] = x_test["datetime"].dt.year
x_test["month"] = x_test["datetime"].dt.month
x_test["hour"] = x_test["datetime"].dt.hour
x_test["day"] = x_test["datetime"].dt.day_of_week
x_test_index = x_test["datetime"]
x_test.drop(columns = "datetime", inplace = True)


# 독립변수 확인 
# 다중공산성 해결
# 유의미한 변수 groupby
data = pd.concat([x_train,y_train], axis = 1)

# col = ["year","hour","windspeed","mois","bodytemp","temp","weather","workday","holiday"]
#for i in col:
#    print(data.groupby([i])["count"].sum())

x_train.drop(columns = ["season","month","day"] , inplace = True)
x_test.drop(columns = ["season","month","day"], inplace= True)


# 제출용 인덱스저장
y_train.drop(columns = "datetime",inplace = True)
# x_test_index

# 인코딩
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
encoder = LabelEncoder()
x_train["year"] = pd.Series(encoder.fit_transform(x_train["year"]))
x_test["year"] = pd.Series(encoder.fit_transform(x_test["year"]))

scaler = MinMaxScaler()
temp = x_train[["temp","bodytemp","mois"]]
temp1 = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_temp", 1:"new_body_temp",2:"new_mois"})
x_train = pd.concat([x_train, temp1], axis = 1)
x_train.drop(columns = ["temp","bodytemp","mois"], inplace = True)

temp = x_test[["temp","bodytemp","mois"]]
temp1 = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_temp", 1:"new_body_temp",2:"new_mois"})
x_test = pd.concat([x_test, temp1], axis = 1)
x_test.drop(columns = ["temp","bodytemp","mois"], inplace = True)

# train
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train, y_train, test_size = 0.2, random_state = 2024)

from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_TRAIN,Y_TRAIN)
y_test_predict = pd.DataFrame(model.predict(x_test)).rename(columns = {0:"count"})
result = pd.concat([x_test_index,y_test_predict], axis = 1)

# predict test
from sklearn.metrics import r2_score
Y_TEST_PREDICT = pd.DataFrame(model.predict(X_TEST)).rename(columns = {0:"count"})
result = r2_score(Y_TEST,Y_TEST_PREDICT)
print("predict_Score : ", result)
print(x_train.head())