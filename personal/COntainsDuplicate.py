import time
class Solution(object):
    def containsDuplicate(self, nums):
     list = {}
     for x in nums:
        if not (x in list):
         list.update({x:1})
        else:
         return True
     return False

    def containsDuplicate2(self, nums):
        return len(nums) != len(set(nums))

j = Solution()
x=[1,2,3,4,5,6,1]
start = time.clock()
print(j.containsDuplicate(x))
dif = time.clock()- start
print(dif)
start = time.clock()
print(j.containsDuplicate2(x))
dif = time.clock()- start
print(dif)