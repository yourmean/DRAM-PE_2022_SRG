k = int(input())

g = int((1+(8*k-7)**(1/2))/2)

an = (g**2-g+2)/2
diff = k-an

if g % 2 == 0:
    numerator = 1 + diff
    denominator = g - diff
else:
    numerator = g - diff
    denominator = 1 + diff
    
result = str(int(numerator)) + '/' + str(int(denominator))
print(result)
