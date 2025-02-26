price = 59
txt = f"The price is {price} dollars"
print(txt)

print()
price = 49
txt = f"The price is {price:.2f} dollars"
print(txt)


print()
txt = f"The price is {95:.2f} dollars"
print(txt)

print()
txt = f"The price is {20 * 59} dollars"
print(txt)


print()
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)


print()
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)



print()
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)


print()
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)




print()
price = 590000975
txt = f"The price is {price:,} dollars"
print(txt)



"""
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding Unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format
"""



print()
price = 49
txt = "The price is {} dollars"
print(txt.format(price))


print()
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))


"""print(txt.format(price, itemno, count))"""
print()
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

"""You can use index numbers (a number inside the curly brackets {0}) 
to be sure the values are placed in the correct placeholders:"""

print()
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


print()
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


print()
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!Now the file has more content!