a = 5
print(a)

a += 1
print(a)

s1 = "alpharithms"
print(s1)

# concatenate some text
s1 += " is cool."
print(s1)

a1 = ['a', 'l', 'p', 'h', 'a', 'r', 'i', 't', 'h', 'm', 's']
a1[-1] = "\0"
print(a1)

# change integer item
a2 = [1, 2, 3, 4, 5]
a2[0] = 6
print(a2)

b1 = "alpharithms"
b2 = b1 - "s"
print(b2)

b1 = "alpharithms"
b1 -= "s"
print(b1)

s1 = "alpharithms"

s2 = s1 * " is cool"

# attempt an assignment operation
s1 *= " is cool"

s1 = "alpharithms"

# Use multiplication modifier with an integer value
# to create a new string made of duplicates of the
# initial string
s2 = s1 * 5

print(s2)
