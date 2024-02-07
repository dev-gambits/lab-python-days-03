# Functions can Return a Boolean
def myBooleanTrueFunction() :
  return True

print(myBooleanTrueFunction())

print()
print()
def myBooleanFalseFunction() :
  return False

print(myBooleanFalseFunction())

# Print "YES!" if the function returns True, otherwise print "NO!":
print()
print('Print "YES!" if the function returns True, otherwise print "NO!":')
def myTrueFunction() :
  return True

if myTrueFunction():
  print("YES!")
else:
  print("NO!")

# Print "NO!" if the function returns True, otherwise print "YES!":
print()
print('Print "NO!" if the function returns True, otherwise print "YES!":')
def myFalseFunction() :
  return False

if myFalseFunction():
  print("YES!")
else:
  print("NO!")


# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
# Check if an object is an integer or not:
print()
print('Check if an object is an integer or not')
x = 200
print(isinstance(x, int))