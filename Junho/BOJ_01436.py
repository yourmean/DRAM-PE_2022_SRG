n = int(input())

x= 666
count=0

while True:
    if "666" in str(x) : 
        count += 1
        if count == n :
            break
    
    x += 1
    
print(x)
