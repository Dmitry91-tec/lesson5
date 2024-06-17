immutable_var = ([1,2], 'string', 7)
print(type(immutable_var))
print(immutable_var)
# immutable_var [2] = 5     // операция невыполнима, особенность типа данных кортеж - запрет на изменение элементов
immutable_var [0][1] = 7   # возможна замены значений внутри элемента с типом данных список,но не замена всего элемента
print(immutable_var)
mutable_list = ['orange', 'apple', 6, [0,9]]
print(type(mutable_list))
mutable_list [0] = 'coconut'
mutable_list [3] = 3
mutable_list [2] = [3,4]
print(mutable_list)