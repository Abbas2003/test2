def isPrimeNo(val):
    i = 2
    while(i < val):
        if(val%i == 0):
            return False
        else:
            i += 1
    if(i==val):
        return True


abc = 'None'