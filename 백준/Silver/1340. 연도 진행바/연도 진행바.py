month, day, year, time = input().split()
day = int(day[:-1])
year = int(year)
h, m = map(int, time.split(':'))

month_name = ["January" , "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"]
count_day = [31,28,31,30,31,30,31,31,30,31,30,31]

if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    count_day[1] += 1
total_time =sum(count_day)*24*60

last_month = month_name.index(month)
current_time = (sum(count_day[:last_month]) + day-1)*24*60 + h*60 + m
print(current_time/total_time * 100)