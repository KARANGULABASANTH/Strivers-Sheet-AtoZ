
   # Spiral matrix
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        self.matrix=matrix
        top=0
        bottom=len(self.matrix)-1
        left=0
        right=len(self.matrix[0])-1
        li=[]
        while (top<=bottom and left<=right):
            for i in range (left,right+1):
                li.append(self.matrix[top][i])
            top+=1
            for j in range (top,bottom+1):
                li.append(self.matrix[j][right])
            right-=1
            if top<=bottom:
                for k in reversed(range (left,right+1)):
                    li.append(self.matrix[bottom][k])
                bottom-=1
            if left<=right:
                for l in reversed(range(top,bottom+1)):
                    li.append(self.matrix[l][left])
                left+=1
        return li



      #    Majority element 

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        self.nums=nums
        count=0
        # key=self.nums[0]
        for num in self.nums:
            if count==0:
                key=num
            if num==key:
                count+=1
            else:
                count-=1
        return key


  #   Leader elemnet in array

n=int(input("Enter a number"))
nums=list(map(int,input("Enter list").split()))
li=[]
for i in range (0,len(nums)-1):
    if nums[i]>max(nums[i+1:len(nums)]):
        li.append(nums[i])
li.append(nums[len(nums)-1])
print(li)


 # SET MATRIX ZERO

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m=matrix
        t=[]
        p=[]
        for i in range (0,len(m)):
            for j in range (0,len(m[0])):
                if m[i][j]==0:
                    t.append(i)
                    p.append(j)
        for i in range (0,len(m)):
            for j in range (0,len(m[0])):
                if i in t:
                    m[i][j]=0
                if j in p:
                    m[i][j]=0
        return m
