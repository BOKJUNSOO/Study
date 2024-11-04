"""객체를 호출해야 self 인자를 받지 않는다"""
class Solution:
    def chess(self,piece : list) -> list:
        right_piece = [1,1,2,2,2,8]
        answer = [None] * 6
        for i in range(len(piece)):
            if piece[i] == right_piece[i]:
                answer[i] = 0
            else:
                need = right_piece[i] - piece[i]
                answer[i] = need
        return answer
    
solution = Solution()
#num_list = list(map(int, input().split()))
#result = solution.chess(num_list)
#for i in result:
#    print(i, end=" ")

"""함수는 return 값을 만족하면 스택을 지우고, 호출을 종료하며 값을 반환한다"""
# 10988
class Solution:
    def droom(self,word:str) -> bool:
        word_len = len(word)
        if word_len%2 == 0: #even
            check_idx = (word_len)//2
            for i in range(check_idx):
                if word[i] == word[-i-1]:
                    continue
                else:
                    return False
        if word_len%2 != 0: # odd
            check_idx = ((word_len)//2)-1
            for i in range(check_idx):
                if word[i] == word[-i-1]:
                    continue
                else:
                    return False
        return True 


# 1157
class Solution:
    def study(self, word:str) -> str:
        word = word.upper() #copy 한 str을 upper(스택의 값을 변경 안함)
        word_list = list(set(word))
        counting_list = []
        for i in word_list:
            count = 0
            for j in range(len(word)):
                if i == word[j]:
                    count += 1
                else:
                    continue
            counting_list.append(count)
        key= word_list
        value = counting_list
        di = dict(zip(key,value))
        max_count = [k for k, v in di.items() if max(di.values()) == v]
        if len(max_count) != 1:
            return "?"
        else:
            return max_count[0]

# 2941
class Solution:
    def alpha(self,word:str) ->int:
        alpha_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]
        for i in alpha_list:
            if i in word:
                word = word.replace(i,"*")
        return word

# 1316 - for / break
class Solution:
    def main(self) -> int:
        number = int(input())
        for i in range(number):
            word = input()
            # check word
            for j in range(len(word)):
                if word[j] in word[j+1:]:
                    if word[j] != word[j+1]:
                        number -= 1
                        break   # 가장 가까운 for 문을 break
                    else:
                        continue
        return number   # for 문을 탈출한 결과

# 25206
import sys
class Solution:
    def my_score(self)->int:
        score_list = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
        sum_mean_score = 0
        get_score_sum = 0
        for i in range(20):
            a,b,c = map(str,sys.stdin.readline().split())
            학점 = float(b) # int로 쓰면 메모리 할당이 더 커진다.?
            grade = c
            if grade == "P":
                continue
            else:
                for key, value in score_list.items():
                    if key == grade:
                        grade = value
                sum_mean_score += 학점*grade
                get_score_sum += 학점
        return sum_mean_score/get_score_sum
solution = Solution()
result = solution.my_score()
print(result)


