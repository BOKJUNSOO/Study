# 이직여부 판단 데이터

import pandas as pd
pd.options.display.max_columns = None
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_test.csv")


# unique한 값이 너무 많으면 drop 하자 **
drop_col = ['city','company_type','experience']
print("drop_dataframe :",x_train[drop_col].nunique())
x_train.drop(columns = drop_col,inplace=True)
x_test.drop(columns = drop_col,inplace=True)

#
y_id = y_train["enrollee_id"]
y_train.drop(columns = "enrollee_id",inplace = True)
x_train.drop(columns = "enrollee_id",inplace = True)
x_test.drop(columns = "enrollee_id",inplace = True)

# 인코딩으로 결측치 처리됨.. 타겟변수와 로우 겟수 맞춰짐 ** row 지우면 성능 매우저하
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
x_train.info()
list = ["gender","relevent_experience","enrolled_university","education_level","major_discipline","company_size","last_new_job"]
for i in list:
    x_train[i] = pd.Series(encoder.fit_transform(x_train[i]))
    x_test[i] = pd.Series(encoder.fit_transform(x_test[i]))

from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train, y_train, test_size= 0.3, random_state = 2024)

# model1
from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(X_TRAIN, Y_TRAIN)
label = pd.DataFrame(model.predict(X_TRAIN))
y_test_pre = pd.DataFrame(model.predict(x_test))

from sklearn.metrics import roc_auc_score
Y_PRE = model.predict(X_TEST)
print("label_val :", roc_auc_score(Y_TRAIN, label))
print("real_score :",roc_auc_score(Y_TEST, Y_PRE))

# model2
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_TRAIN,Y_TRAIN)
y_test_pre = model.predict(x_test) # result

Y_TEST_PRE = model.predict(X_TEST)
label = model.predict(X_TRAIN)

# 문제에서 묻는 것에 따라 모델 성능 확인하기
# 정확도 (accuracy) , f1_score , recall , precision -> model.predict로 결과뽑기
# auc , 확률이라는 표현있으면 model.predict_proba로 결과뽑고 첫번째 행의 값을 가져오기 model.predict_proba()[:,1]
print("label_val_RF : ", roc_auc_score(Y_TRAIN,label))
print("real_score_RF : ", roc_auc_score(Y_TEST,Y_TEST_PRE))


