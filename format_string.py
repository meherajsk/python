age = 36


#error due to format
#txt = "my name is meheraj, i am " +  age
#print(txt)

#with format
txt = f"my name is meheraj, i am {age}"
print(txt) 

#modifier
txt = f"my name is meheraj, i am {age:.4f}"
print(txt)

#operation
txt = f"my name is meheraj, i am {4 * 9}"
print(txt)