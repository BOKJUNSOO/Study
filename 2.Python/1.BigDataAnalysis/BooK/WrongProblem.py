# list의 sort 메서드는 힙에 저장된 객체를 바로 변환한다! (출력용이라기 보다는 수정용)
list1 = [1,2,4,5,6,7,-55,99,3,16]
list1.sort()
# print(list1) # sorting된 결과

# 교재에 있는 1유형 문제중 틀렸던 문제

import pandas as pd
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\data\boston.csv")
pd.options.display.max_columns = None
"""boston 데이터 세트의 MEDV 칼럼을 기준으로 30번째로 큰 값을 1~29번째로 큰 값에 적용한다.
    그리고 MEDV 칼럼의 평균값, 중위값, 최솟값, 최댓값 순으로 한줄에 출력하시오."""

val = df["MEDV"].sort_values(ascending = False).iloc[29]

# 1)
df.sort_values(by = "MEDV",ascending = False).iloc[0:29] = val # sort_values 를 호출하고 스택에서 삭제된다.
                                                               # 해당 메서드를 저장할 프레임이 없어서 스택에서 날라가고,
                                                               # 저장이 안된다
                                                               # df의 저장된 프레임을 sort_value 메서드는 바로 참조하지 않는다
print("need frame for stack! :",df.sort_values(by = "MEDV",ascending = False)["MEDV"])   # 대체안됨

# 2)
new_heap = df.sort_values(by="MEDV", ascending= False) # sort_values 를 호출하고 스택에서 삭제된다.
                                                      # 해당 메서드를 new_heap이라는 새로운 프레임에 저장한다.
                                                      # 포인팅할 프레임이 생긴다
new_heap["MEDV"].iloc[0:29] = val
print("hear is new heap! :" ,new_heap.sort_values(by = "MEDV",ascending=False)["MEDV"])

# 3) 
df.sort_values(by = "MEDV",ascending = False,inplace= True) # sort_values 호출하고 스택에서 삭제된다 
                                                            # 해당 메서드를 df 에 저장한다
df.iloc[0:29] = val
print("df stack is change! :",df.sort_values(by = "MEDV",ascending = False)["MEDV"])   # 대체됨

# 4) loc 을 써서 해보기
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\practice\kaggle\kaggledataset\boston.csv")
df2 = df.sort_values(by = "MEDV", ascending=False) # 새로운 df2 프레임을형성하고 sorting된 객체를 포인팅
val = df2["MEDV"].iloc[29]  # 값 추출 단순 int
# print("val with location:" ,val) # 41.7
df2.reset_index(drop = False , inplace= True) # df2프레임이 포인팅한 힙의 객체의 "인덱스를 0부터 재설정하고 저장"
df2.loc[1:30 ,"MEDV"] = val # loc는 rownumber를 쓴다. df2의 힙에는 인덱스를 재설정한 dataframe이 저장되어 있으므로 1:30 작성
# print(df2.sort_values(by = "MEDV",ascending = False)["MEDV"].iloc[27:32])


"""boston 데이터 세트의 AGE 컬럼을 소수점 첫 번쨰 자리에서 반올림 하고,
    가장 많은 비중을 차지하는 AGE 값과 그 개수를 차례대로 출력하시오.
    즉, AGE 칼럼의 최빈값과 그 개수를 출력하시오."""

"""boston 데이터 세트의 TAX 칼럼을 
    오름차순으로 정렬한 결과와 내림차순으로 정렬한 결과를 각각구한다
    그리고 각 순번에 맞는 오름차순값과 내림차순 값의차이를 구하여 분산값을 출력하시오."""