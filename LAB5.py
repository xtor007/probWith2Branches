import math
n = int(input("Введіть кількість чисел для виводу "))
x = int(input("Введіть кількість розрядів "))
L=0
if n<0 or x<=0:
    n=int(math.fabs(n))
    x=int(math.fabs(x))
for i in range(10**(x-1), (10**x)+1):
    if (L>=n):
        break
    k=False; number=i; temp=0
    while number != 0:
        temp=10*temp+number%10
        number//=10
    if temp==i and L<n:
        for j in range(2,i//2+1):
            if i%j==0:
                k=True
                break
        if k==False:
            L+=1
            print("%d) Number %d"%(L,i))
if L==0:
    print("Простих чисел-паліндромів не знайдено")