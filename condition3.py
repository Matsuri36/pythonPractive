# The text is given: the number of lines is written in the first line, then the lines themselves follow. 
# Determine how many different words are in this text.

# A word is a sequence of consecutive non-blank characters, words separated by one or more spaces or end-of-line characters.

n = int(input())
text = []
for i in range(n):
    text.extend(input().split())
print(len(set(text)))