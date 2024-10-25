# 학생성적 예측 데이터
import pandas as pd
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/studentscore/X_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/studentscore/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/studentscore/X_test.csv")

pd.options.display.max_columns = None

y_test_id = y_train["StudentID"]
y_train.drop(columns = "StudentID", inplace = True)
x_train.drop(columns = "StudentID", inplace = True)
x_test.drop(columns = "StudentID", inplace = True)

# encoding
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

list = ["school","address","sex","famsize","Pstatus","Mjob","Fjob","reason","guardian","schoolsup","famsup","paid",
        "activities","nursery","higher","internet","romantic"]
for i in list:
#    print(x_train[i].unique())
    x_train[i] = pd.Series(encoder.fit_transform(x_train[i]))
for i in list:
    x_test[i] = pd.Series(encoder.fit_transform(x_test[i]))

# data split
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train,y_train, test_size = 0.3, random_state=2024)

from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
model = XGBRegressor()
model2 = RandomForestRegressor(random_state= 2024)
model.fit(X_TRAIN,Y_TRAIN)
model2.fit(X_TRAIN,Y_TRAIN)
# RESULT
y_test_predict = pd.DataFrame(model.predict(x_test)).rename(columns = {0:"G3"})

from sklearn.metrics import r2_score
Y_PREDICT = pd.DataFrame(model.predict(X_TEST))
Y_PREDICT2 = pd.DataFrame(model2.predict(X_TEST))
print(r2_score(Y_PREDICT, Y_TEST))
print(r2_score(Y_PREDICT2, Y_TEST))

