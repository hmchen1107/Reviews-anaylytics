#read
data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print('File has been read, there are', len(data), 'datas')	

#1000000筆字串
#每一筆字串代表一個留言

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('每筆留言的平均長度為 : ' ,sum_len/len(data))






 