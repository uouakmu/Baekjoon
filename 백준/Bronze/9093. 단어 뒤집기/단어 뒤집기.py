for i in range(int(input())):
    s = list(input().split(' '))
    for word in s:
        print(word[::-1],end=" ")
    print()