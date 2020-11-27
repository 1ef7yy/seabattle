import random
import methods as m


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

random.shuffle(enemy)


# str_player = methods.to_str(player)
# str_enemy = methods.to_str(enemy)


print(str_player+'\n')
print(str_enemy)


# s = input('Input coordinates\n')
# methods.decypher(s)
