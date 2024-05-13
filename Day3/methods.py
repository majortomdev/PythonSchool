text = "We are going to learn six methods today"
result=text.upper()
print(result)

result2= text[16:22].upper()
print(result2)

result3 = text.split()#or could enter eg: 'o' and it would split it at every o
print(result3)

a = "learning"
b = "Python"
c = "is"
d = "amazing"
e = " ".join([a,b,c,d])
print(e)


word_list = ["Simple","is","better","than","complex."]



print(" ".join(word_list))