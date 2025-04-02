w_data = []
k_data = []

for i in range(20) :
  if i < 10 :
    w_data.append(int(input()))
  else :
    k_data.append(int(input()))

w_data.sort(reverse=True)
k_data.sort(reverse=True)

print(sum(w_data[:3]), sum(k_data[:3]))