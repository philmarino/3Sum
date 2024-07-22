def threeSum(nums):
    answer = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                    if not isDup([nums[i], nums[j], nums[k]], answer):
                        answer.append([nums[i], nums[j], nums[k]])

    return answer

def isDup(oneArray, bigArray):
    thisArray = oneArray
    thisArray.sort()
    for anArray in bigArray:
        anArray.sort()
        if thisArray[0] == anArray[0] and thisArray[1] == anArray[1] and thisArray[2] == anArray[2]:
            return True
        
    return False

# Example 1:
# Input: 
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: 
nums = [0,1,1]
print(threeSum(nums))
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: 
nums = [0,0,0]
print(threeSum(nums))
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
