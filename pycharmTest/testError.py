import sys
# while True:
#     try:
#         x = int(input("Please enter a number:"))
#         print(x)
#         break
#     except (RuntimeError, TypeError, NameError):
#         print("Oops! That was no valid number, Try again ")

# try:
#     a=int(1+'2')
#     return a
# except (RuntimeError, TypeError, NameError.ZeroDivisionError):
#     print("ok")
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     print("s=", s)
#     # i = int(s.strip())
#     # print("i=", i)
# except OSError as err:
#     print("OS error is:", str(err))
# else:
#     print("没有错误")
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise



a = 10
b = 0
c = a / b
print(c)
raise ZeroDivisionError