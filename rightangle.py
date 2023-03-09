for a in range(1,21):
    for b in range(1,21): 
        for c in range(1,21):
            if (b**2) + (c**2) == (a**2):
                print(b,c,a, "is a pythagorean triple")