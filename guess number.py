# August and Beatrice are playing a game. August thought of a natural number from 1 to n. Beatrice tries to guess this number, 
# for this she names some sets of natural numbers. August replies to Beatrice YES if among the numbers named by her there 
# is a plan or NO otherwise. After a few questions, Beatrice is confused about what questions she asked and what answers she got, 
# and asks you to help her figure out what numbers August might have been thinking.

# The first line contains n - the maximum number August could think of. Each line then contains Beatrice's 
# question (a set of numbers separated by a space) and Augustus' answer to that question.

# You must print, separated by a space, in ascending order, all the numbers that August could think of.

n = int(input())
AugustNumbers = [int(i) for i in input().split()]
numbers = AugustNumbers

while True:
    AugustAnswer = input()
    if AugustAnswer == 'YES':
        AugustNumbers = set(AugustNumbers) & set(numbers)
    elif AugustAnswer == 'NO':
        AugustNumbers = set(AugustNumbers) - set(numbers)

    BeatrisAnswer = input()
    if BeatrisAnswer == 'HELP':
        break
    else:
        numbers = [int(i) for i in BeatrisAnswer.split()]

print(*sorted(AugustNumbers, key=int))
