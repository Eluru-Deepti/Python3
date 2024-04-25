x=int(input())
def findpi(nums,left,right):
    pivot=nums[right]
    pos=left
    for i in range(left,right):
        if nums[i]<pivot:
            temp=nums[pos]
            nums[pos]=nums[i]
            nums[i]=temp
            pos+=1
    temp=nums[right]
    nums[right]=nums[pos]
    nums[pos]=temp
    return pos




def quick(nums,left,right):
    if left>=right:
        
        return

    pi=findpi(nums,left,right)
    quick(nums,left,pi-1)
    quick(nums,pi+1,right)


nums=list(map(int,input().split()))
n=len(nums)
quick(nums,0,n-1)
print(*nums)
