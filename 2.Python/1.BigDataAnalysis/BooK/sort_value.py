import pandas as pd
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\boston.csv")
# list의 sort와 DataFrame의 sort_value는 힙의 참조하는 방식이 다르다. sort 는 수정용 / sort_value는 출력용
# loc = location // iloc = index location
"""boston 데이터 세트의 MEDV 칼럼을 기준으로 30번째로 큰 값을 1~29번째로 큰 값에 적용한다.
    그리고 MEDV 칼럼의 평균값, 중위값, 최솟값, 최댓값 순으로 한줄에 출력하시오."""

# list의 sort 메서드는 힙에 저장된 객체를 바로 변환한다! (출력용이라기 보다는 수정용)
list1 = [1,2,4,5,6,7,-55,99,3,16]
list1.sort()
# print(list1) # sorting된 결과


# df 스택 생성
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\boston.csv")
val = df.sort_values(by = "MEDV",ascending=False)["MEDV"].iloc[29] # 값을 포인터 val 스택생성
a = df["MEDV"] # 의미없음! 

# 1) list 의 sort 메서드처럼 힙을 바로 참조하지는 않는다. 출력용 
#print("this is sorting: ",a.sort_values(ascending=False).head())

# 2) 위의 경우와 마찬가지로 힙의 객체를 포인팅할 Frame이 없다
df.sort_values(by = "MEDV", ascending = False)["MEDV"].iloc[0:29] = val
#print("need a new heap!:" ,df["MEDV"].head())

# 3) list의 sort 메서드처럼 힙을 바로 참조하지는 않는다.
# sort_values method
a.sort_values(ascending=False) #판다스 시리즈 데이터의 sort_values 메서드는 힙의 객체를 변환하지 않는다.
# print("just method:",a) # a 값 sorting 되지 않음 (리스트와의 차이점!!!)

# 4) 대입은 바로 힙의 객체를 참조한다.
# print("before input method:" ,a.loc[(a >= val)].head() , "\n")
a.iloc[0:29] = val
# print("input is working with heap! : ", a.loc[(a >= val)].head()) # 값이 바뀌었으나 ascending 된 객체에서의 반환이아님!

# sort 된 dataframe의 객체를 참조하여 대입하는 방법
# 1) 스택에 새로운 변수를 추가
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\boston.csv")
new_heap = df["MEDV"].sort_values(ascending= False) # sort된 series객체를 힙에 저장
new_heap.iloc[0:29] = val # 프레임에서 포인팅할 객체가 존재하기 떄문에 해결가능
# print(new_heap.head()) # df에는 해당 내용이 저장되지 않는다.

# 2) 원본 dataframe 을 바꾸기
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\boston.csv")
df.sort_values(by = "MEDV", ascending = False, inplace = True) # dataframe을 sorting한 상태로 저장한다.
df["MEDV"].iloc[0:29] = val # 힙에 솔팅된 상태로 df가 저장되어 있고, 바로 대입연산을 진행한다.
#print(df["MEDV"].sort_values(ascending=False).iloc[0:29].head())

# 3) loc 을 써서 해보기
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\boston.csv")
df2 = df.sort_values(by = "MEDV", ascending=False) # 새로운 df2 프레임을형성하고 sorting된 객체를 포인팅
val = df2["MEDV"].iloc[29]  # 값 추출 단순 int
# print("val with location:" ,val) # 41.7
df2.reset_index(drop = False , inplace= True) # df2프레임이 포인팅한 힙의 객체의 "인덱스를 0부터 재설정하고 저장"
df2.loc[1:30 ,"MEDV"] = val # loc는 rownumber를 쓴다. df2의 힙에는 인덱스를 재설정한 dataframe이 저장되어 있으므로 1:30 작성
# print(df2.sort_values(by = "MEDV",ascending = False)["MEDV"].iloc[27:32])

