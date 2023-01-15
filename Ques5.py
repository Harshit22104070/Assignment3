for i in range(10, 0, -1):
    for j in range(11-i):
        print(" ", end="")
    for k in range(i):
        print(chr(65+k),end=" ")
    print()
