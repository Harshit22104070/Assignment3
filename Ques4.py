grade=float(input("Enter grade points"))
x=0
if grade==10:
        x="A+"
elif grade>=9:
        x="A"
elif grade>=8:
        x="B+"
elif grade>=7:
        x="B"
elif grade>=6:
        x="c+"
elif grade>=5:
        x="c"
elif grade>=4:
        x="D"
else:
        x="Very Poor Performance"
print(x)