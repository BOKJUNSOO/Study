# 의료비용 예측
import pandas as pd
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/MedicalCost/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/MedicalCost/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/MedicalCost/x_test.csv")

# drop col
y_test_id = y_train["ID"]
x_train.drop(columns = "ID",inplace=True)
x_test.drop(columns = "ID",inplace=True)
y_train.drop(columns = "ID",inplace=True)

# encoder
list = ["sex","smoker","region"]
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for i in list:
    x_train[i] = pd.Series(encoder.fit_transform(x_train[i]))
    x_test[i] = pd.Series(encoder.fit_transform(x_test[i]))

# training
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train, y_train, test_size = 0.3 , random_state = 2024)

from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
model1 = XGBRegressor()
model2 = RandomForestRegressor()

# xgboost
model1.fit(X_TRAIN,Y_TRAIN)
y_test_result1 = pd.DataFrame(model1.predict(x_test)).rename(columns = {0:"charges"})
Y_PRED1 = pd.DataFrame(model1.predict(X_TEST))
label1 = model1.predict(X_TRAIN)
# randomForest
model2.fit(X_TRAIN,Y_TRAIN)
y_test_result2 = pd.DataFrame(model2.predict(x_test)).rename(columns = {0:"charges"})
Y_PRED2 = pd.DataFrame(model2.predict(X_TEST))
label2 = model2.predict(X_TRAIN)
# score
from sklearn.metrics import r2_score
"""print("xgb_r2_score:",r2_score(Y_TEST,Y_PRED1))
print("xgb_label_score:",r2_score(Y_TRAIN,label1))
print("\n")
print("rdf_r2_score:",r2_score(Y_TEST,Y_PRED2))
print("rdf_label_score:",r2_score(Y_TRAIN,label2))""" 

result = pd.concat([y_test_id,y_test_result1],axis=1)
#print(result.head())

