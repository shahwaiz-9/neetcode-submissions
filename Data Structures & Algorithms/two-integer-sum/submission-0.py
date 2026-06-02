class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = dict()

        for i in range(len(nums)):
            finder = target - nums[i]
            print(target , nums[i],finder)

            if finder in map:
                solution = [map[finder], i]
                return solution

            else:
                map[nums[i]] = i
                print(map)

               
        
        