# 2941
# string.replace() 방법을 떠올리지 못함
class Solution:
    def alpha(self,word:str) ->int:
        alpha_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]
        for i in alpha_list:
            if i in word:
                word = word.replace(i,"*")
        return word

# 방법은 찾았지만
# 컴프리헨션, dictionary 정의에 대한 이해 부족
# 1157
class Solution:
    def study(self, word:str) -> str:
        word = word.upper()
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
    
        
        

