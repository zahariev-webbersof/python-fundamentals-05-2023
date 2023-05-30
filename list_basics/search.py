n = int(input())
special_word = input()

strings = []

for _ in range(n):
    string = input()
    strings.append(string)

print(strings)

filtered_strings = []

for string in strings:
    if special_word in string:
        filtered_strings.append(string)

print(filtered_strings)