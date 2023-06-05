number_list = input().split()

absolute_value = []

for num in number_list:
    absolute_value.append(abs(float(num)))


print(absolute_value)