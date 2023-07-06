while True:
    command = input()

    if command == 'end':
        break

    print(f'{command} = {command[::-1]}')