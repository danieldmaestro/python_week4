for i in range(1,11):
    # loop for first triangle
    # loop for star
    for a in range(0,i):
        print("*", end=" ")
    # loop for space
    for b in range(0,10-i):
        print(" ", end=" ")
    print(" ", end="") 
    
    # loop for second triangle
    # loop for star
    for c in range(0,11-i):
        print("*", end=" ")
    # loop for space
    for d in range(0,i-1):
        print(" ", end=" ")
    print(" ", end="")

    # loop for thrid triangle
    for e in range(0,i-1):
        print(" ", end=" ")
    for f in range(0, 11-i):
        print("*", end=" ")
    print(" ", end="")
    
    # loop for fourth triangle
    for g in range(0,10-i):
        print(" ", end=" ")
    for h in range(0,i):
        print("*", end=" ")
    print()
    