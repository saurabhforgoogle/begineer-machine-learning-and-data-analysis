#Mr. Yash asks all the great programmers of the world to solve a trivial problem. He gives them an integer m and asks for the number of positive integers n, such that the factorial of n ends with exactly m zeroes. Are you among those great programmers who can solve this problem?

#Input First line of input contains an integer T number of test cases. Each test case contains an integer M (1 ≤ M ≤ 100,000) — the required number of trailing zeroes in factorial.

#Output First print k — the number of values of n such that the factorial of n ends with m zeroes. Then print these k integers in increasing order.




n=int(input())
count=0
list1=[]
mainlist=[]
count2=0
count5=0
count10=0
while(n!=0):
    m=int(input())
    mainlist.append(m)
    n-=1
maximum=max(mainlist)

for j in range(1,1000000):
    k1=j
    while(k1%5==0):
        count5+=1
        k1=k1//5
    while(k1%2==0):
        count2+=1
        k1=k1//2
    list1.append(min(count2,count5))
    if(min(count2,count5)>maximum):
        break
    
for z in mainlist:
    
    count=0
    for k in range(len(list1)):
        if(list1[k]==z):
            count+=1
    print(count)
    for k in range(len(list1)):
        if(list1[k]==z):
            print(k+1,end=" ")
    print("\n")
    