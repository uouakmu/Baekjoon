two_to_eight = {
    '000': '0',
    '001': '1',
    '010': '2',
    '011': '3',
    '100': '4',
    '101': '5',
    '110': '6',
    '111': '7'
}

num = input()
result = ""

while len(num) % 3 != 0:
    num = "0" + num

while num:
    result = result + two_to_eight[num[0:3]]
    num = num[3:]

print(result)