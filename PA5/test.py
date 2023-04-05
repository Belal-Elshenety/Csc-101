def func(list):
  count = 0
  max = 0
  for k in range(len(list)):
    if list[k] > max:
      max = list[k]
      count += 1
  return count

list = [6,2,8,4,11,13]
ans = func(list)
print(ans)