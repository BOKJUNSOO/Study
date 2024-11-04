# 레드 와인 퀄리티 예측 데이터
import pandas as pd
pd.options.display.max_columns = None

x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/redwine/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/redwine/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/redwine/x_test.csv")

# set id
y_id = y_train["ID"]
drop_col = ["ID"]

x_train = x_train.drop(columns = drop_col)
y_train = y_train.drop(columns = drop_col)
x_test = x_test.drop(columns = drop_col)


# print(x_train.loc[x_train["total sulfur dioxide"] == 0]) # empty
x_train["sul_percentage"] = (x_train["free sulfur dioxide"] / x_train["total sulfur dioxide"]) * 100
x_test["sul_percentage"] = (x_test["free sulfur dioxide"] / x_test["total sulfur dioxide"]) * 100

# scaler
scal_col = ["fixed acidity","residual sugar"]
temp = x_train[scal_col]
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
temp = pd.DataFrame(scaler.fit_transform(temp))
x_train = pd.concat([x_train,temp], axis = 1).rename(columns = {0:"new_acid",
                                                                1:"new_res_sug"
                                                                })
x_train = x_train.drop(columns = scal_col)

#
temp = x_test[scal_col]
temp = pd.DataFrame(scaler.fit_transform(temp))
x_test = pd.concat([x_test,temp], axis = 1).rename(columns = {0:"new_acid",
                                                                1:"new_res_sug"
                                                                })
x_test = x_test.drop(columns = scal_col)

# y_train catagory
y_train.loc[y_train["quality"] <= 5] = 0
y_train.loc[y_train["quality"] >= 6] = 1
print(y_train.head())

# split
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train,y_train, test_size = 0.3 , random_state = 2024)

# random forest
from sklearn.ensemble import RandomForestClassifier
model1 = RandomForestClassifier()
model1.fit(X_TRAIN,Y_TRAIN)
y_test_predict1 = pd.DataFrame(model1.predict(x_test))
Y_TEST_PREDICT1 = pd.DataFrame(model1.predict(X_TEST))
label1 = pd.DataFrame(model1.predict(X_TRAIN))

from xgboost import XGBClassifier
model2 = XGBClassifier()
model2.fit(X_TRAIN,Y_TRAIN)
y_test_predict2 = pd.DataFrame(model2.predict(x_test))
Y_TEST_PREDICT2 = pd.DataFrame(model2.predict(X_TEST))
label2 = pd.DataFrame(model2.predict(X_TRAIN))

# model score
from sklearn.metrics import r2_score, accuracy_score, roc_auc_score
print("ensenble_model_score_ roc_auc:",roc_auc_score(Y_TEST,Y_TEST_PREDICT1))
print("ensenble_label_score :",r2_score(label1,Y_TRAIN))
print()
print("Xgboost_model_score_ roc_auc:",roc_auc_score(Y_TEST,Y_TEST_PREDICT2))
print("xgboost_label_score :",r2_score(label2,Y_TRAIN))



