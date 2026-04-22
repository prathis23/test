def square (num):
    return num * num
def cube (num):
    return num *num* num
def operate(nums,operation):
    for i in nums:
     result = operation(i)
    print(result)

nums= [9,8,15]
operate(nums, cube)

