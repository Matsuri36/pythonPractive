# The input string contains a sequence of numbers separated by a space. For each number, 
# print the word YES (on a separate line) if this number has previously occurred in the sequence, or NO if it has not.

a = [int(i) for i in input().split()]
b = []
for i in a:
    if i not in b:
        print('NO')
        b.append(i)
    elif i in b:
        print('YES')