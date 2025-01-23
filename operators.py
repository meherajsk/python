x = 5
y = 3

print(x + y)
print(x - y)    
print(x * y)    
print(x / y)    
print(x % y)
print(x ** y)
print(x // y)

#assignment operators

print("Assignment operators")

x = 5
x += 3  # x = x + 3
print(x)

x = 5
x -= 3  # x = x - 3
print(x)    

x = 5   
x *= 3  # x = x * 3
print(x)

x = 5
x /= 3  # x = x / 3

x = 5
x %= 3  # x = x % 3
print(x)

x = 5
x //= 3  # x = x // 3
print(x)

x = 5   
x **= 3  # x = x ** 3
print(x)

x = 5
x &= 3  # x = x & 3
print(x)

x = 5   
x |= 3  # x = x | 3
print(x)

x = 5
x ^= 3  # x = x ^ 3
print(x)

x = 5
x >>= 3  # x = x >> 3
print(x)

x = 5
x <<= 3  # x = x << 3
print(x)

print(x:=5)


print("Comparison operators")


x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


print("Logical operators")
#logical operators are used to combine conditional statements

x = 5
y = 3

print(x < 5 and y < 5)
print(x < 5 or y < 5)
print(not(x < 5 and y >10))


print("Identity operators")
#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


print("membership operators")
#Membership operators are used to test if a sequence is presented in an object:

x = ["apple", "banana"] 
print("banana" in x)
print("pineapple" not in x)

print("Bitwise operators")
#Bitwise operators are used to compare (binary) numbers:

print(5 & 3) # 5 = 101, 3 = 011
print(5 | 3) # 5 = 101, 3 = 011
print(5 ^ 3)
print(~5)
print(5 << 3)
print(5 >> 3)
