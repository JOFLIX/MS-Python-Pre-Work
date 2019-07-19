# def get_age():
#     print("How old are you ")
#     age = int(input())
#     return age
#
# print(get_age())

# This error is difficult to understand. Let us create a more understandable error message

# def get_age():
#     print("How old are you ")
#     try:
#         age = int(input())
#         return age
#     except ValueError:
#         return "That was not a valid input"
list_b = [1,2,3,4,5,6]
list_b.reverse()
print(list_b)
