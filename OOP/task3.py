# Create a Computation class with a default constructor (no parameters) 
# that can perform several different calculations on whole numbers.
# 1.	Factorial(n) — calculates the factorial of a whole number n.
# 2.	naturalSum(n) — calculates the sum 1 + 2 + 3 + ... + n.
# 3.	testPrime(n) — checks whether n is a prime number or not.
# 4.	testPrims(a, b) — checks whether two numbers are "prime to one another,"
#  meaning the only number that divides both of them evenly is 1 (for example, 4 and 9).
# 5.	tableMult(n) — prints the multiplication table of n. Then build allTablesMult(),
#  which prints every multiplication table from 1 to 9.
# 6.	A static method listDiv(n) — collects every divisor of n into a new list called Ldiv. 
# Then build listDivPrim(n), which collects only the prime divisors of n.

class Computation:
    def __init__(self):
        pass

    def factorial(self,n):
        if n==1 :
           return 1
        return n*self.factorial(n-1) 
    
    def naturalSum (self,n):
        sum = 0
        for i in  range(1,n+1):
            sum +=i
        return sum

    def testPrime(self,n):
        if n<=1:
            return False
        for i in range(2,n):
            if n%i == 0:
                return False
        else:
            return True
    
    def testPrimes(self,a,b):
        gcd = 1
        for i in range(1,min(a,b)+1):
            if a%i ==0 and b%i ==0:
                gcd = i
            
        if gcd ==1:
            return True
        else:return False


    def table(self,n):
        for i in range(1,n+1):
            for j in range(1,11):
                print(f"{i}*{j} = {i*j}")
    

    @staticmethod            
    def lisDiv(n):
        l = []
        for i in range(1,n+1):
            if n%i==0:
                l.append(i)
        return l

comp = Computation()
print(comp.factorial(5))
print(comp.naturalSum(10))
print(comp.testPrime(12))
print(comp.testPrimes(10,12))


comp.table(9)