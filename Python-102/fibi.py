#  num_input = int(input('Give number: '))

#  while num_input > 0 and num_input < 1000:
#      num_input = num_input + num_input
#      print(num_input)

# num_input = int(input('Give number: '))
# num_1 = 0
# num_2 = 1
# while num_input > 0 and num_output < 1000:
#     num_output = num_input + num_output
#     print(num_output)

def fib_num_seq():
    fib_num_1 = 0
    fib_num_2 = 1
    next_fib_num = 0
    fib_list = []
    for next_fib_num in fib_list:
        next_fib_num[fib_list] = fib_num_1 + fib_num_2
        print(fib_list)
    user_input = int(input('How many numbers in the Fibonacci Sequence? '))
    if user_input == 0:
        print('The list isn\'t possible')
    elif user_input == 1:
        print(f'{fib_num_2}')
    elif user_input >= 2:
        while len(fib_list) <= 100:
            print(fib_list)
print(fib_num_seq())