def fact(num):
  if num == 1:
   return 1
  return num * fact(num-1)
result = fact(5)
print(result)


def fun(num): 
     return num * num
fun = lambda num : num * num
result = fun(5)
print(result)


add = lambda a,b: a + b
result3= add(4,5)
print(result3)