# 3. Write a script to sum of the first n positive integers.

n = int(input("input a positive integer : "))
sum = 0
for i in range (1, n+1):
    sum += i

print(sum)