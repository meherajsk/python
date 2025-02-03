tuple1 = ("a", "b", "c", "d")
tuple2 = (1, 2, 3, 4)
tuple3 = tuple1 + tuple2
print(tuple3) # ('a', 'b', 'c', 'd', 1, 2, 3, 4)

tuple4 = tuple1 * 3
print(tuple4) # ('a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd')   


x = tuple4.count("a")
print(x)
y = tuple4.index("b")
print(y)
z = tuple4.index("b", 2)
print(z)
