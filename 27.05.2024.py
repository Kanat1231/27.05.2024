# set1 = {1,2,3,4,5}
# b = set(1,2,3,4)
#
#
# a = (1,2,3)
# b = tuple(1,2,3,4)
#
#
# a = {"name":"Kanat"}
# print(type(a))
# if type(a) == dict:
#     print("true")
# else:
#     print("false")
#
# a = 4
# while a < 5:
#     print("hello world")
#     a+=1
#
# a = 1
# while True:
#     print("Hi")
#     a += 1
#     if a > 3:
#         break
#

# a = [(1,2), (7,8), (12, 21), 1]
# type1 = 0
# for i in a:
#     if type(i) == tuple:
#         type1 +=1
# print(type1)

a = [(1,2), (7,8), (12, 21), 1, 2]
type1 = 0
index = 0
while True:
    if index >= len(a):
        break
    if type(a[index]) == tuple:
        type1+=1
    index += 1
print(type1)