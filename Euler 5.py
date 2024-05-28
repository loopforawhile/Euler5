            # Question 5 // Soru 5

#  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 2520, 1'den 10'a kadar olan sayılara kalansız bölünebilen en küçük sayıdır.
# 1'den 20'ye kadar tüm sayılara tam olarak bölünebilen en küçük pozitif sayı nedir?



# def check(a):
#     is_true = True
#     for i in range(1,21):
#         if a%i != 0:
#             is_true = False
#     return is_true    

#                         # This is the slowest version in my opnion -_- that'as my solution
# flag_ = True
# x = 21
# while flag_:
#     if check(x) == True:
#         flag_ = False
#         print(x)
#     else:
#         x += 1




                        # This will be faster than mine solution. I found this on youtube and it's kinda shortcut.
                        # I haven't used the reduce functione yet. That's why I didn't think that way.
        
import math
import functools

def gcd(x,y):
    return math.gcd(x,y)

def lcm(x,y):
    return x*y // (gcd(x,y))

liste = range(1,21)

result = functools.reduce(lcm,liste)

print(result)
