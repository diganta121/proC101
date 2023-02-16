import random

inp=input("press\'y\' to roll dice ")

while inp =='y':
    rval=random.randint(1,6)
    print(rval)

    inp=input("press\'y\' to roll dice \'n\' to exit")
    if inp == 'n':
        break
