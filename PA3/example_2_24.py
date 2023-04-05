def func():
   infoFile = open("info.txt", "r")
   new_list = []
   for k in infoFile:
      new_list.append(int(k))
   return new_list
num = func()
print(num)

def getAvg(items):
    sum = 0
    count = 0
    for k in range(len(items)):
        sum += items[k]
        count += 1
    avg = sum / count
    return avg

num = func()
print (num)
ans = getAvg(num)
print("Average = ", ans)

f = open("info2.txt", 'w')
f.write(str(ans))
f.close()