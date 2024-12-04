x,y = map(int,input().split())
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

date=[0,31,28,31,30,31,30,31,31,30,31,30,31]
all_date=0

for i in range(len(date)):
    if x>i:
        all_date += date[i]
all_date += y

print(day[all_date%7])