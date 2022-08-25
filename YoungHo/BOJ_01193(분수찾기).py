n = int(input())

line = 0
total = 0

while n > total:
    line += 1
    total += line

num = total - n

# line이 짝수일때 top은 +1 , bottom은 -1
if line % 2 == 0:
    top = line - num
    bottom = num + 1
    
# line이 홀수일때 top은 -1, bottom은 +1
else:
    top = num + 1
    bottom = line - num
    
print("%d/%d"%(top,bottom))
