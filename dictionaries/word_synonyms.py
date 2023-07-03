n = int(input())
synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonym_list in synonyms.items():
    synonyms_str = ', '.join(synonym_list)
    print(f'{word} - {synonyms_str}')