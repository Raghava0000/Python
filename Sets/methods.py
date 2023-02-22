
# Set methods:
    # union,intersection.difference,symmetric_difference,issubset,issuperset,isdisjoint..

# print(dir(set))

# Set Methods

# union() - Adding both the set elements and making it as single set(removing duplicates)..

# a={43,12,56,83}

# b={76,87,12,98}

# print(a.union(b))

# print(a|b)

# intersection() -- Common elements between both the sets..

# print(a.intersection(b))
# print(a&b)

# difference() -- 

# {43,56,83} # a-b

# {76,87,98} # b-a

# print(a.difference(b))
# print(a-b)

# print(b-a)

# Symmetric_difference() -- 

# print(a.symmetric_difference(b))

# print(a^b)


# print(a)
# print(b)

# print(a.intersection(b))

# a = a.intersection(b)

# a.intersection_update(b)

# print(a)
# print(b)


# a.difference_update(b)

# print(a)
# print(b)


# a.symmetric_difference_update(b)

# print(a)
# print(b)


# a={43,56,23,65,87,13}

# b={23,13,87}

# # issuperset()

# print(a.issuperset(b))

# print(a.issubset(b))

# # isdisjoint() -- no common elements between both the sets..

# print(a.isdisjoint(b))

# Strings Task Solution:

str1 = "Dont trouble the trouble if you trouble the trouble the trouble troubles you i am not the trouble i am the truth"

# print(str1.replace('trouble','problem',3))

# print(str1[::-1])

# data = str1.split()[::-1]

# new_str = " ".join(data)
# print(new_str)

# new_str_data = new_str.replace('trouble','problem',3)

# print(new_str_data)
# data = new_str_data.split()[::-1]

# print(data)
# new_str = " ".join(data)

# print(new_str)


# List Task Solution

a=[32,'54','python','54','django',65,'15','python','54','devops',32,'python',43,'python']

print(a.index('python'))


input1 = input("enter your word:")
if input1 in a:
    which_occurence = int(input("Enter which occurence:"))
    if a.count(input1) >= which_occurence:
        word_count = 0
        for index,ele in enumerate(a):
            if ele == input1:
                word_count += 1
                if word_count == which_occurence:
                    print(f'{which_occurence}nd occurence of {input1} is at {index} index value. ')
                    break
    else:
        print(f"{input1} is occured {a.count(input1)} no.of time only, please give correct occurence")
else:
    print("element doesnt exist!")