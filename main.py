import os
# exercise 1 : Given two integer numbers by user return their product only if the product is equal to or lower than 1000, else return their sum.
def sum_if():
    number1 = int(input("give first number"))
    number2 = int(input("give second number"))
    product = number1 * number2
    if product <= 1000:
        print(product)
    else:
        print(number1 + number2)


# exercise 2 : Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
def sum_iter():
    sum_of_2_numbers = 0
    for i in range(10):
        if i == 0:
            print(f"Current number {i}, previous number {i}, sum = {sum_of_2_numbers}")
        else:
            sum_of_2_numbers = i + (i - 1)
            print(f"Current number {i}, previous number {i - 1}, sum = {sum_of_2_numbers}")


# exercise 3 : Write a program to accept a string from the user and display characters that are present at an even index number.
def even_index_string():
    user_string = input("write your string")
    for i in range(len(user_string)):
        if i % 2 == 0:
            print(user_string[i])


# exercise 4 : Write a program to remove characters from a string starting from zero up to n and return a new string.
def remove_char():
    user_string = input("write your string")
    number_of_letters_to_remove = int(input("write number of letters to remove, must be lower than string length"))
    if number_of_letters_to_remove > len(user_string):
        print("number of letters to remove exceed string length")
    else:
        x = user_string[number_of_letters_to_remove:]
        print(x)


# exercise 5 : Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
def are_the_same():
    list_to_check = [1, 2, 3, 5]
    if list_to_check[0] == list_to_check[-1]:
        return True
    else:
        return False


# exercise 6 : Iterate the given list of numbers and print only those numbers which are divisible by 5
def divisible_by_5():
    list_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in list_to_check:
        if i % 5 == 0:
            print(i)


# exercise 7 : Write a program to find how many times substring appears in the given string.
def how_many_time():
    user_string = input("write sentence in which you want to search for word")
    word = input("write a word you are looking for")
    print(user_string.count(word))


# exercise 8 : Print the pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
def print_pattern():
    for i in range(1, 6):
        print(f"{i} " * i)


# exercise 9 : Write a program to check if the given number is a palindrome number.
def if_palindrome_number():
    number_to_check = int(input("write integer to  check if it is palindrome"))
    original_number = number_to_check
    reversed_number = 0
    while original_number > 0:
        rest = original_number % 10
        reversed_number = (reversed_number * 10) + rest
        original_number = (original_number // 10)
    if number_to_check == reversed_number:
        print("number is a palindrome")
    else:
        print("not a palindrome")


# exercise 10 : Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
def join_lists():
    first_list = [1, 2, 3, 4, 5, 6, 7]
    second_list = [10, 11, 12, 13, 14, 15]
    mix = []
    for i in first_list:
        if i % 2 == 1:
            mix.append(i)
    for i in second_list:
        if i % 2 == 0:
            mix.append(i)
    print(mix)


# exercise 11 : Write a Program to extract each digit from an integer in the reverse order.
def reverse_digit():
    user_integer = int(input("write your integer to extract digits in reverse order"))
    extract_int = user_integer
    while extract_int > 0:
        digit = extract_int % 10
        extract_int = extract_int // 10
        print(digit, end=" ")


#exercise 12 : Calculate income tax for the given income by adhering to the below rules
#               amount  %
#First          $10,000	0
#Next           $10,000	10
#The remaining	        20
def tax_calculator():
    user_money = int(input("write how much money to calculate tax from"))
    tax = 0
    if user_money <= 0:
        print("please enter valid amount of money")
    else:
        if user_money <= 10000:
            return tax
        elif 10000 < user_money <= 20000:
            tax = (user_money-10000) * 0.1
            return tax
        else:
            tax = (user_money-20000) * 0.2 + 1000
            return tax


#exercise 13: Print multiplication table form 1 to 10
def multiplication_table():
    for i in range(1,11):
        for j in range(1,11):
            print(i*j, end=" ")
        print()


#exercise 14: Print downward Half-Pyramid Pattern with Star
def downward_pyramid():
    for i in range(1,6):
        print("*" * (6-i))


#exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent():
    base = int(input("write base of exponent"))
    exp = int(input("write positive exponent integer"))
    value = 1
    if exp <= 0:
        print("write integer greater then 0")
    else:
        for i in range(exp):
            value = value*base
        return value


#exercise 16: Display three string “Name”, “Is”, “James” as “Name**Is**James”
def display_name():
    print('Name', 'Is', 'James',sep="**")


#exercise 17: Accept a list of 5 float numbers as an input from the user
def input_list():
    input_numbers = input("Enter numbers separated by space")
    list_of_numbers = input_numbers.split()
    for i in range(len(list_of_numbers)):
        list_of_numbers[i] = float(list_of_numbers[i])


#exercise 18: Write all content of a given file into a new file but skipping given line number
def skip_line():
    given_file = open('test.txt', 'r')
    new_file = open('new_file.txt', 'a')
    which_line_to_skip = int(input("write line that you want to skip during rewriting"))
    iterator = 0
    for line in given_file:
        if iterator != which_line_to_skip-1:
            new_file.write(line)
        iterator += 1
    given_file.close()
    new_file.close()


#exercise 19: Accept any string from one input() call separated with space and print them
def multi_input():
    given_names = input("write list of names separated with space")
    listed_names = given_names.split(sep=" ")
    for i in range(len(listed_names)):
        print(f"name {i+1} is {listed_names[i]} ")


#exercise 20: Print variables with f""
def f_format():
    money = 102
    quantity = 3
    price = 50
    print(f"I have {money} dollars so I can buy {quantity} for {price}")


#exercise 21: Check if file is empty
def is_empty():
    file_path = 'test.txt'
    if os.stat(file_path).st_size == 0:
        print("Empty file")
    else:
        print("File  not empty")


#exercise 22: Read given line number from the following file
def read_given_live():
    f = open('test.txt', 'r')
    chosen_line = int(input("write line that you want to read"))
    iterator = 0
    for line in f:
        if iterator == chosen_line-1:
            print(line)
        iterator += 1
    f.close()


#exercise 23: Calculate the sum of all numbers from 1 to a given number
def sum_of_numbers():
    number = int(input("write your number"))
    sum_of_numbers = 0
    for i in range(1, number+1):
        sum_of_numbers += i
    print(sum_of_numbers)


#exercise 24: Write a program to print multiplication table of a given number
def multiplication_of_number():
    number_to_multiply = int(input("write number to multiply"))
    for i in range(1,11):
        print(i*number_to_multiply)


#exercise 25: Display numbers from a list using loop. Write a program to display only those numbers from a list that satisfy the following conditions:
#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop
def display_number_from_list():
    number_list=[12, 75, 150, 180, 145, 525, 50]
    for number in number_list:
        if number > 500:
            break
        elif number > 150:
            continue
        elif number % 5 == 0:
            print(number)


#exercise 26: Write a program to use for loop to print the following reverse number pattern
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1
def disp_pattern():
    pattern = [5,4,3,2,1]
    for j in range(len(pattern)):
        for i in pattern:
            print(i, end=" ")
        pattern.pop(0)
        print()


#exercise 27: Print list in reverse order using a loop
def reverse_list():
    list1 = [10, 20, 30, 40, 50]
    for i in range(1, len(list1)+1):
        print(list1[-i])


#exercise 28: Display numbers from -10 to -1 using for loop
def disp_negative_numbers():
    for i in range(-10, 0, 1):
        print(i)


#exercise 29: Use else block to display a message “Done” after successful execution of for loop
def done_after_loop():
    for i in range(5):
        print(i)
    else:
        print("DONE")


#exercise 30: Write a program to display all prime numbers within a range
def prime_numbers():
    start = int(input("write where to start looking for prime numbers"))
    end = int(input("Write when to stop"))
    for number in range(start, end+1):
        if number > 1:
            for i in range(2, number):
                if number%i == 0:
                    break
            else:
                print(number)


#exercise 31: Display Fibonacci series up to 10 terms
def fibonacci():
    fibo = [0,1]
    for i in range(2,10):
        fibo.append(fibo[i-1]+fibo[i-2])
    print("Fibonacci sequence:")
    for i in fibo:
        print(i,end=" ")


#exercise 32: Find the factorial of a given number
def factorial():
    number = int(input("Write number to factor"))
    result = 1
    if number < 0:
        print("type positive number")
    else:
        while number > 0:
            result = result * number
            number -= 1
        print(result)


#exercise 33: Reverse a given integer number
def rev_number():
    number = int(input("Write number to reverse"))
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number*10) + digit
        number = number // 10
    print(reversed_number)


