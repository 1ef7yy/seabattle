import random


# print('Начать игру?\n')
# input('ENTER\n')


enemy = [ 
  1, 1, 1, 1, 1,
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0

]

str_enemy = ''
str_player = ''


player = [
 
  1, 1, 1, 1, 1,
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0

]

random.shuffle(player)
random.shuffle(enemy)

def to_str(l, N = 5):
  str_k = ''
  res = []

  app_list = ['\n']

  for idx, ele in enumerate(l):
    if idx % N == 0:
      res.extend(app_list)
    res.append(ele)


  for i in res:
    str_k+=str(i)

#input('Введите свои клетки')


  count = []
  str_enemy=str_k[1:]
  # print(str_k)
  # print(enemy)
  return str_k

str_player = to_str(player)
str_enemy = to_str(enemy)
# print(str_player)
# print(str_enemy)