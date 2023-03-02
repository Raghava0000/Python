# tuples : Sequence of multiple elements seperated with comma(,) which are declared inside ( )...

a=(43,54,'prakash',12.43,'rajesh',76)

print(a)

# print(type(a))

# nested tuples : Tuple inside the other tuple..

a=(43,54,'prakash',12.43,'rajesh',76,(21,23,24))

# print(a)

# print(type(a))

# # single value tuple

# a=(12,)

# print(a)
# print(type(a))

# accessing the elements inside the tuple is done using ---- indexing..

# indexing starts from 0..
# negative indexing starts from -1..


a=(43,54,'prakash',12.43,'rajesh',76,(21,23,24))

# print(a[2])

# print(a[1:5])

# print(a[-1])

# print(a[-4])

# print(a[-1:-6:-1])


# Tuples are immutable....

# a[0]=54 # It wont allow as tuples are immutable datatypes..


# Basic Operation:

    # concatenation(+): Adding 2 tuples elements and making it as single tuple
    # repetition(*) : Repeating the element of 1 tuple multiple no.of times in the single tuple..


# a=(1,2,3)
# b=(4,5,6)

# print(a+b)

# print(a)
# print(b)

# print(b*3)

# print(b)

# print(dir(tuple))

a=(43,54,'prakash',12.43,'rajesh',76,(21,23,24),43)

print(a.index('rajesh'))

print(a.count(43))