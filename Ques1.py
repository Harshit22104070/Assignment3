count=0
word=str(input("Enter the line"))
letter=str(input("Enter the alphabet "))
for i in word:
    if i == letter:
        count=count+1
print(count)