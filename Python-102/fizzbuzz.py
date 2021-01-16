# def fizz_buzz():
#     num_inp = int(input('What\'s your number? '))
#     if (num_inp % 3 == 0):
#         print('fizz')
#     elif (num_inp % 5 == 0):
#         print('buzz')
#     elif (num_inp % 3 and num_inp % 5 == 0):
#         print('fizzbuzz')
#     else (num_inp % 3 or 5 != 0):
#         print('Your number neither fizzes nor buzzes, so check yourself!!!')
# print(fizz_buzz())

def fizz_buzz():
    num_inp = int(input('What\'s your number? '))
    while True:
        if (num_inp % 3 == 0):
            print('fizz')
            break
        elif (num_inp % 5 == 0):
            print('buzz')
            break
        elif (num_inp % 3 and num_inp % 5 == 0):
            print('fizzbuzz')
            break
    else:
        print('Your number neither fizzes nor buzzes, so check yourself!!!')
        break
print(fizz_buzz())