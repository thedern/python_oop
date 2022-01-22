from udemy import MaxSize

a = MaxSize(4)
b = MaxSize(1)

a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)

b.push('cat')
b.push('dog')

print(a.get_list())
print(b.get_list())

