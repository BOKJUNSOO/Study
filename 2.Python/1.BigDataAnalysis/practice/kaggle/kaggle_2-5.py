import pandas as pd
train = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\5TRAIN.csv") 
x_test = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\5TEST.csv")

pd.options.display.max_columns = None

# 잘못 입력된 데이터 컬럼 삭제

condition = train["year"] != 2060
train = train.loc[condition]

condition2 = x_test["year"] != 2060
x_test = x_test.loc[condition2]

# 독립변수 종속변수 분리 
x_train = train.drop(columns = ["price"])
y_train = train[["price"]]

# 인코딩
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

x_train["fuelType"] = pd.DataFrame(encoder.fit_transform(x_train["fuelType"]))
x_test["fuelType"] = pd.DataFrame(encoder.fit_transform(x_test["fuelType"]))

x_train["transmission"] = pd.DataFrame(encoder.fit_transform(x_train["transmission"]))
x_test["transmission"] = pd.DataFrame(encoder.fit_transform(x_test["transmission"]))

x_train["model"] = pd.DataFrame(encoder.fit_transform(x_train["model"]))
x_test["model"] = pd.DataFrame(encoder.fit_transform(x_test["model"]))


# 독립변수간 상관관계파악 -- 독립변수간 상관이 작으므로 모든 변수를 포함
# price 와 그룹핑하여 EDA # model // year // transmission // fuelType // tax // engineSize //

#print(train.groupby(["engineSize"])["price"].sum())

# 결측값 처리
x_train["model"].fillna(4, inplace= True)
x_train["transmission"].fillna(1, inplace= True)
x_train["fuelType"].fillna(2, inplace= True)


# 이상치확인 (mpg, mileage)
new_data = x_train[["mpg","mileage"]]
stat_data = new_data.describe().T
# print(stat_data.head())
# find IQR
IQR = stat_data["75%"] - stat_data["25%"]
max_scal = stat_data["75%"] + (IQR * 1.5)
min_scal = stat_data["25%"] - (IQR * 1.5)

# 이상치 확인
# print(stat_data.head())
# print(max_scal.head(), min_scal.head(), "\t")

# 이상치 condtion pointing
# train mpg 이상치 처리
x_train.loc[x_train["mpg"] > 85.8 , "mpg"] = 85.8
x_train.loc[x_train["mpg"] < 32.2, "mpg"] = 32.2

# train mileage 이상치 처리
x_train.loc[x_train["mileage"] > 62504.875, "mileage"] = 62504.875


new_data = x_test[["mpg", "mileage"]]
stat_data = new_data.describe().T

IQR = stat_data["75%"] - stat_data["25%"]
max_scal = stat_data["75%"] + (IQR * 1.5)
min_scal = stat_data["25%"] - (IQR * 1.5)

# 이상치 확인
# print(stat_data.head())
# print(max_scal.head(), min_scal.head(), "\t")

# test mpg 이상치 처리
x_test.loc[x_test["mpg"] > 85.8 , "mpg"] = 85.8
x_test.loc[x_test["mpg"] < 32.2 , "mpg"] = 32.2

# test mileage 이상치 처리 
x_test.loc[x_test["mileage"] > 62112.0, "mileage"] = 62112.0

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = pd.DataFrame(scaler.fit_transform(x_train), columns = x_train.columns)
x_test = pd.DataFrame(scaler.fit_transform(x_test) , columns = x_train.columns)

from sklearn.model_selection import train_test_split


X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train, y_train, test_size= 0.2 , random_state= 10)

x_train.info()
y_train.info()

from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_TRAIN,Y_TRAIN)
data = pd.DataFrame(model.predict(x_test)).rename(columns = {0:"price"}) # 제출용 데이터

from sklearn.metrics import r2_score
Y_TEST_PREDICT = pd.DataFrame(model.predict(X_TEST)).rename(columns = {0:"price"})
print(r2_score(Y_TEST, Y_TEST_PREDICT))
print("code is work")
