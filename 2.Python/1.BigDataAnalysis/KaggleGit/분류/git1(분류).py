# 분류 서비스이탈예측 데이터
# dataset : Churn_Modelling.csv
import pandas as pd
pd.options.display.max_columns = None

# 데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/X_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/X_test.csv")

# 제출용 id 분리
y_test_id = x_test[["CustomerId"]]
y_train.drop(columns = "CustomerId", inplace= True)
x_train.drop(columns = "CustomerId", inplace = True)
x_test.drop(columns = "CustomerId", inplace = True)


# LabelEncoder
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

# encoding list
list = ["Surname","Geography","Gender"]
for i in list:
    x_train[i] = pd.Series(encoder.fit_transform(x_train[i]))
for i in list:
    x_test[i] = pd.Series(encoder.fit_transform(x_test[i]))

# Standard prprocessing
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# preprocessing
list = ["Balance","EstimatedSalary"]

temp = x_train[list]
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_balance",1:"new_est"})
x_train = pd.concat([x_train,temp], axis = 1)
x_train.drop(columns = list, inplace = True)

temp = x_test[list]
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_balance",1:"new_est"})
x_test = pd.concat([x_test,temp], axis = 1)
x_test.drop(columns = list, inplace = True)

# value selection # train 시켜보고 정하기 groupby
# dummy_data = pd.concat([x_train,y_train], axis = 1)

# data split
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train, y_train, test_size = 0.3, random_state = 2024)

from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(X_TRAIN,Y_TRAIN)
y_test_predict = pd.DataFrame(model.predict(x_test))
result = pd.concat([y_test_id, y_test_predict],axis = 1)

# 모델평가
from sklearn.metrics import roc_auc_score , accuracy_score
Y_TEST_PREDICT = pd.DataFrame(model.predict(X_TEST))
print("this is accuracy:" ,accuracy_score(Y_TEST, Y_TEST_PREDICT))
print("this is score:",roc_auc_score(Y_TEST, Y_TEST_PREDICT))




# check unique value
"""list = ["HasCrCard","IsActiveMember"]
for i in list:
    print("check unique",x_train[i].unique())"""

"""for i in list1:
    print("This is encoding list:", x_train[i].unique() ,"\t")
list2 = ["Age","Tenure"]
for i in list2:
    print("This is second list:", x_train[i].unique(), "\t")"""




print("This Code is Working")