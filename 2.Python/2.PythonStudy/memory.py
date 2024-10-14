# 기본자료형
a = 10
b = [1,2,3,4]
def fuction():
    #global a, b
    a = 20
    b.extend([5,6,7,8])
    print(a)
    print(b)
#fuction()
#print(a)
#print(b)

# 매개변수 복사
a = 10
b = [1,2,3,4]
print(a,b)
def fuction1(c,d):
    c = 20
    d = [5,6,7,8]
fuction1(a,b)
print(a,b)
def fuction2(c,d):
    c = 30
    d.extend([9,10])
fuction2(a,b)
print(a,b)
