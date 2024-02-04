from math import sqrt


def pri(k):
    for i in range(2,int(sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True

L = int(input())
sum,ret = 0,0
for i in range(2,100000):
    if pri(i):
        sum += i
        if sum <= L:
            print(i)
            ret += 1
        else:
            break
print(ret)
        
    