fruit = ("apple", "banana", "cherry")
(green, yellow, red) = fruit

print(green)
print(yellow)
print(red)

fruit = ("apple", "banana", "orange", "rasberry", "mango")
(green, blue, *black) = fruit #asterisk to access the remaining data
print(black)
(green, *blue, black) = fruit
print(green)
print(blue)
print(black)


