# print target sum of two numbers in a list
lis = [2,7,11,15]
nums = len(lis)
for i in range (nums):
    for j in range (i+1,nums):
        if lis[i] + lis[j] == 9:
            print (i,j)
            
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.   
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
print(twoSum([2,7,11,15], 9))

# Given num is palindrome or not without using string
def pali(num):
    a = 0
    c = num
    while num > 0:
        r = num % 10
        num = num // 10
        a = (10 *a) + r
        
    if a == c:
        print("true")
    else:
        print("false")
        
pali(1234321)
    
# Given num is palindrome or not using string

my_string = "malayalam"
if my_string == my_string[::-1]:
    print("true")
else:
    print('false')