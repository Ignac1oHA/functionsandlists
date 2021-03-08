# empty list
a = []
b = [1, 2, 3, 4, 5]
c = [9+8, "Noo", "-7", None]
print(a, b, c)
d = [1, 2,[ 3, 4, [5, 6]]]
print(d)
print(len(d))
#List operations:
a = [1, 2, 3]
b = ["a", "b", "c"]
c = a + b
print(c)

e = 4*a
print(e)
print(e[1])
e[1]=7
print(e)

for item in e:
    print(item)

list = [1, 3, 4, 7, 9]
print(list[1])
print(1 in list)

print(list[1:3])
print(list[::-1])

print(5 in list)

t = [1, 2, 3]
x=t.pop(1)
print(x)


