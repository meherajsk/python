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


print("Operator precedence")
#Operator precedence is a rule that defines the order in which the operators should be

print((6-4) - 2)
print(6 * (8-2))
print(6**7) # 6^7
print(100 - +2) # +x -x ~x
print(10 * 2 // 3 % 2) #if they have same precedence level then the will be executed from left to right
print(10 - 5 + 11 - 2) #Addition and subtraction
print(8 >> 4 - 2) #<<  >>	Bitwise left and right shifts
print(10 & 11) #Bitwise AND
print(10 ^ 11 -2) #Bitwise XOR
print(10 | 11 -2) #Bitwise OR
print(5 == 4 + 1) #==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
print(not 5 == 5) #not 	Logical NOT
print(1 or 2 and 3) #and
print(1 and 2 or 3) #or

