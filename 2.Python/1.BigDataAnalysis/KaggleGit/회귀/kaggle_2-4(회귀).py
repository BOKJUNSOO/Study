import pandas as pd
train = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\4TRAIN.csv")
test_x = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\4TEST.csv")

"""model classfication"""
pd.options.display.max_columns = None

train_x = train.drop(columns = "Segmentation")
train_y = train[["Segmentation"]]

# drop ID
train_x.drop(columns = "ID" , inplace= True)
test_x_ID = test_x["ID"]
test_x.drop(columns = "ID", inplace = True)

print(train_x.head())

# encoding
col = ["Gender","Ever_Married","Graduated","Profession","Spending_Score","Var_1"]

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for i in col:
    train_x[i] = pd.DataFrame(encoder.fit_transform(train_x[i]))

for i in col:
    test_x[i] = pd.DataFrame(encoder.fit_transform(test_x[i]))
# select every var
# print(train_x.corr())

# groupby
data = pd.concat([train_x, train_y] , axis = 1)
col = ["Gender","Ever_Married","Graduated","Profession","Spending_Score","Var_1","Work_Experience"]

#for i in col:
#    print(data.groupby(i)["Segmentation"].count()) 

# train_x.drop(columns = "Gender", inplace = True)
# test_x.drop(columns = "Gender", inplace= True)

train_x.drop(columns = "Ever_Married", inplace = True)
test_x.drop(columns = "Ever_Married", inplace= True)

# train_x.drop(columns = "Profession", inplace = True)
# test_x.drop(columns = "Profession", inplace= True)

# split data set
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST , Y_TRAIN, Y_TEST = train_test_split(train_x, train_y, test_size = 0.2, random_state = 10)

# modeling
from xgboost import XGBClassifier
model = XGBClassifier()

# checkcol = ["Ever_Married","Age","Graduated","Profession","Spending_Score","Var_1","Work_Experience","Family_Size"]
# for i in checkcol:
#    print(X_TRAIN[i].unique())

Y_TRAIN = Y_TRAIN.replace(1,0).replace(2,1).replace(3,2).replace(4,3) # if not it got error
model.fit(X_TRAIN, Y_TRAIN) 
y_test_predict = pd.DataFrame(model.predict(test_x)).rename(columns = {0:"Segmentation"}) # 제출용
# print(y_test_predict.head())

# 
from sklearn.metrics import accuracy_score
Y_TEST_PREDICT = pd.DataFrame(model.predict(X_TEST)).rename(columns= {0:"Segmentation"})
Y_TEST = Y_TEST.replace(1,0).replace(2,1).replace(3,2).replace(4,3)
# print(Y_TEST_PREDICT.head())
print(accuracy_score(Y_TEST, Y_TEST_PREDICT))

print("Code is work")