#exercise 34: Use a loop to display elements from a given list present at odd index positions
def odd_index_list():
    my_list = [10,20,30,40,50,60,70]
    for i in range(len(my_list)):
        if i % 2 != 0:
            print(my_list[i])


#exercise 35: Calculate the cube of all numbers from 1 to a given number
def cube_number():
    number = int(input("Write number to calculate cubes of all number from 1 to number"))
    for i in range(1, number+1):
        print(f"Current number {i} and cube equal to {i*i*i}")


#exercise 36: Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
def sum_of_series():
    series_number = int(input("write base number of our series (1-9)"))
    n = int(input("how many digits will last number has"))
    sum_of_numb = 0
    for i in range(1, n+1):
        number = int(f"{series_number}" * i)
        sum_of_numb += number
    print(sum_of_numb)


#exercise 37: Print the following pattern. Write a program to print the following start pattern using the for loop
def print_pyramide_pattern():
    for i in range(1, 6):
        print(f"*"*i)
    for j in range(4, 0, -1):
        print(f"*"*j)


#exercise 38: Write a program to create function func1() to accept a variable length of arguments and print their value.
# Note: Create a function in such a way that we can pass any number of arguments to this function,
# and the function should process them and display each argument’s value.
def func1(*args):
    print("Printing values:")
    for i in range(len(args)):
        print(args[i])


#execise 39: Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction.
#Also, it must return both addition and subtraction in a single return call.
def calculation(*args):
    addi = args[0] + args[1]
    sub = args[1] - args[0]
    return addi, sub


#exercise 40: Write a program to create a function show_employee() using the following conditions.
#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name, salary=0):
    if salary == 0:
        salary = 9000
    print(f"Name: {name} salary: {salary}")


#exercise 41: Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters, a and b
#Create an inner function inside an outer function that will calculate the addition of a and b
#At last, an outer function will add 5 into addition and return it
def addition(a, b):
    def add(c, d):
        return c+d
    return add(a, b) + 5


#exercise 42: Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def recursive_sum(number):
    if number == 0:
        return 0
    else:
        return number + recursive_sum(number-1)


#exercise 43: Below is the function display_student(name, age). Assign a new name show_student(name, age) to it and call it using the new name.
def display_student(name, age):
    print(name, age)

show_student = display_student


#exercise 44: Generate a Python list of all the even numbers between 4 to 30
def list_of_even():
    lis_of_evens = [i for i in range(4,30) if i%2==0]
    print(lis_of_evens)


#exercise 45: Find the largest item from a given list
def sort_list():
    x = [4,6,8,24,12,2]
    print(max(x))
    

sort_list()

