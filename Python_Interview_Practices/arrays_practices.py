# ====================================================================================
# 1. This code maintains a running sum and computes the average at each index as 
# running_sum / (i + 1) in O(n) time without recomputing prefix sums.
def avg_values(nums):
    # nums = [1,2,3,1,2,3]
    index = 1
    num_sum = 0
    for i,num in enumerate(nums):
        # print(i)
        num_sum+=num
        print(num_sum/(i+index))
    
# ====================================================================================

# 2. Problem:
# Given a list of numbers, return a list where each element is the sum up to that index.

def sum_num(nums):
    num_sum = 0
    for i,num in enumerate(nums):
        num_sum+=num
        print(num_sum)

        
# ====================================================================================
# 3. Problem:
# Count how many positive numbers are in the list. 
 

def positive_nums(nums):
    count = 0
    # for num in nums:
    #     if num%2==0:
    #         count+=1
    
    print(sum(1 for num in nums if num%2==0))
    
# ====================================================================================
# 4. Problem:
# Reverse a list without using reverse() or slicing.

def reverse_list(nums):
    result = []
    length = len(nums)
    for i,_ in enumerate(nums):
        result.append(nums[length-i-1])
    print(result)
    
def rever2_list(nums):
    left , right = 0, len(nums)-1
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1
        
    print("dddd ", nums)
        

# ====================================================================================
# 5️⃣ Prefix Maximum
# Problem:Return a list where each element is the maximum value seen so far.
# Example:[1, 3, 2, 5] → [1, 3, 3, 5]

def max_value(nums):
    current_max = 0
    result=[]
    for num in nums:
        current_max = max(current_max,num)
        result.append(current_max)            
            
            
    print("Result. : ",result)

# ====================================================================================
# 6️⃣ Remove Duplicates (Preserve Order)
# Problem:Remove duplicates but keep the original order.
# Example:[1, 2, 1, 3, 2] → [1, 2, 3]

def remove_duplicates(nums):
    result=[]
    for num in nums:
        if num not in result:
            result.append(num)
    print(result)
            
# ====================================================================================
# 7️⃣ Find Second Largest Number
# Problem:Find the second largest number in a list.
# Example:[10, 5, 8, 20] → 10

# def second_largest(nums):
#     first = second = 0
#     for num in nums:
#         print("NUM : ",num)
#         if num > first:
#             second = first
#             first = num
#         elif first > num > second:
#             second = num
#     print(second)

def second_largest(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print(nums[-2])

# ====================================================================================
# 8️⃣ Running Difference
# Problem:Return a list where each element is the difference between current and previous element.
# Example:[5, 10, 7] → [0, 5, -3]

def current_pre_diff(nums):
    prev = 0
    result=[]
    for num in nums:
        value=num-prev
        result.append(value)
        prev=num
    
    print(result)            

# ====================================================================================            
            
# 9️⃣ Word Frequency
# Problem:Given a string, return a dictionary of word counts (case-insensitive).
# Example:"Hello hello world" → {'hello': 2, 'world': 1}

# from collections import Counter  
# import re
# def word_freq(sentence):
#     words = re.findall(r"[a-zA-Z]+",sentence)
#     count = Counter(words)
#     print(count)
    
def word_freq(sentence):
    freq={}
    for word in sentence.lower().split():
        # print(word)    
        freq[word]=freq.get(word,0)+1 
    print(freq)
# ====================================================================================
#🔟 First Non-Repeating Element
# Problem:Find the first element that does not repeat.
# Example:[1, 2, 2, 3, 3] → 1

def non_repeating(nums):
    freq={}
    for num in nums:
        freq[num] = freq.get(num,0)+1
        
    print(freq)
    
    for num in nums:
        if freq[num] ==1:
            print(num)
         

# ====================================================================================



def main():
    for i in range(3):
        print(i)
    # print("================= 1. Problem Start ==================")  
    # nums = [1,2,3,1,2,3]
    # avg_values(nums)
    # print("================= 1. Problem End ==================") 
    
    
    # print("================= 2. Problem Start ==================")  
    # test = [1,2,3,3,3]
    # sum_num(test)
    # print("================= 2. Problem End ==================")
    
    
    # print("================= 3. Problem Start ==================")  
    # test3 = [1,2,3,3,2]
    # positive_nums(test3)
    # print("================= 3. Problem End ==================")
    
    
    # print("================= 4. Problem Start ==================")  
    # test4 = [1,2,3,4]
    # # reverse_list(test4)
    # rever2_list(test4)
    # print("================= 4. Problem End ==================")
    
    
    # print("================= 4. Problem Start ==================")  
    # test5 = [1,2,13,4,1,76,1,2]
    # # reverse_list(test4)
    # max_value(test5)
    # print("================= 4. Problem End ==================")
    
    # print("================= 6. Problem Start ==================")  
    # test6 = [1,2,2,2]
    # # reverse_list(test4)
    # remove_duplicates(test6)
    # print("================= 6. Problem End ==================")
    
    # print("================= 7. Problem Start ==================")  
    # test7 = [10,5]
    # # reverse_list(test4)
    # second_largest(test7)
    # print("================= 7. Problem End ==================")
    
    # print("================= 8. Problem Start ==================")  
    # test7 = [10,5,3,3]
    # # reverse_list(test4)
    # current_pre_diff(test7)
    # print("================= 8. Problem End ==================")
    
    # print("================= 9. Problem Start ==================")  
    # test9 = "World Hello Hello World"
    # # reverse_list(test4)
    # word_freq(test9)
    # print("================= 9. Problem End ==================")
    
    print("================= 10. Problem Start ==================")  
    test10 = [1,2,3,2,1,5,4,5,10]
    # reverse_list(test4)
    non_repeating(test10)
    print("================= 10. Problem End ==================")
    
    
    
    
if __name__ =="__main__":
    main()
    
    
    
    
    
