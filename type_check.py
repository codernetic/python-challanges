# def only_ints(a, b):
#     if a != True and b != True:
#         try:
#             int(a)
#             int(b)
#
#             return True
#         except:
#             return False
#     else:
#         return False

def only_ints(a, b):
    a = type(a) is int
    b = type(b) is int

    if a and b:
        return True
    else:
        return False


print(only_ints(1, 2))

