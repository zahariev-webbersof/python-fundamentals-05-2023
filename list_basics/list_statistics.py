n = int(input())

positives = []
negatives = []

for _ in range(n):
    number = int(input())

    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)

print(positives)
print(negatives)

print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')