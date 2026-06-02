class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0
        end = len(numbers) - 1

        if len(numbers) == 0:
            return []

        while start < end:
            result = numbers[start] + numbers[end]
            if result == target:
                return [start + 1, end + 1]
            elif result < target:
                start = start + 1
            else:
                end = end - 1      
        

        return []