data = [13, 17, 31, 57,  '', 41, 83]

def del_empty(list):
	for i in list:
		if i == '':
			list.remove(i)

def data_avg(list):
	total = 0
	for i in list:
		total+=i
	avg = total / len(data)
	return avg

del_empty(data)
avg = data_avg(data)
print(f'平均値：{avg}')