from functools import reduce
num = [4,5,3,6,2,8,9,7]
# even = []
# for i in num:
#     if i % 2 ==0:
#         even.append(i)
# def sum_it(a,b):
#   return n * 2 
even = list(filter(lambda n : n % 2 == 0,num)) 
double = list(map (lambda n: n*2, even))
sum = reduce(lambda a,b : a + b , double)

print(even)
print(double)
print(sum)


