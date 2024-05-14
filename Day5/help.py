dic = {'key1':150, 'key2':575}

print(dic)
a =dic.popitem()
print(a)
print(dic)

a= "#][_%$£Hello Dolly$%".lstrip("#[]%$£_")
print(a)#strips out blank space to left or else charcters specified

fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

fruits.insert(3,"orange")
print(fruits)#insert into list obejct 2nd arg at index 1st arg



print()

phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}
print(phone_brands.isdisjoint(tv_brands))