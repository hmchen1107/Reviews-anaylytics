#read
data = []
with open('reviews.txt', 'r') as f:
	for line in f:
	    data.append(line.strip())
print('File has been read, there are', len(data), 'datas.')	

#1000000筆字串
#每一筆字串代表一個留言

#============算留言的平均長度==============
#sum_len = 0
#for d in data:
#	sum_len = sum_len + len(d)
#print('每筆留言的平均長度為 : ' ,sum_len/len(data))
#print(sum_len)
#print(print(len(d))
#==========================================


#============清單塞選==============
new = []
for d in data:
        if len(d) < 100:
                new.append(d)
print('一共有',len(new), '筆留言長度小於100')
