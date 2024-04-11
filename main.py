from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    print(f'Input: nums = {nums}, target = {target}')
    
    tmp = []
    for i in nums:
        if i <= target:
            tmp.append(i)
    
    for i in range(len(tmp)):
        for j in range(i+1,len(tmp)):
            if(nums[i]+nums[j] == target):
                res: List[int] = [i,j,nums[i],nums[j]]
                return res
    return 0

if '__main__':
    nums = [2,7,11,15]
    target = 9
    res:List[int] = twoSum(nums,target)
    
    print(f"Output: {res[:2]}")
    print(f"Explanation: Because nums[{res[2]}] + nums[{res[3]}] == {target}, we return {res[:2]}")
    
    nums = [3,2,4]
    target = 6
    res:List[int] = twoSum(nums,target)
    
    print(f"Output: {res[:2]}")
    print(f"Explanation: Because nums[{res[2]}] + nums[{res[3]}] == {target}, we return {res[:2]}")
    
    nums = [3,3]
    target = 6
    res:List[int] = twoSum(nums,target)
    
    print(f"Output: {res[:2]}")
    print(f"Explanation: Because nums[{res[2]}] + nums[{res[3]}] == {target}, we return {res[:2]}")
    
    