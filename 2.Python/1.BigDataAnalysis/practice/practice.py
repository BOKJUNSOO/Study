import pandas as pd
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\mtcars.csv")

# 결측치 처리
# print(df["cyl"].mean(), df["qsec"].median(), "\t") 
# 7.6 and 17.6
df["cyl"].fillna(7.6, inplace = True)
df["qsec"].fillna(17.6, inplace= True)

# 독립/ 종속변수 분리
X = df.drop(columns = "mpg")
Y = df["mpg"]
X = X.iloc[:,1:]

# 인코딩
X["am"] = X["am"].replace("manual", 1).replace("auto",0)
X["gear"] = X["gear"].replace("*3",3).replace("*5",5)
X["gear"] = X["gear"].astype(int)

# 이상치처리
기본통계량 = X.describe().T
IQR = 기본통계량["75%"] - 기본통계량["25%"]
최대경계값 = 기본통계량["75%"] + IQR*1.5 
최소경계값 = 기본통계량["25%"] - IQR*1.5

#print(최대경계값
#      ,기본통계량["max"])   # cyl // 14, hp // 305.25, qsec // 21.465, carb // 7 << 이상치 존재

# 포인터로 인덱스확인 
#print("this is index:",X.loc[X["qsec"] > 21.465],"\t")

# 값 대체 // 4분위수 활용
X.loc[14, "cyl"] = 14
X.loc[8, "qsec"] = 21.465
X.loc[24, "qsec"] = 21.465
print(X.head(25))


# carb, hp // 평균과 표준편차 사용 30번 인덱스에서 두 수치에 이상발견

carb_mean = X["carb"].mean()
carb_std =X["carb"].std()
대체값 = carb_mean + 1.5*carb_std
X.loc[30,"carb"] = 대체값

hp_mean = X["hp"].mean()
hp_std = X["hp"].std()
대체값 = hp_mean + 1.5*hp_std
X.loc[30,"hp"] = 대체값

# 데이터 스케일링 (필요시)
from sklearn.preprocessing import StandardScaler
temp = X[["qsec"]]

# 파생변수 생성
wt_mean = X["wt"].mean()
condition = X["wt"] > wt_mean
X.loc[condition, "wt_class"] = 1
X.loc[~condition, "wt_class"] = 0
X.drop(columns = "wt", inplace = True)

# 데이터 분리하기
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size= 0.3 , random_state= 10)




print(X.head())
print("code is work")