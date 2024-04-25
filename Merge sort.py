z=int(input())
def merge(left,mid,right,nums):
    i1=left
    i2=mid+1
    temp=[]
    while i1<=mid and i2<=right:
        if nums[i1]>nums[i2]:
            temp.append(nums[i2])
            i2+=1
        else:
            temp.append(nums[i1])
            i1+=1
    while i1<=mid:
        temp.append(nums[i1])
        i1+=1
    while i2<=right:
        temp.append(nums[i2])
        i2+=1
    curr=0
    for pos in range(left,right+1):
        nums[pos] = temp[curr]
        curr += 1 


def divide(left,right,nums):
    if left>=right:
        return 
    
    mid=(left+right)//2
    divide(left,mid,nums)
    divide(mid+1,right,nums)
    merge(left,mid,right,nums)

nums=list(map(int,input().split()))
divide(0, len(nums) - 1, nums)
print(*nums)
