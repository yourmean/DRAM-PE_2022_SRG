# 호솔 규칙

def collatz(num):
    count = 0
    while num > 1:
        if count > 500:
            return -1
        num = num*3 + 1 if num%2 else num/2
        count += 1
    return count

a = int(input())
print(collatz(a))