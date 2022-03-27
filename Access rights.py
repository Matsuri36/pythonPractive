# A virus penetrated the file system of one supercomputer, which broke the control over file access rights. 
# For each file, it is known what actions can be accessed with it:

# record W,
# reading R,
# launch X.

# The first line contains the number N — the number of files contained in the given file system. 
# The next N lines contain the names of the files and the operations allowed with them, separated by spaces. 
# Next, the number M is indicated - the number of requests to files. The last M lines contain a query of the form Operation File. 
# Any number of requests can be applied to the same file.

# You need to regain control over file access rights (your program will need to return OK for each request if a valid operation is 
# being performed on the file, or Access denied if the operation is invalid.

c = {
    "read": "R",
    "write": "W",
    "execute": "X"
}

a = {}
for _ in range(int(input())):
    d = input().split()
    a[d[0]] = d[1:]

for _ in range(int(input())):
    d = input().split()
    if c[d[0]] in a[d[1]]:
        print('OK')
    else:
        print('Access denied')