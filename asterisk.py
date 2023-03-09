print("Asterisk Pyramid A")
print()

for i in range(1,11):
    for j in range(0,i):
        print("*", end=" ")
    print()

print("Asterisk Pyramid B")
print()

for i in range(10,0, -1):
    for j in range(0,i):
        print("*", end=" ")
    print()

print("Asterisk Pyramid C")
print()

for i in range(1,11):
    for j in range(1,i):
        print(" ", end=" ")
    for k in range(0,10-j):
        print("*", end=" ")
    print()

print("Asterisk Pyramid D")
print()

for i in range(1,11):
    for j in range(0,10-i):
        print(" ", end=" ")
    for k in range(0,i):
        print("*", end=" ")
    print()