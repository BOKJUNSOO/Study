class Soltion:
    def coin(self,N:int,K:int)-> int:
        coin_list = []
        count = 0
        for i in range(N):
            coin = int(input())
            coin_list.append(coin)
        coin_list.sort(reverse = True)
        for coin in coin_list:
            if K < coin:
                continue
            else:
                val = K//coin
                K %= coin
                count += val
        return count

class Solution:
    def main(self,n:int)->int:
        pass

