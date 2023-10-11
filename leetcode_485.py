def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_count = result = 0
    for i in nums:
        if (i==1):
            max_count = max_count+1
        else:
            result = max_count if max_count > result else result
            max_count = 0
    result = max(max_count, result)
    return result

nums =[1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))