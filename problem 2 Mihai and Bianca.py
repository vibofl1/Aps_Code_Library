'''Mihai and Bianca are playing with bags of candies. They have a row 𝑎
 of 𝑛
 bags of candies. The 𝑖
-th bag has 𝑎𝑖
 candies. The bags are given to the players in the order from the first bag to the 𝑛
-th bag.

If a bag has an even number of candies, Mihai grabs the bag. Otherwise, Bianca grabs the bag. Once a bag is grabbed, the number of candies in it gets added to the total number of candies of the player that took it.

Mihai wants to show off, so he wants to reorder the array so that at any moment (except at the start when they both have no candies), Mihai will have strictly more candies than Bianca. Help Mihai find out if such a reordering exists.

Input
The first line of the input contains an integer 𝑡
 (1≤𝑡≤1000
) — the number of test cases.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤100
) — the number of bags in the array.

The second line of each test case contains 𝑛
 space-separated integers 𝑎𝑖
 (1≤𝑎𝑖≤100
) — the number of candies in each bag.

Output
For each test case, output "YES" (without quotes) if such a reordering exists, and "NO" (without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer)'''

n=int(input()) 
def fun():
    x=int(input())
    arr=list(map(int,input().split()))
    m=0
    b=0
    for x in arr:
        if x%2==0:
            m+=x 
        else:
            b+=x 
    if m>b:
        return "YES"
    else:
        return "NO"
    
    
    
for t in range(n):
    print(fun())