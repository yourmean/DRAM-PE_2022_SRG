# 엿장수 준호

values = list(map(int, input().split()))
num_trees = values[0]
cut_cost = values[1]
sell_price = values[2]
trees = []

for _ in range(num_trees):
	trees.append(int(input()))
total_answer = 0
for i in range(1, max(trees)+1):
	answer = 0
	for j in range(num_trees):
		if trees[j] >= i:
			num_pieces = int(trees[j] / i)
			if trees[j] % i == 0:
				num_cut = int(trees[j] / i) - 1
			else:
				num_cut = int(trees[j] / i)
			if (num_pieces * sell_price * i - num_cut * cut_cost > 0):
				answer += num_pieces * sell_price * i - num_cut * cut_cost
	if (answer > total_answer):
		total_answer = answer

print(total_answer)