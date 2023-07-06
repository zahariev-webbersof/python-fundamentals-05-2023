data = input().split()
new_text = [word * len(word) for word in data]

print(''.join(new_text))