# dial
class Solution:
    def dial(self,alpha : str):
        list = ["abc","def","ghi","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
        second = 0
        for i in range(len(alpha)):
            for j in range(len(list)):
                if alpha[i] in list[j]:
                    second += j
                else:
                    continue
        return second
a = "WA"
solution = Solution()
result = solution.dial(a)
print(result)


            



