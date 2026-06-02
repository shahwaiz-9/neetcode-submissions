class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        result = []


        nums.sort()

        terminator = len(nums) - 2


        for i in range (0, terminator):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                res = nums[i] + nums[start] + nums[end]
                if res == 0:
                    # Check Duplicate 
                    trip = [nums[i], nums[start], nums[end]]
                    if trip not in result:
                        result.append(trip)
                    start = start + 1

                elif res < 0:
                    start = start + 1
                else:
                    end = end - 1 

        return result

        