#   Tower of Hanoi

def move(n,source,aux,dist):
    if(n==1):
        print("Move {0} to {1}".format(source,dist))
    else:
        move(n-1,source,dist,aux)
        move(1,source,aux,dist)
        move(n-1,aux,source,dist)


n=int(input('Enter total no. disc : '))
print("\nTotal no. of move : ",2**n-1)
move(n,'A','B','C')
print('...Distination Reached...\n');