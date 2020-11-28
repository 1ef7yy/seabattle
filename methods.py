import seabattle


def to_str(arg, n=5):
	str_k = ''
	res = []

	app_list = ['\n']

	for idx, ele in enumerate(arg):
		if idx % n == 0:
			res.extend(app_list)
		res.append(ele)

	for i in res:
		str_k += str(i)


# input('Введите свои клетки')

	str_k = str_k[1:]
	# print(str_k)
	# print(enemy)
	return str_k


def decypher(k):
	c_error = 'Invalid coordinates'
	if len(k) != 2:
		print(c_error)
	elif k[0].isalpha() == False and k[1].isalpha() == True:
		print(c_error)
	elif k not in d:
		print(c_error)
	else:
		if seabattle.enemy[d[k]] == 1:
			print('Hit!')
		else:
			print('Miss!')


def check(m):
	if m in d:
		return True
	else:
		return False


d = {
	'a1': 0,
	'a2': 1,
	'a3': 2,
	'a4': 3,
	'a5': 4,

	'b1': 5,
	'b2': 6,
	'b3': 7,
	'b4': 8,
	'b5': 9,

	'c1': 10,
	'c2': 11,
	'c3': 12,
	'c4': 13,
	'c5': 14,

	'd1': 15,
	'd2': 16,
	'd3': 17,
	'd4': 18,
	'd5': 19,

	'e1': 20,
	'e2': 21,
	'e3': 22,
	'e4': 23,
	'e5': 24
}

# Я ЕГО РОТ ЕБАЛ БЛЯТЬ
# САМИ РАЗБИРАЙТЕСЬ В СВОЕЙ ХУЙНЕ
