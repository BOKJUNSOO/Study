# 정시 배송여부 판단 (2회기출)
import pandas as pd

pd.options.display.max_columns = None
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/shipping/X_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/shipping/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/shipping/X_test.csv")

y_test_id = y_train["ID"]
x_train.drop(columns = "ID", inplace = True)
x_test.drop(columns = "ID", inplace = True)
y_train.drop(columns = "ID", inplace = True)

# 전처리
x_train["Customer_care_calls"] = x_train["Customer_care_calls"].replace("$7",7)
x_test["Customer_care_calls"] = x_test["Customer_care_calls"].replace("$7",7)

x_train["Customer_care_calls"] = x_train["Customer_care_calls"].astype(int)
x_test["Customer_care_calls"] = x_test["Customer_care_calls"].astype(int)

# 인코딩
list = ["Warehouse_block","Mode_of_Shipment","Product_importance","Gender"]
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
encoder = LabelEncoder()
for i in list:
    x_train[i] = pd.Series(encoder.fit_transform(x_train[i]))
    x_test[i] = pd.Series(encoder.fit_transform(x_test[i]))

scaler = MinMaxScaler()
list = ["Weight_in_gms"]#,"Cost_of_the_Product"]#,"Discount_offered"]
# train ss
temp = x_train[list]
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_gms",
                                                           1:"new_cost_product",
                                                           2:"new_Discount_off"})
x_train = pd.concat([x_train,temp], axis = 1)
x_train.drop(columns = list, inplace = True)
# test ss
temp = x_test[list]
temp = pd.DataFrame(scaler.fit_transform(temp)).rename(columns = {0:"new_gms",
                                                           1:"new_cost_product",
                                                           2:"new_Discount_off"})
x_test = pd.concat([x_test,temp], axis = 1)
x_test.drop(columns = list, inplace = True)

# training split
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train, y_train, test_size = 0.3, random_state = 2024)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_TRAIN,Y_TRAIN)
y_predict_test = pd.DataFrame(model.predict(x_test))
result = pd.concat([y_test_id,y_predict_test], axis = 1)
# result.to_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\KaggleGit\분류\gogo.csv",index = False)
# test model
from sklearn.metrics import roc_auc_score , accuracy_score
Y_PRET = pd.DataFrame(model.predict(X_TEST))
print("this is model score :", roc_auc_score(Y_TEST,Y_PRET))
print("this is acc score :", accuracy_score(Y_TEST,Y_PRET))

label = model.predict(X_TRAIN)
#print("this is label score :", accuracy_score(Y_TRAIN,label)) 분류는 라벨링 무조건 만점..








