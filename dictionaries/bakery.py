data = input().split()

stock = {}

for i in range(0, len(data), 2):
    product = data[i]
    quantity = int(data[i + 1])
    stock[product] = quantity

print(stock)