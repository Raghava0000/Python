# print(dir(dict))

# dict methods={ 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'}

# adding methods:=
    # 1)update

# removal methods:=
# 1)pop 2)popitem 3)clear

# accesssing:=
# 1)get 2)key 3)value 4)items
# copy, fromkeys, setdefault


# a={"name":"raghava","mobile":"9638527410","email":"raghava@gmail.com"}
# b={"name":"shabbu","mobile":"7418523215","address":"hyd"}
# print(a)
# print(b)

# update:-it will add the all key-values pairs into 1st to 2nd dict
# a={"name":"raghava","mobile":"9638527410","email":"raghava@gmail.com"}
# b={"name":"shabbu","mobile":"7418523215","address":"hyd"}
# a.update(b) 
# print(a)
# print(b)

# pop:-it will remove the key-value pair from the dict
# a={"name":"raghava","mobile":"9638527410","email":"raghava@gmail.com"}
# b={"name":"shabbu","mobile":"7418523215","address":"hyd"}

# a.pop('address')
# print(a)


# a.item:-it will remove the last key-value pair from the dict
# a={"name":"raghava","mobile":"9638527410","email":"raghava@gmail.com"}
# b={"name":"shabbu","mobile":"7418523215","address":"hyd"}
# a.popitem()
# print(a)


# clear:-remove the all key-values pair and make it as empty dict
# a={"name":"raghava","mobile":"9638527410","email":"raghava@gmail.com"}
# b={"name":"shabbu","mobile":"7418523215","address":"hyd"}
# a.clear()
# print(a)



# keys:-will return the keys inside the dict
# a={"name":"raghava","mobile":"9638527410","email":"raghava@gmail.com"}
# print(a.keys())


# values:-it will return all the values inside the dict
# a={"name":"raghava","mobile":"9638527410","email":"raghava@gmail.com"}
# print(a.values())


# items:-it will return the combination of key-values inside the dict
# a={"name":"raghava","mobile":"9638527410","email":"raghava@gmail.com"}
# b={"name":"shabbu","mobile":"7418523215","address":"hyd"}
# print(a.items())


# copy:-
# a={"name":"raghava","mobile":"9638527410","email":"raghava@gmail.com"}
# b={"name":"shabbu","mobile":"7418523215","address":"hyd"}

# b=a.copy()
# print(a)
# print(b)

# a['mobile']="852963214"
# print(a)
# print(b)

# print(a['mobile'])
# print(a.get('mobile'))


# from-keys():-its for creating a dict using list of elements where each element will taken as in the dict
# a=['name','email','address','mobile']
# print({}.fromkeys(a,'dummy'))

# b={

# }
# for ele in a:
#     b[ele]=None
#     print(b)


# setdefault():-its for setting a default key-value pair inside the dict
# a={"name":"raghava","mobile":"9638527410","email":"raghava@gmail.com"}

# a.setdefault('company',"TCS")
# print(a)

# a['company']="wipro"
# print(a)




