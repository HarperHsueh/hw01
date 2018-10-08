for m in range(1,10):
    for n in range(1,10):
        if m>n:
            print (end='       ')
        else:
            print ("{}*{}={:<2}".format(m,n,m*n),end=' ')
    print()
