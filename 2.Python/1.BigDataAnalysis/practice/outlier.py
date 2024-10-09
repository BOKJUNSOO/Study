"""데이터프레임과 컬럼을 입력받으면, 이상치 인덱스가 리턴된다"""
class OutlierSearch():
    def __init__(self,df):
        pass
    def outlier(self,df,column):
        mean = df[column].mean()
        std = df[column].std()
        lowest = mean - (std * 1.5)
        highest = mean + (std * 1.5)
        print("최대경계값 : ", highest,
              "최소경계값 : ", lowest)
        high_outlier = df.loc[self.df[self.column] >= highest].iloc[:,0]
        low_outlier = df.loc[self.df[self.column] <= lowest].iloc[:,0]
        return print(high_outlier, low_outlier)
