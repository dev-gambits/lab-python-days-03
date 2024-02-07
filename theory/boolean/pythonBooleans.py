# Booleans in Python

# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.

print('Code Boolean')
print()
print("Boolean evaluated:  10 > 9", 10 > 9)
print("Boolean evaluated:  not 10 == 9", not 10 == 9)
print("Boolean evaluated:  10 == 9", 10 == 9)
print("Boolean evaluated:  10 < 9", 10 < 9)

valueTrue = True
valueFalse = False
valueNone = None


print("Se imprime boolean True:", valueTrue)
print("Se imprime boolean False:", valueFalse)
print("Se imprime boolean None:", valueNone)

print()
print('Boolean condition in an if statement:')
# When you run a condition in an if statement, Python returns True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print()
print(bool("Hello"))
print(bool(15))
print(bool())

print()
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print()
print('Examples Boolean')
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
