my_set = set({1,2,3,4,5})
print(type(my_set))
print(my_set)
print(7 in my_set)


s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)

print(type(s1))
print(s3)

s3.add(7)
print(s3)
s3.remove(3)
print(s3)