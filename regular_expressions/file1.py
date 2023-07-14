import re

names = input()
pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"

matches = re.findall(pattern, names)

for name in matches:
    print(name, end=' ')