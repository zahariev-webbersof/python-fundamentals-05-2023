def sort_names():
    names_list = input().split(', ')
    sorted_names = sorted(names_list, key=lambda x: (-len(x), x))
    return sorted_names


result = sort_names()
print(result)