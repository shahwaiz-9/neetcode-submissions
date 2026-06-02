class Solution:



    def create_map(self, nums: List[int]) -> dict:
        map = dict()
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1

        print(map)    

        return map    


        
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = self.create_map(nums)

        for i in range(len(nums)):
            if map[nums[i]] > 1:
                return True

        return False        


        