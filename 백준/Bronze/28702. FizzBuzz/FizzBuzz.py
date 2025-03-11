a=list()
num=0

for i in range(3):
    s = input()
    a.append(s)
    if s not in {"Fizz", "Buzz", "FizzBuzz"}:
        num = int(s)+(3-i)
if num%3 == 0 and num%5 != 0:
    print("Fizz")
elif num%5 == 0 and num%3 != 0:
    print("Buzz")
elif num%3 == 0 and num%5 == 0:
    print("FizzBuzz")
else:
    print(num)