

import os
"""

f = open("python/formatting.py", "r")
print(f.read())
f.close()


print()
f = open("python/formatting.py", "r")
print(f.read(100))
f.close()

"""

print()
f = open("formatting.py", "r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()


print()
f = open("formatting.py", "r")
for x in f:
  print(x)  # Loop through the file line by line:
f.close()



print()
f = open("formatting.py", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("formatting.py", "r")
print(f.read())
f.close()

"""
f = open("formatting.py", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("formatting.py", "r")
print(f.read())
f.close()

the "w" method will overwrite the entire file.


f = open("jj.py", "x")
print(f.read())
f.close()

"""



f = open("kk.py", "w")
f.close()
#file is created here


if os.path.exists("kk.py"):
  os.remove("kk.py")
else:
    print("The file does not exist")
#file is deleted here


os.mkdir("myfolder")
#os.rmdir("myfolder")
#folder is deleted here