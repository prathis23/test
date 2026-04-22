#func_arg.py

# def add(num1 = 0, num2 = 0): #default arguments
#     return num1 + num2

#multi arugment in fun

# def add(num1 ,*num2): #variable length arguments
#     sum = num1
#     for n in num2:
#       sum += n
#     return sum 

# result = add (4,5,6,7)
# print(result)

#multi arugment
# def person(name , **key ):
#     print("name :" , name)
#     for k,v in key.items() :
#      print(k , " : " , v)
# person(name = "nova" , age = 24 , loc = "chennai" , colour = "white")
 
# a = 10    #global variable
# def somthing():

#  globals()["a"] = 20
# a = 15   #local variable

# print("inside:" , a)
# somthing()
# print("outside :" ,a)

  #higher order function
# def square (num):
#    return  num * num
# def cube (num):
#    return num * num * num
# def operate(nums , operation):
#    for i in nums:
#       result = operation(i)
#       print(result) 
# nums= [5,6,7]
# result = operate(nums, square)



