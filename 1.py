def closestno(n,m):
    q=n/m
    n1=q*m#first closest
    if((n * m) > 0) :#check for positive no.,Second closest
        n2 = (m * (q + 1))
    else :
        n2 = (m * (q - 1))
     
    if (abs(n - n1) < abs(n - n2)) :
        return n1
     
    
    return n2
     
