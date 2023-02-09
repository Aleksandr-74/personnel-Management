# import time
# import asyncio
from Management_app.models import Role

# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print("func1 - ВСЕ")
#     print("********")
#
# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print("fun2-ВСЕ")
#     print("**********")
#
#
#
# async def main():
#     task1=asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
#
#
# print(time.strftime("%X"))
# asyncio.run(main())
# print(time.strftime("%X"))



# fib=0
# fib1=1
# fn= (fn-1)+(fn+2)


# def fac(n):
#     factr = 1
#     counter = 1
#     while counter <= n:
#         factr = factr*counter
#         counter += 1
#     return print(f"результ: {factr}")
#
# # print(time.strftime("%X"))
#
# async def fac1(x):
#     factr = 1
#     counter = 1
#     while counter <= x:
#         factr = factr * counter
#         counter += 1
#     return print(f"результ: {factr}")
#
#
# async def fac2(x):
#     factr = 1
#     counter = 1
#     while counter <= x:
#         factr = factr * counter
#         counter += 1
#     return print(f"результ: {factr}")
#
#
# async def main():
#     task1 = asyncio.create_task(fac1(5))
#     task2 = asyncio.create_task(fac2(6))
#
#     await task1
#     await task2
#
#
# fac(4)
# print(time.strftime("%X"))
# asyncio.run(main())
# print(time.strftime("%X"))



# s = Role.objects.create(role="ОТК")
# print(s)