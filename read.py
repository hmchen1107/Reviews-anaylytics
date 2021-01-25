#read
n = 0

data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		n = n + 1
		if n % 1000 == 0:
			print(len(data))

print('File has been read, there are', len(data), 'datas')


 