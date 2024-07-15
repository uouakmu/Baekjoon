n = int(input())
words = []
for _ in range(n):
    words.append(input())

words = list(set(words))

words.sort()
words.sort(key=lambda word: len(word))
for word in words:
    print(word)