# Anya and Borya play multi-colored cubes, and each of them has his own set, and in each set all the cubes are different in color. 
# Once the children were interested, the number of such colors that the cubes of each color are present in the set. To do this,
# they numbered all the colors with random numbers from 0 to 108. On this path, they ran out, so it's up to you to help them in 
# the rest.

# In the first stage of input data on the concentration of substances N and M - the number of cubes Anya and Borya have. 
# The next N lines contain the numbers of the colors of Anya's cubes. In the last M rows of numbers Bor colors.

# three types: numbers of colors that are in sets; the number of dice colors that only Anya has and the number of dice 
# colors that only Borya has. For each set, you enter first the number of elements in it, and then the elements themselves, 
# sorted by age.

Anya_Borya = [int(i) for i in input().split()]
Anya = []
Borya = []
for i in range(Anya_Borya[0]):
    Anya.append(int(input()))
for i in range(Anya_Borya[1]):
    Borya.append(int(input()))
print(len(set(Anya) & set(Borya)))
print(*sorted(set(Anya) & set(Borya), key=int))
print(len(set(Anya) - set(Borya)))
print(*sorted(set(Anya) - set(Borya), key=int))
print(len(set(Borya) - set(Anya)))
print(*sorted(set(Borya) - set(Anya), key=int))