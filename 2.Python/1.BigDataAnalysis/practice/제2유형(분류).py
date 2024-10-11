import pandas as pd
x_train = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\titanic_x_train.csv",encoding="utf-8")
y_train = pd.read_csv('C:\\Users\\brian\\Desktop\\JUNSOO\\study\\2.Python\\1.BigDataAnalysis\\data\\titanic_y_train.csv')
x_test = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\titanic_x_test.csv",encoding="utf-8")

"""고객 891명에 대한 학습용 데이터를 이용하여 생존 여부를 예측하는 모형을 만듭니다.
    이후 예측 모형을 평가용 데이터에 적용하여 
    418명 승객의 생존 여부 예측값을 다음과 같은 형식의 CSV 파일로 생성하시오"""
# 말줄임표 없애기
pd.options.display.max_columns = None



# 필요한 (독립변수가 되는) 컬럼 찾기
dum = pd.concat([x_train, y_train] , axis = 1)
# dum.info()
# note) groupby 는 다른 groupbyobject 로 설정됨 (메서드를 붙히기전에 출력할 수 있는게 없다!)
# print(type(dum.groupby(["sex"])["Survived"].mean()))   # 성별로 그룹핑한 다음에 생존확률의 평균
# print(dum.groupby(["level"])["Survived"].mean())   # 티켓등급으로 그룹핑한 다음에 생존확률의 평균
# print(dum.groupby(["entry"])["Survived"].mean())

# 전처리하기
x_test_id = x_test["PassengerId"]
x_train.drop(columns = "PassengerId" , inplace= True)
y_train.drop(columns= "PassengerId", inplace = True)
x_test.drop(columns = "PassengerId", inplace=True)

x_train.drop(columns = ["no", "ticketno", "name","fee"], inplace= True)
x_test.drop(columns = ["no", "ticketno", "name","fee"], inplace= True)

# 결측치 처리 (age, entry)
# print(dum[["age","Survived"]].corr())
x_train.drop(columns = "age", inplace = True)
x_test.drop(columns = "age", inplace= True)

x_train["entry"].fillna("S",inplace=True)
x_test["entry"].fillna("S", inplace=True)

# 인코딩
x_train["sex"] = x_train["sex"].replace("male",1).replace("female",0)
x_test["sex"] = x_test["sex"].replace("male",1).replace("female",0)

# 라벨 인코딩 (정규화는 temp 와 데이터 프레임을 입력해야하지만 라벨인코딩은 시리즈변수 입력, 바로 지정가능!)
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
x_train["entry"] = encoder.fit_transform(x_train["entry"])  # fit_transform 은 array 를 리턴하지만 
                                                            # dataframe 에 바로 대입연산 가능***
x_test["entry"] = encoder.fit_transform(x_test["entry"])

# 파생변수만들기
x_train["Family"] = x_train["partner"] + x_train["parent"]
x_test["Family"] = x_test["partner"] + x_test["parent"]

x_train.drop(columns = ["partner","parent"] , inplace=True)
x_test.drop(columns = ["partner","parent"] , inplace=True)

# x_train, 과 y_train 으로 모델학습시키기
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(x_train, y_train, test_size=0.3 , random_state = 10)

# 일반적으로 성능이 잘 나오는 분류모델 XGBClassifier
from xgboost import XGBClassifier
model = XGBClassifier()

# 모델 학습시키기
model.fit(X_TRAIN, Y_TRAIN)

# 학습한 모델로 예측하기
x_test_predict = pd.DataFrame(model.predict(x_test)).rename(columns = {0:"Survived"})

# 제출용 파일작성
x_test_id = pd.DataFrame(x_test_id)
data = pd.concat([x_test_id, x_test_predict], axis = 1)

# 제출 형식에 맞게 index = False
data.to_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\go.csv", index = False)

# 모델 평가하기 - 평가지표 계산용 (제출코드는 아님 , X_TEST, Y_TEST 사용)
from sklearn.metrics import roc_auc_score
Y_TEST_PREDICT = pd.DataFrame(model.predict(X_TEST))
print(roc_auc_score(Y_TEST, Y_TEST_PREDICT))


print("code is work")






