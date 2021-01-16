#def giveMeEven(list): 
#     new_list = []
#     for number in list:
#         if number % 2 == 0:
#         new_list.append(number)
#     return new_list

# print(giveMeEven([1,2,3,4])

def giveMeEven(list):
    newList = []
    for number in list:
        if number % 2 == 0:
            newList.append(number)
    return newList

print(giveMeEven([1, 2, 4, 5, 7, 89, 48]))
print(giveMeEven([1, 12, 5, 7, 89, 48]))
