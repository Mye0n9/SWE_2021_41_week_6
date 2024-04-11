from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    print(f'Input: nums = {nums}, target = {target}')
    
    tmp = []
    for i in nums:
        if i <= target:
            tmp.append(i)
    
    for i in range(len(tmp)):
        for j in range(i,len(tmp)):
            if(nums[i]+nums[j] == target):
                res: List[int] = [i,j]
                print(f"Output: {res}")
                print(f"Explanation: Because nums[{i}] + nums[{j}] == {target}, we return {res}")
                return 0
    return 0

if '__main__':
    twoSum([2,7,11,15],9)