text_block = input("Enter a block of text")
letters = input("Enter 3 letters")
first = letters[0].lower()
second = letters[1].lower()
third = letters[2].lower()
#Increase your quantitative reasoning skills through a deeper
#understanding of probability and statistics

count1 = text_block.lower().count(first)
count2 = text_block.lower().count(second)
count3 = text_block.lower().count(third)


word_list = text_block.split()

first_letter = text_block[0]
last_letter = text_block[-1]
word_list.reverse()

print(str(count1)+"  "+str(count2)+"  "+str(count3))
print(len(word_list))


print()
print("First letter:  "+str(first_letter)+".    Last letter:   "+str(last_letter))

print()
print(" ".join(word_list))

python = "python" in text_block
#print("np of times python is in the text: "+str(word_list.count(python)))

print(f"Python is in the text:  {python}")