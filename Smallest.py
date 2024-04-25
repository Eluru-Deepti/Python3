def findsmallestelement(numbers):
    result=1000000
    n=len(numbers)
    for index in range(n):
        if numbers[index]<result:
           result=numbers[index]
    return result
numbers=[12,3,4,65,43,21,65,1,2,3]
result=findsmallestelement(numbers) 
print("smallest element is",result)
