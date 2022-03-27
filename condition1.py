# Two lists of numbers are given. Find all the numbers that are in both the first and the second list and output them in 
# ascending order.

print(*sorted(set(input().split())&set(input().split()), key=int))