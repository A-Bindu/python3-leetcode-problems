class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #nums=[8,1,2,2,3]
        l=[]
        for i in range(len(nums)):
          count=0
          for j in range(len(nums)):
             if i!=j and nums[j] < nums[i]:
                count+=1
          l.append(count)
        return l