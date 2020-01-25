name='PRACHI'

for k in range(0,len(name)):
    word = input("\nEnter one word in your name")
   

    if word=='A':
        A=[0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]
        for i in range(0,len(A)):
            if A[i]==1:
                print("* ",end="")
            else:
                print("  ",end="")
            if i==4 or i==9 or i==14 or i==19:
                print()
                
    elif word=='D':
        C=[1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0]
        for i in range(0,len(D)):
            if D[i]==1:
                print("* ",end="")
            else:
                print("  ",end="")
            if i==4 or i==9 or i==14 or i==19:
                print()

    elif word=='I':
        I=[1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1]
        for i in range(0,len(I)):
            if I[i]==1:
                print("* ",end="")
            else:
                print("  ",end="")
            if i==4 or i==9 or i==14 or i==19:
                print()
    
    elif word=='T':
        T=[1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]
        for i in range(0,len(T)):
            if T[i]==1:
                print("* ",end="")
            else:
                print("  ",end="")
            if i==4 or i==9 or i==14 or i==19:
                print()
                
    else :
        print("Sorry you have entered wrong character")