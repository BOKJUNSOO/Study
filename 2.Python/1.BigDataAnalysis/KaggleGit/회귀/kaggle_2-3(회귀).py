# data/pretest/3TEST AND 3TRAIN.csv

"""[분류] 여행 보험 패키지 상품을 구매할 확률 값을 구하시오 / 리더보드 제출용"""

import pandas as pd

pd.options.display.max_columns = None

train = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\3TRAIN.csv")
test_x = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\3TEST.csv")

# 독립변수 종속변수 분리
train_x = train.drop(columns = "TravelInsurance")
train_y = pd.DataFrame(train["TravelInsurance"])

# 필요없는 칼럼 제거 (id)
test_x_id = test_x["id"]
test_x.drop(columns = "id", inplace=  True)
train_x.drop(columns = "id", inplace = True)

# 이상치 확인 (AnnualIncome)
data = pd.DataFrame(train_x["AnnualIncome"].describe())
data = data.T

IQR = data["75%"] - data["25%"]
max_scal = data["75%"] + IQR * 1.5
min_scal = data["25%"] - IQR * 1.5

# max_scal 보다 큰 값 대치 = None



# 결측치 처리 이상치 처리 이후
train_mean = train_x["AnnualIncome"].mean()
test_mean = test_x["AnnualIncome"].mean()

train_x["AnnualIncome"].fillna(train_mean , inplace= True)
test_x["AnnualIncome"].fillna(test_mean, inplace=True)


# Label encoding // minmaX sCALER
from sklearn.preprocessing import MinMaxScaler
mm_scaler = MinMaxScaler()

# minmaxscaler
temp = train_x[["AnnualIncome"]]
annual_scal = pd.DataFrame(mm_scaler.fit_transform(temp)).rename(columns = {0: "new_AnnualIncome"})

train_x = pd.concat([train_x, annual_scal], axis = 1)
train_x.drop(columns = "AnnualIncome", inplace = True)

temp = test_x[["AnnualIncome"]]
annual_scal = pd.DataFrame(mm_scaler.fit_transform(temp)).rename(columns = {0 : "new_AnnualIncome"})

test_x = pd.concat([test_x, annual_scal], axis = 1)
test_x.drop(columns = "AnnualIncome", inplace = True)


# Label Encoder
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
list = ["Employment Type","GraduateOrNot","FrequentFlyer", "EverTravelledAbroad"]
for i in list:
    train_x[i] = encoder.fit_transform(train_x[i])
for i in list:
    test_x[i] = encoder.fit_transform(test_x[i])

# split data set
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(train_x, train_y, test_size = 0.2, random_state = 2024)

# model selection
from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_TRAIN, Y_TRAIN)
y_test_predict = pd.DataFrame(model.predict(test_x)).rename(columns = {0:"TravelInsurance"})

# 결과 제출
result = pd.concat([test_x_id, y_test_predict], axis = 1)
result["TravelInsurance"] = abs(result["TravelInsurance"])
print(result.head())
# result.to_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\pretest\2-3result.csv", index= False)

# model auc
from sklearn.metrics import roc_auc_score
Y_PREDICT = pd.DataFrame(model.predict(X_TEST))
result = (roc_auc_score(Y_TEST,Y_PREDICT))
print(result)
print(train_x.head(), "code is work" , "\t")

