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