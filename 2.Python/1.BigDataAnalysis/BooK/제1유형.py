"""boston 데이터 세트의 MEDV 칼럼에 대해서 가장 작은 값 부터 순서대로 10개 행을 출력해야한다.
    오름차순으로 정렬된 MEDV 값에서 TOP10을구하시오"""
# 공통제출코드
import pandas as pd
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\boston.csv")

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

print(abs(dropna_std - mean_na_std))



"""boston 데이터 세트의 ZN 컬럼을 대상으로 
    ZN 값의 평균값에서 표준편차의 1.5배보다 크거나 작은 ZN값의 합계를 구하시오"""

# 제출코드3
zn_mean = df["ZN"].mean()
zn_std = df["ZN"].std()
max_lier = zn_mean + zn_std * 1.5
min_lier = zn_mean - zn_std * 1.5
val1 = df.loc[(max_lier < df["ZN"])]["ZN"].sum()
val2 = df.loc[(min_lier > df["ZN"])]["ZN"].sum()
# print(val1 + val2)



"""boston 데이터 세트에서 CHAS 칼럼과 RAD 칼럼을 제외한 칼럼에 한해서
    칼럼별 IQR을 구하시오. 
    단 출력구조는 2열이고 1열은 모스턴 데이터 세트의 칼럼 이름이 표시 되어야 한다"""

# 제출코드4
df2 = df.describe().drop(columns = ["CHAS","RAD"]).T
IQR = df2["75%"] - df2["25%"]
#print(IQR)



"""boston 데이터 세트의 MEDV 칼럼을 기준으로 30번째로 큰 값을 1~29번째로 큰 값에 적용한다.
    그리고 MEDV 칼럼의 평균값, 중위값, 최솟값, 최댓값 순으로 한줄에 출력하시오."""

# sort_values 는 dataframe 을 리턴하지만 원래 값을 바꿔줘야함 ()
val = df.sort_values(by = "MEDV", ascending = False)["MEDV"].iloc[29]   # 메모리에 저장됨
print("val : ",val) # 41.7
# print("unique :" ,df["MEDV"].unique())
# df.sort_values(by = "MEDV", ascending = False , inplace = True) #매개변수 inplace 없으면 값대체 안된다.
df["MEDV"].sort_values(ascending = False).iloc[0:29] = val 
                                                           # inplace 가 없다면
                                                           # df["MEDV"].sort_values(ascending = False).iloc[0:29]
                                                           # 라는 새로운 스택에 val 을 저장하고
                                                           # df 자체에는 변화가 없음
                                                           # df["MEDV"].sort_values(ascending = False).iloc[0:29]
                                                           # 라는 스택은 변수가 아니기 때문에 다시 print 해도
                                                           # 같은 변수가아님 // 원래 값으로 되돌아감(list.sort랑 다른 개념)
                                                           # 메모리 스택 삭제됨!
# print(df["MEDV"].unique()) # 0~29 행 뿐만아니라 모든 행이 대체돼버림..
print(df.sort_values(by = "MEDV" , ascending=False).head(20))

# 이건 왜 될까
val = df.sort_values(by = "MEDV", ascending = False)["MEDV"].iloc[29] # 41.7
new_data = df.sort_values(by = "MEDV", ascending = False)["MEDV"] # 변수 생성 (sort한 값을 저장) 메모리스택에서 안날라감
df.sort_values(by = "MEDV", ascending = False)["MEDV"].iloc[0:29] = val
# new_data[0:29] = val   # 대입연산
# print(new_data.unique())
# print(new_data.head()) # 41.7로 대체됨


# loc 을 써서 해보잠
df2 = df.sort_values(by = "MEDV", ascending=False)
val = df2["MEDV"].iloc[29]
print("val with location:" ,val) # 41.7
df2.reset_index(drop = False , inplace= True) # reset index 했으므로 loc 쓰기 수월
df2.loc[1:30 ,"MEDV"] = val
print(df2.sort_values(by = "MEDV",ascending = False)["MEDV"].iloc[27:32])

# df.sort_values(by = "MEDV", ascending=True).loc[1:,"MEDV"].info() # = val
# print(df["MEDV"].sort_values(ascending=True).head())


