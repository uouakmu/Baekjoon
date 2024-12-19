def count_iron_rod_falls(s):
    stack = []
    count = 0

    for i in range(len(s)):
        if s[i] == '(':  
            stack.append('(')
        else:  
            stack.pop()
            if s[i-1] == '(':  
                count += len(stack)  
            else:  
                count += 1
    return count

s = input().strip()
print(count_iron_rod_falls(s))