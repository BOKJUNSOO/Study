# 수질 음용성 여부 데이터
import pandas as pd
pd.options.display.max_columns = None
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/waters/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/waters/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/waters/x_test.csv")

# id
y_id = y_train["ID"]
x_train = x_train.drop(columns = "ID")
y_train = y_train.drop(columns = "ID")
x_test = x_test.drop(columns = "ID")

# ph, sulfate, trihalomethanes
ph_mean = x_train["ph"].mean()
sulfate_mean = x_train["Sulfate"].mean()
trihal_mean = x_train["Trihalomethanes"].mean()

x_train["ph"] = x_train["ph"].fillna(ph_mean)
x_train["Sulfate"] = x_train["Sulfate"].fillna(sulfate_mean)
x_train["Trihalomethanes"] = x_train["Trihalomethanes"].fillna(trihal_mean)
#
#ph_mean = x_test["ph"].mean()
#sulfate_mean = x_test["Sulfate"].mean()
#trihal_mean = x_test["Trihalomethanes"].mean()

x_test["ph"] = x_test["ph"].fillna(ph_mean)
x_test["Sulfate"] = x_test["Sulfate"].fillna(sulfate_mean)
x_test["Trihalomethanes"] = x_test["Trihalomethanes"].fillna(trihal_mean)

# prerpocessing
from sklearn.preprocessing import StandardScaler
stand_col = ["Hardness","Solids","Sulfate","Conductivity","Trihalomethanes"]

temp = x_train[stand_col]
scaler = StandardScaler()
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_hard",
                                                                  1:"new_sol",
                                                                  2:"new_sul",
                                                                  3:"new_cond",
                                                                  4:"new_trihal"})
x_train = pd.concat([x_train,temp], axis = 1)
x_train = x_train.drop(columns = stand_col)

# test
temp = x_test[stand_col]
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_hard",
                                                                  1:"new_sol",
                                                                  2:"new_sul",
                                                                  3:"new_cond",
                                                                  4:"new_trihal"})
x_test = pd.concat([x_test,temp], axis = 1)
x_test = x_test.drop(columns = stand_col)
x_train.info()
x_test.info()
# split
from sklearn.model_selection import train_test_split
X_TRAIN,X_TEST, Y_TRAIN,Y_TEST = train_test_split(x_train,y_train, test_size = 0.3, random_state = 2024)

# model and score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
model1 = RandomForestClassifier()
model1.fit(X_TRAIN,Y_TRAIN)
y_test_pre = pd.DataFrame(model1.predict(x_test)) # result
Y_TEST_PRE = pd.DataFrame(model1.predict(X_TEST))
label = pd.DataFrame(model1.predict(X_TRAIN))
model = "RandomForest"
print(f"{model} label score:",roc_auc_score(label,Y_TRAIN))
print(f"{model} model score:", roc_auc_score(Y_TEST,Y_TEST_PRE))

from xgboost import XGBClassifier
model2 = XGBClassifier()
model2.fit(X_TRAIN,Y_TRAIN)
y_test_pre = pd.DataFrame(model2.predict(x_test))
Y_TEST_PRE = pd.DataFrame(model2.predict(X_TEST))
model = "xgboost"
print(f"{model} model score:", roc_auc_score(Y_TEST,Y_TEST_PRE))