"""boston 데이터세트의 TAX 칼럼이 TAX 칼럼의 중위값보다 큰 데이터를 대상으로,
    CHAS 칼럼과 RAD 칼럼 순으로 그룹을 지은후 각 그룹의 데이터 개수를 구하시오.
     단, CHAS,RAD 칼럼별 데이터 개수는 COUNT 라는 칼럼으로 출력합니다. """
tax_median = df["TAX"].median() # 330
new_data = df.loc[df["TAX"] > tax_median][["CHAS","RAD"]] # TAX 컬럼의 중위값보다 큰 데이터프레임 포인터

# df.groupby(그룹핑할 컬럼들)["그룹화된 컬럼중 하나"].count()

new_data = new_data.groupby(["CHAS","RAD"])["CHAS"].count() # 시리즈 데이터 !
new_data = pd.DataFrame(new_data) # 변수 지정 잘 하고 마지막에 print 잘 할것.
new_data.columns = ["COUNT"] # 데이터프레임클래스에서 멤버변수 객체지정
#print(new_data)



"""boston 데이터 세트의 TAX 칼럼을 
    오름차순으로 정렬한 결과와 내림차순으로 정렬한 결과를 각각구한다
    그리고 각 순번에 맞는 오름차순값과 내림차순 값의차이를 구하여 분산값을 출력하시오."""

new_data1 = df.sort_values(by = "TAX", ascending=False) # 내림차순
new_data2 = df.sort_values(by = "TAX", ascending=True) # 오름차순

new_data1 = new_data1["TAX"].reset_index(drop=True) # 인덱스 설정을 해야 concat시 새로운 인덱스를 기준으로 병합
new_data2 = new_data2["TAX"].reset_index(drop=True)

data = pd.concat([new_data1, new_data2], axis = 1)  # concat시 series 데이터는 자동으로 dataframe으로 변환?
data["차이"] = abs(data.iloc[:,0] - data.iloc[:,1])
#print(data["차이"].var())


"""boston 데이터세트의 MEDV 컬럼을 최소최대 척도로 변환한후
    0.5보다 큰 값을 가지는 레코드 수를 구하시오"""

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

temp = df[["MEDV"]]
new_data = scaler.fit_transform(temp)   # df 를 넣고 나중에 선택해도 된다
new_data = pd.DataFrame(new_data, columns = temp.columns) #DataFrame 메서드 파라미터중 columns 유의!
#print(new_data.loc[new_data["MEDV"] > 0.5].count())


"""boston 데이터 세트의 AGE 컬럼을 소수점 첫 번쨰 자리에서 반올림 하고,
    가장 많은 비중을 차지하는 AGE 값과 그 개수를 차례대로 출력하시오.
    즉, AGE 칼럼의 최빈값과 그 개수를 출력하시오."""
new_data = df["AGE"].round()
new_data = pd.DataFrame(new_data)
new_data = new_data.groupby(["AGE"])["AGE"].count()
new_data = pd.DataFrame(new_data)
new_data.columns = ["COUNT"]
new_data = new_data.reset_index(drop = False)   # groupby 한 프레임이 정돈된다!** 
                                                # AGE 인덱스사용하기 위해서 drop = False
#print(new_data.head())
print(new_data.sort_values(by = "COUNT", ascending=False).iloc[0,0],
new_data.sort_values(by = "COUNT", ascending=False).iloc[0,1])


"""boston 데이터 세트의 DIS 칼럼을 표준화 척도로 변환한 후, 
    0.4 보다 크면서, 0.6 보다 작은 값들에 대한 평균을 구하시오.
    단, 소수점 셋째 자리에서 반올림하여 소수점 둘째 자리까지 출력하시오."""
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
temp = df[["DIS"]]
new_data = pd.DataFrame(scaler.fit_transform(temp), columns = temp.columns)

new_data = new_data.loc[(0.4 < new_data["DIS"]) & (new_data["DIS"] <0.6)] # loc 내의 condition and 말고 &
print(round(new_data["DIS"].mean(),2))


"""boston 데이터의 전체 칼럼에 대해서 중복을 제거한
    유니크한 값을 구한후, 칼럼별로 유니크한 값의 개수를 기준으로 평균값을 구하시오."""
colums_count = df.columns.size   # 14
new_data = pd.DataFrame(df.nunique())
new_data.columns = ["count"]
sum = new_data["count"].sum()
result = sum / colums_count
#print(result)
#print("Code is work")





