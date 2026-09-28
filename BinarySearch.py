# Search insert position 


# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         for i in range (0,len(nums)):
#             if (nums[i]==target):
#                 return i
#             if (nums[i]>target):
#                 return i
#         return len(nums)


#   Row with max number of ones

# class Solution:
#     def rowWithMax1s(self, mat):
#        self.mat=mat 
#        li=[]
#        for i in range (0,len(self.mat[0])):
#         count=0
#         for j in range (0,len(self.mat)):
#             if self.mat[i][j]==1:
#                 count+=1
#         li.append(count)
#         m=max(li)
#         if m!=0:
#             return li.index(m)
#         else:
#             return -1



#     FIND PEAK ELEMNET


# class Solution:
#     def findPeakElement(self, nums: list[int]) -> int:
#         self.nums=nums
#         m=max(self.nums)
#         return self.nums.index(m)



#    Kth element of 2 sorted arrays

# class Solution:
#     def kthElement(self, a, b, k):
#         li=a+b
#         li.sort()
#         return li[k-1]

