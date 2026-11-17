class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        class Node:
            def __init__(self, value):
                self.value = value
                self.next = None

        def create_node(value):
            return Node(value)

        buckets = [None] * 10
        flag = 0

        for i in range(len(nums)):
            index = nums[i] % len(buckets)
            node = create_node(nums[i])
            if buckets[index] == None:
                buckets[index] = node
            elif buckets[index] != None:
                walker = buckets[index]
                while walker.next != None:
                    if walker.value == nums[i]:
                        flag = 1
                    walker = walker.next
                if walker.value == nums[i]:
                    flag = 1
                walker.next = node

        if flag == 1:
            return True
        else:
            return False