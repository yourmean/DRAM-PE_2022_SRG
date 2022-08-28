n = int(input())
number = list(map(int, input().split()))
s_num = list(sorted(set(number)))
s_dict = dict()
for i in range(len(s_num)):
    s_dict.update({str(s_num[i]): i})

result = []
for i in range(len(number)):
    result.append(str(s_dict.get(str(number[i]))))
print(' '.join(result))
