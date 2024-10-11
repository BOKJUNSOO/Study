import pandas as pd
x_train = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\bike_x_train.csv", encoding = "cp949")
y_train = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\bike_y_train.csv", encoding = "utf-8")
x_test = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\bike_x_test.csv", encoding = "cp949")

"""고객 10,866건에 대한 학습용 데이터를 이용하여 자전거 대여량 예측 모형을 만든다.
생성한예측 모형으로 평가용 데이터에 해당하는 6,493건의 자전거 대여량 예측값을 다음과 같은 csv 파일로 생성하시오"""
pd.options.display.max_columns = None
# 데이터 전처리

# 결측치확인
# print(x_train.isnull().sum()) zero

# 독립변수 종속변수 확인 season, holiday, weather, workday 모두 포함시키는 것이 필요
dum = pd.concat([x_train, y_train], axis = 1)
# print(dum.groupby(["season"])["count"].sum())
# print(dum.groupby(["holiday"])["count"].sum())
# print(dum.groupby(["weather"])["count"].sum())

# 상관관계 확인
# print(dum[["season","holiday","workday","weather"]].corr()) 모두 낮은 상관이므로 모두 포함

# datetime 컬럼을 분해하여 년도, 월 , 일 , 시간별 컬럼으로 추출!
x_train["datetime"] = pd.to_datetime(x_train["datetime"]) # datetime 컬럼을 object에서 datetime 타입으로 바꾸기
x_train["year"] = x_train["datetime"].dt.year
#x_train["month"] = x_train["datetime"].dt.month
#x_train["day"] = x_train["datetime"].dt.day
x_train["hour"] = x_train["datetime"].dt.hour
#x_train["dayofweek"] = x_train["datetime"].dt.dayofweek # 요일데이터

x_test["datetime"] = pd.to_datetime(x_test["datetime"])
x_test["year"] = x_test["datetime"].dt.year
x_test["hour"] = x_test["datetime"].dt.hour
# dum = pd.concat([x_train, y_train] , axis = 1)
# datetime 변수로 부터 얻은 칼럼중 유용한 변수찾기 # year, hour
# print(dum.groupby(["dayofweek"])["count"].sum())

# 불필요한 컬럼 제거
x_test_datetime = x_test["datetime"]
x_test.drop(columns = "datetime", inplace = True)
x_train.drop(columns = "datetime", inplace = True)
y_train.drop(columns = "datetime", inplace = True)




# 데이터 분리하기
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train, y_train, test_size= 0.2 , random_state = 10)

# 모델링 
from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_TRAIN, Y_TRAIN)
y_test_predict = pd.DataFrame(model.predict(x_test)).rename(columns = {0:"count"})

# count 값이 음수로 나온경우 0으로 바꾸기
y_test_predict.loc[y_test_predict["count"] < 0 ] = 0
data = pd.concat([x_test_datetime,y_test_predict], axis =1) # 최종 제출용데이터
data.to_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\go2.csv", index= False)

# 모델 평가하기(파라피터 성능 확인을 위해)
from sklearn.metrics import r2_score
Y_TEST_PREDICT = pd.DataFrame(model.predict(X_TEST)).rename(columns = {0:"count"})
print(Y_TEST_PREDICT.head())
Y_TEST_PREDICT.loc[Y_TEST_PREDICT["count"]<0] = 0
print(r2_score(Y_TEST, Y_TEST_PREDICT))