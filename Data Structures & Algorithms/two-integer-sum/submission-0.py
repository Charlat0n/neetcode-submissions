class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        answer = [None, None]
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            value = hash_map.get(diff)
            if(value != None and value != i):
                answer[0] = value
                answer[1] = i
                break
        if(answer[0] < answer[1]):
            return answer
        else:
            temp = answer[0]
            answer[0] = answer[1]
            answer[1] = temp
            return answer
