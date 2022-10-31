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
    exponent = int(input("write positive exponent integer"))
    value = 1
    if exponent <= 0:
        print("write integer greater then 0")
    else:
        for i in range(exponent):
            value = value*base
        return value


#exercise : Display three string “Name”, “Is”, “James” as “Name**Is**James”
def display_name():
    print('Name', 'Is', 'James',sep="**")
