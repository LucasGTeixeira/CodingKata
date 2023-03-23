'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

def runningSum(nums: list[int]) -> list[int]:
        sumarray = []
        for i in range(1, len(nums)+1):
            sumarray.append(sum(nums[:i]))
        return sumarray

data = [1,2,3,4]
print(runningSum(data))