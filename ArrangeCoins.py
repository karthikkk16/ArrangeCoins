def ArrangeCoins(num):
    count=0
    for i in range(1,num+1):
        if num>=i:
            num-=1
            count+=1
    return count
number=int(input())
print(ArrangeCoins(number))