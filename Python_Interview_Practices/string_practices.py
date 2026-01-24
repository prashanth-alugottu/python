
# ===================================================================================
# 11️⃣ Check Palindrome (String)
# Problem:Check if a string is a palindrome (case-insensitive).
# Example:"Madam" → True

def polindrome():
    name="madams"
    new_name=""
   
    for i,_ in enumerate(name):
        new_name+=name[len(name)-1-i]
        
    if name in new_name:
        print("Its a polindrome")
    else:
        print("Its NOT a polindrome")
        
    print("=====> One line ans See here once : ",name.lower() == name[::-1].lower())
        
# ===================================================================================
# 12️⃣ Sum of Digits
# Problem:Given an integer, return the sum of its digits.
# Example:123 → 6

def sum_int():
    n = 123
    sum=0
    while n>0:
        sum += n%10
        n//=10
    print("Sum is : ",sum)


# ===================================================================================

# 13️⃣ Find Minimum and Maximum
# Problem:Return both min and max from a list without using min() or max().
# Example:[3, 1, 5] → (1, 5)

def min_max(nums):
    min=max=nums[0]
    
    for num in nums[1:]:
        if num<min:
            min=num
        elif num>max:
            max=num
    print(f"MIN : {min} === MAX : {max}")
            

# ===================================================================================
    # 4️⃣ Count Vowels
# Problem:Count the number of vowels in a string.
# Example:"hello" → 2    

def count_vowels():
    text="helloeeee"
    vowels="aeiou"
    count=0
    
    for ch in text.lower():
        if ch in vowels:
            count+=1
            
    print(count)
            

# ===================================================================================
# 5️⃣ Merge Two Lists Alternately
# Problem:Merge two lists by alternating elements.
# Example:[1,2] , [3,4] → [1,3,2,4]
 
def merge_array():
    a=[1,2,7,8]
    b=[3,4]
    result = []
    for i in range(max(len(a), len(b))):
        if i < len(a):
            result.append(a[i])
        if i < len(b):
            result.append(b[i])
    print(result)
    
    # # 2
    # new_res=[]
    # for i in range(min(len(a),len(b))):
    #     new_res.append(a[i])
    #     new_res.append(b[i])
    # print("====>> NEW RES : ",new_res)

# ===================================================================================
# 6️⃣ Find Missing Number
# Problem:Given numbers from 1 to n with one missing, find the missing number.
# Example:[1,2,4,5] → 3

def missing_num():
    nums=[1,2,4,5]
    n=len(nums)+1
    expeted=n*(n+1)//2
    actual=sum(nums)
    res=expeted-actual
    print(res)
    
# ===================================================================================
# 7️⃣ Count Character Frequency
# Problem:Return frequency of each character in a string.
# Example:"aab" → {'a':2,'b':1}

def count_cha():
    text="aab"
    freq={}
    for ch in text:
        freq[ch]=freq.get(ch,0)+1
        
    print(freq)
    
# ===================================================================================
# 8️⃣ Remove All Occurrences
# Problem:Remove all occurrences of a given element from a list.
# Example:[1,2,2,3], remove 2 → [1,3]

def remove_occurence():
    a=[1,2,2,3]
    occ=2
    res=[]
    for i in a:
        if i!=occ:
            res.append(i)
    
    print(res)

# ===================================================================================
# 9️⃣ Find Common Elements
# Problem:Find common elements between two lists.
# Example:[1,2,3], [2,3,4] → [2,3]

def common_elemets():
    a=[1,2,3,5,6,5,4,6,7]
    b=[2,3,4,5,7]
    seen =set()
    res=[]
    for i in range(max(len(a),len(b))):
        if a[i] in b and i not in seen:
            res.append(a[i])
            seen.add(a[i])
    print(res)
            

# ===================================================================================
# 20️⃣ Longest Word in a Sentence
# Problem:Return the longest word in a sentence.
# Example:"I love Python programming" → programming

def longest_word():
    l_res_word=0
    final_word=""
    text="I love Python programming"
    for word in text.lower().split():
        l_word=len(word)
        if l_word>l_res_word:
            l_res_word=l_word
            final_word=word
    print(final_word)
    
    #Easy way
    print("==========>>> ",min(text.split(),key=len))
    print("==========>>> ",max(text.split(),key=len))
# ===================================================================================

            



# ===================================================================================

def main():
    # polindrome()
    # sum_int() 
    # min_max([1,3,4,9,5,5,5,9.1])
    # count_vowels()
    # merge_array()
    # missing_num()
    # count_cha()
    # remove_occurence()
    # common_elemets()
    longest_word()
    
if __name__=="__main__":
    main()
    
