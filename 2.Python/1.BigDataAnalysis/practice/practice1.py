"""boston 데이터 세트의 MEDV 칼럼에 대해서 가장 작은 값 부터 순서대로 10개 행을 출력해야한다.
    오름차순으로 정렬된 MEDV 값에서 TOP10을구하시오"""
# 공통제출코드
import pandas as pd
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\boston.csv")

# 제출코드1
# print(df.sort_values(by = "MEDV", ascending = True)["MEDV"])

"""boston 데이터 세트의 RM 칼럼에 대한 결측치 처리를 평균값으로 대치하거나 삭제할 수 있다.
RM 칼럼의 결측치를 평균값으로 대치한후에 산출된 표준편차값
결측치를 삭제한후에 산출된 표준편차 값의 차이를 구하시오"""

# 제출코드2

# 결측값 삭제후 표준편차
dropna_std = df["RM"].dropna().std()

# 평균값 대치후 표준편차
rm_mean = df["RM"].mean()
df["RM"].fillna(rm_mean, inplace = True)
mean_na_std = df["RM"].std()

# print(abs(dropna_std - mean_na_std))

"""boston 데이터 세트의 ZN 컬럼을 대상으로 
    ZN 값의 평균값에서 표준편차의 1.5배보다 크거나 작은 ZN값의 합계를 구하시오"""

# 제출코드3
zn_mean = df["ZN"].mean()
zn_std = df["ZN"].std()
max_lier = zn_mean + zn_std * 1.5
min_lier = zn_mean - zn_std * 1.5
#print(df.loc[(max_lier < df["ZN"])]["ZN"].sum())
#print(df.loc[(min_lier > df["ZN"])]["ZN"].sum())

"""boston 데이터 세트에서 CHAS 칼럼과 RAD 칼럼을 제외한 칼럼에 한해서
    칼럼별 IQR을 구하시오. 
    단 출력구조는 2열이고 1열은 모스턴 데이터 세트의 칼럼 이름이 표시 되어야 한다"""

# 제출코드4
df2 = df.describe().drop(columns = ["CHAS","RAD"]).T
IQR = df2["75%"] - df2["25%"]
#print(IQR)

"""boston 데이터 세트의 MEDV 칼럼을 기준으로 30번째로 큰 값을 1~29번째로 큰 값에 적용한다.
    그리고 MEDV 칼럼의 평균값, 중위값, 최솟값, 최댓값 순으로 한줄에 출력하시오."""



print("Code is work")
