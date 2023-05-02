def func(*args,**kwargs):

 n=[]

 for i in range(len(args)):
     def calc_largest(arr):
         second_largest = arr[0]
         largest_val = arr[0]
         for i in range(len(arr)):
             if arr[i] > largest_val:
                 largest_val = arr[i]

         for i in range(len(arr)):
             if arr[i] > second_largest and arr[i] != largest_val:
                 second_largest = arr[i]

         return second_largest

     print(calc_largest([20, 30, 40, 25, 10]))
 return n

print(func(1,3,"k","d",a=3,b=4))