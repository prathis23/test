def outer():
     print("in outer function")
     def inner(num):
       print("in inner function" , 5)

    #  inner()
     return inner
something = outer()
something(5)
