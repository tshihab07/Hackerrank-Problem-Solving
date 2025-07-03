my_list = []
N = int(input())

for i in range(N):
    cmd = input().split()
    command = cmd[0]
    
    
    if command == 'insert':
        my_list.insert(int(cmd[1]), int(cmd[2]))
    elif command == 'append':
        my_list.append(int(cmd[1]))
    elif command == 'remove':
        my_list.remove(int(cmd[1]))
    elif command == 'sort':
        my_list.sort()
    elif command == 'pop':
        my_list.pop()
    elif command == 'reverse':
        my_list = list(reversed(my_list))
    elif command == 'print':
        print(my_list)