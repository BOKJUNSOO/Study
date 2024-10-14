import pandas as pd


# 문제 1) https://www.kaggle.com/code/agileteam/tutorial-t1-2-python (2회)

"""데이터셋(basic1.csv)의 'f5' 컬럼을 기준으로 상위 10개의 데이터를 구하고,
'f5'컬럼 10개 중 최소값으로 데이터를 대체한 후, 
'age'컬럼에서 80 이상인 데이터의'f5 컬럼 평균값 구하기"""
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\basic1.csv")
df = df.sort_values(by = "f5", ascending=False)
# print(df.iloc[0:10].head(10))
ten_min = df.iloc[0:10,7].min() # 91.297791
df.iloc[0:10,7] = ten_min # 대체

condition = df["age"] >= 80
data = df.loc[condition]
result = data["f5"].mean()
# print(result)

"""데이터셋(basic1.csv)의 앞에서 순서대로 70% 데이터만 활용해서,
'f1'컬럼 결측치를 중앙값으로 채우기 전후의 표준편차를 구하고
두 표준편차 차이 계산하기"""


"""데이터셋(basic1.csv)의 'age'컬럼의 이상치를 더하시오!
단, 평균으로부터 '표준편차*1.5'를 벗어나는 영역을 이상치라고 판단함"""

# 문제2) 3회 기출
pd.options.display.max_columns = None
df1 = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\3_t1-data2.csv")
df2 = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\basic1.csv")

"""Q. 2022년 데이터(3_t1-data2.csv) 중 2022년 중앙값보다 큰 값의 데이터 수"""
# https://www.kaggle.com/code/agileteam/3rd-type1-1-3-1-1
#print(df1.head())
data = (df1.iloc[0])
m = data.median()
# print(data.loc[data > m].count())

"""Q. (basic1.csv) 결측치 데이터(행)을 제거하고, 앞에서부터 60% 데이터만 활용해, 'f1' 컬럼 3사분위 값을 구하시오."""
# https://www.kaggle.com/code/agileteam/3rd-type1-2-3-1-2
df2 = df2.dropna()
#df2.info()
key_count = df2["id"].count()
percentage = key_count * (60/100)
percentage = round(percentage)
# data = df2.iloc[1:percentage,3] # location 함수 다시 공부
data = df2.iloc[:int(len(df2)*0.6)]

# data.info() 60 퍼센트 데이터는 21개
# data = pd.DataFrame(data)
#print(data['f1'].quantile(.75))
#print(RESULT)


# 문제3) 4회 기출
""" data : basic1.csv
age 컬럼의 3사분위수와 1사분위수의 차를 절대값으로 구하고, 소수점 버려서, 정수로 출력"""

""" data : fb.csv
(loves반응+wows반응)/(reactions반응) 비율이 0.4보다 크고 0.5보다 작으면서,
type 컬럼이 'video'인 데이터의 갯수"""

"""data : nf.csv
1-3. date_added가 2018년 1월 이면서 country가 United Kingdom 단독 제작인 데이터의 갯수"""


#문제4) 세션의 지속 시간을 분으로 계산하고 가장 긴 지속시간을 출력하시오(반올림 후 총 분만 출력)
"""가장 많이 머무른 Page를 찾고 그 페이지의 머문 평균 시간을 구하시오 (반올림 후 총 시간만 출력)
사용자들이 가장 활발히 활동하는 시간대(예: 새벽, 오전, 오후, 저녁)를 분석하세요.
이를 위해 하루를 4개의 시간대로 나누고 각 시간대별로 가장 많이 시작된 세션의 수를 계산하고, 
그 중에 가장 많은 세션 수를 출력하시오"""
# https://www.kaggle.com/code/agileteam/t1-33-timedelta-py/notebook
# data : website.csv
# 새벽: 0시 부터 6시 전
# 오전: 6시 부터 12시 전
# 오후: 12 부터 18시 전
# 저녁: 18시 부터 0시 전
# user가 가장 많이 접속 했던 날짜를 출력하시오. (예, 2023-02-17)

