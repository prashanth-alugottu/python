

def prime_numer():
    a=3
    for n in range(2,a):
        if a%2==0 or a%n==0:
            print("Not Prime")
        else:
            print("Prime number")
            
def fibonacci():
    a,b=0,1
    res=[0]
    for _ in range(5):
        a,b=b,a+b
        res.append(a)  
    print(res)
    
def factorial():
    n=4
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

    
def main():
    # prime_numer()
    # fibonacci()
    # factorial()
    print(is_anagram("listen","netsil"))
    
    
if __name__ == "__main__":
    main()
    