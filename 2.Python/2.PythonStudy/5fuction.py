class Solution:
    def longestConsecutive(self, nums=[]):
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                curr = 1
                while num + 1 in s:
                    curr += 1
                    num += 1
                longest = max(longest, curr)
        return longest
    
import pandas as pd
df = pd.read_csv(r"C:\Users\brian\Desktop\JUNSOO\study\2.Python\1.BigDataAnalysis\BooK\data\mtcars.csv")
class solution:
  def outlier(self, df:pd.DataFrame,column:str):
            mean = df[column].mean()
            std = df[column].std()
            lowest = mean - (std * 1.5)
            highest = mean + (std * 1.5)
            print("max_lier : ", highest,
              "min_lier : ", lowest)
            high_outlier = df.loc[df[column] >= highest].iloc[:,0]
            low_outlier = df.loc[df[column] <= lowest].iloc[:,0]
            return high_outlier, low_outlier
# 객체생성
Solution = solution()

result = Solution.outlier(df,"carb")
print(result)





