n = int(input())
mapping = []
for i in range(6):
    mapping.append(list(map(int, input().split())))


ew_map_length = [[x,[w,v]] for x,[w,v] in enumerate(mapping) if w <= 2]
temp_max = max([v for [x, [w,v]] in ew_map_length])
ew_index = [[x,[w,v]] for x,[w,v] in ew_map_length if v == temp_max][0][0]

sn_map_length = [[x, [w,v]] for x,[w,v] in enumerate(mapping) if w >  2]
temp_max = max([v for [x, [w,v]] in sn_map_length])
sn_index = [[x,[w,v]] for x,[w,v] in sn_map_length if v == temp_max][0][0]

result = mapping[ew_index][1] * mapping[sn_index][1] - mapping[(ew_index+3)%6][1] * mapping[(sn_index+3)%6][1]
print(result*n)
