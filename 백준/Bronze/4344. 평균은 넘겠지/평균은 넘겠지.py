for i in range(int(input())):
    scores = list(map(int,input().split()))
    average = sum(scores[1:])/scores[0]

    high_score = [i for i in range(1,len(scores)) if scores[i]>average]
    ans = (len(high_score ) /scores[0])*100
    print(f"{ans:.3f}%")