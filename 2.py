#armstrong no

def armstrongNumber (ob, n):
        # code here 
        sum=0
        t=n
        
        p=len(str(n))
        
        while(n!=0):
            x=n%10
            sum=sum+pow(x,p)
            n=n//10
        
        if sum==t:
            return "Yes"
        else:
            return "No"
    
#gcd code
def gcd(a,b):
     
    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
 
    # base case
    if (a == b):
        return a
 
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)
 #OR
    def gcd(a,b):
     
    # Everything divides 0
        if (b == 0):
             return a
        return gcd(b, a%b)

#LCM

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
     # Function to return LCM of two numbers
def lcm(a,b):
    return (a / gcd(a,b))* b



# Function to find factorial of given number
def factorial(n):
     
    if n == 0:
        return 1
    
    return n * factorial(n-1)

#function to find prime num
    if num > 1:
        
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
  
            # Bcz factors will be available only between 2 to n/2 eg, 12  factor-->2,3,4,6   till 12/2only
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
  
    else:
        print(num, "is not a prime number")

#Second more better efficient way to find factorial
    from math import sqrt
    # n is the number to be check whether it is prime or not
    n = 1
  
    # no lets check from 2 to sqrt(n)
    # if we found any facto then we can print as not a prime number
  
    # this flag maintains status whether the n is prime or not
    prime_flag = 0
  
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            print("true")
        else:
            print("false")
    else:
        print("false")
