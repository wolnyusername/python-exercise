import os
import datetime
from datetime import datetime, timedelta

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


# exercise 12 : Calculate income tax for the given income by adhering to the below rules
#               amount  %
# First          $10,000	0
# Next           $10,000	10
# The remaining	        20
def tax_calculator():
    user_money = int(input("write how much money to calculate tax from"))
    tax = 0
    if user_money <= 0:
        print("please enter valid amount of money")
    else:
        if user_money <= 10000:
            return tax
        elif 10000 < user_money <= 20000:
            tax = (user_money - 10000) * 0.1
            return tax
        else:
            tax = (user_money - 20000) * 0.2 + 1000
            return tax


# exercise 13: Print multiplication table form 1 to 10
def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print()


# exercise 14: Print downward Half-Pyramid Pattern with Star
def downward_pyramid():
    for i in range(1, 6):
        print("*" * (6 - i))


# exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent():
    base = int(input("write base of exponent"))
    exp = int(input("write positive exponent integer"))
    value = 1
    if exp <= 0:
        print("write integer greater then 0")
    else:
        for i in range(exp):
            value = value * base
        return value


# exercise 16: Display three string “Name”, “Is”, “James” as “Name**Is**James”
def display_name():
    print('Name', 'Is', 'James', sep="**")


# exercise 17: Accept a list of 5 float numbers as an input from the user
def input_list():
    input_numbers = input("Enter numbers separated by space")
    list_of_numbers = input_numbers.split()
    for i in range(len(list_of_numbers)):
        list_of_numbers[i] = float(list_of_numbers[i])


# exercise 18: Write all content of a given file into a new file but skipping given line number
def skip_line():
    given_file = open('test.txt', 'r')
    new_file = open('new_file.txt', 'a')
    which_line_to_skip = int(input("write line that you want to skip during rewriting"))
    iterator = 0
    for line in given_file:
        if iterator != which_line_to_skip - 1:
            new_file.write(line)
        iterator += 1
    given_file.close()
    new_file.close()


# exercise 19: Accept any string from one input() call separated with space and print them
def multi_input():
    given_names = input("write list of names separated with space")
    listed_names = given_names.split(sep=" ")
    for i in range(len(listed_names)):
        print(f"name {i + 1} is {listed_names[i]} ")


# exercise 20: Print variables with f""
def f_format():
    money = 102
    quantity = 3
    price = 50
    print(f"I have {money} dollars so I can buy {quantity} for {price}")


# exercise 21: Check if file is empty
def is_empty():
    file_path = 'test.txt'
    if os.stat(file_path).st_size == 0:
        print("Empty file")
    else:
        print("File  not empty")


# exercise 22: Read given line number from the following file
def read_given_live():
    f = open('test.txt', 'r')
    chosen_line = int(input("write line that you want to read"))
    iterator = 0
    for line in f:
        if iterator == chosen_line - 1:
            print(line)
        iterator += 1
    f.close()


# exercise 23: Calculate the sum of all numbers from 1 to a given number
def sum_of_numbers():
    number = int(input("write your number"))
    sum_of_numbers = 0
    for i in range(1, number + 1):
        sum_of_numbers += i
    print(sum_of_numbers)


# exercise 24: Write a program to print multiplication table of a given number
def multiplication_of_number():
    number_to_multiply = int(input("write number to multiply"))
    for i in range(1, 11):
        print(i * number_to_multiply)


# exercise 25: Display numbers from a list using loop. Write a program to display only those numbers from a list that satisfy the following conditions:
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
def display_number_from_list():
    number_list = [12, 75, 150, 180, 145, 525, 50]
    for number in number_list:
        if number > 500:
            break
        elif number > 150:
            continue
        elif number % 5 == 0:
            print(number)


# exercise 26: Write a program to use for loop to print the following reverse number pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
def disp_pattern():
    pattern = [5, 4, 3, 2, 1]
    for j in range(len(pattern)):
        for i in pattern:
            print(i, end=" ")
        pattern.pop(0)
        print()


# exercise 27: Print list in reverse order using a loop
def reverse_list():
    list1 = [10, 20, 30, 40, 50]
    for i in range(1, len(list1) + 1):
        print(list1[-i])


# exercise 28: Display numbers from -10 to -1 using for loop
def disp_negative_numbers():
    for i in range(-10, 0, 1):
        print(i)


# exercise 29: Use else block to display a message “Done” after successful execution of for loop
def done_after_loop():
    for i in range(5):
        print(i)
    else:
        print("DONE")


# exercise 30: Write a program to display all prime numbers within a range
def prime_numbers():
    start = int(input("write where to start looking for prime numbers"))
    end = int(input("Write when to stop"))
    for number in range(start, end + 1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(number)


# exercise 31: Display Fibonacci series up to 10 terms
def fibonacci():
    fibo = [0, 1]
    for i in range(2, 10):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    print("Fibonacci sequence:")
    for i in fibo:
        print(i, end=" ")


# exercise 32: Find the factorial of a given number
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


# exercise 33: Reverse a given integer number
def rev_number():
    number = int(input("Write number to reverse"))
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number = number // 10
    print(reversed_number)


# exercise 34: Use a loop to display elements from a given list present at odd index positions
def odd_index_list():
    my_list = [10, 20, 30, 40, 50, 60, 70]
    for i in range(len(my_list)):
        if i % 2 != 0:
            print(my_list[i])


# exercise 35: Calculate the cube of all numbers from 1 to a given number
def cube_number():
    number = int(input("Write number to calculate cubes of all number from 1 to number"))
    for i in range(1, number + 1):
        print(f"Current number {i} and cube equal to {i * i * i}")


# exercise 36: Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
def sum_of_series():
    series_number = int(input("write base number of our series (1-9)"))
    n = int(input("how many digits will last number has"))
    sum_of_numb = 0
    for i in range(1, n + 1):
        number = int(f"{series_number}" * i)
        sum_of_numb += number
    print(sum_of_numb)


# exercise 37: Print the following pattern. Write a program to print the following start pattern using the for loop
def print_pyramide_pattern():
    for i in range(1, 6):
        print(f"*" * i)
    for j in range(4, 0, -1):
        print(f"*" * j)


# exercise 38: Write a program to create function func1() to accept a variable length of arguments and print their value.
# Note: Create a function in such a way that we can pass any number of arguments to this function,
# and the function should process them and display each argument’s value.
def func1(*args):
    print("Printing values:")
    for i in range(len(args)):
        print(args[i])


# execise 39: Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.
def calculation(*args):
    addi = args[0] + args[1]
    sub = args[1] - args[0]
    return addi, sub


# exercise 40: Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name, salary=0):
    if salary == 0:
        salary = 9000
    print(f"Name: {name} salary: {salary}")


# exercise 41: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
def addition(a, b):
    def add(c, d):
        return c + d

    return add(a, b) + 5


# exercise 42: Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def recursive_sum(number):
    if number == 0:
        return 0
    else:
        return number + recursive_sum(number - 1)


# exercise 43: Below is the function display_student(name, age). Assign a new name show_student(name, age) to it and call it using the new name.
def display_student(name, age):
    print(name, age)


show_student = display_student


# exercise 44: Generate a Python list of all the even numbers between 4 to 30
def list_of_even():
    lis_of_evens = [i for i in range(4, 30) if i % 2 == 0]
    print(lis_of_evens)


# exercise 45: Find the largest item from a given list
def max_list():
    x = [4, 6, 8, 24, 12, 2]
    print(max(x))


# exercise 46: Write a program to create a new string made of an input string’s first, middle, and last character.
def first_mid_last_letter():
    word = input("Write word")
    word_to_print = ""
    for i in range(len(word)):
        if i == 0:
            word_to_print += word[i]
        elif i == (len(word) // 2):
            word_to_print += word[i]
        elif i == (len(word) - 1):
            word_to_print += word[i]
        else:
            continue
    print(word_to_print)


# exercise 47:Write a program to create a new string made of the middle three characters of an input string.
def mid_3_letters():
    word = input("Write your word")
    mid = len(word) // 2
    word_to_print = f"{word[mid - 1]}{word[mid]}{word[mid + 1]}"
    print(word_to_print)


# exercise 48:Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
def create_new_string():
    s1 = input("write first string")
    s2 = input("write second string")
    s3 = ""
    mid = len(s1) // 2
    s3 = f"{s1[:mid]}{s2}{s1[mid:]}"
    print(s3)


# exercise 49: Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
def exercise_49():
    s1 = input("write first word")
    s2 = input("write second word")
    mid1 = len(s1) // 2
    mid2 = len(s2) // 2
    s3 = f"{s1[0]}{s2[0]}{s1[mid1]}{s2[mid2]}{s1[len(s1) - 1]}{s2[len(s2) - 1]}"
    print(s3)


# exercise 50: Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
def sort_with_lower_first():
    word = input("write your word")
    lower = ""
    caps = ""
    for i in word:
        if i.islower():
            lower += i
        else:
            caps += i
    print(f"{lower}{caps}")


# exercise 51: Count all letters, digits, and special symbols from a given string
def count_letters_digits_symbols():
    special_symbols = ["@", "#", "!", "$", "%", "^", "&", "*", "(", ")"]
    word = input("write your word")
    letters = 0
    digits = 0
    symbols = 0
    for i in word:
        if i.isdigit():
            digits += 1
        elif i.isalpha():
            letters += 1
        elif i in special_symbols:
            symbols += 1
    print(f"letters {letters} digits {digits} symbols {symbols}")


# exercise 52: Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2,
# Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
def mix_string():
    s1 = input("write first word")
    s2 = input("write second word")
    s3 = ""
    if len(s1) > len(s2):
        for i in range(len(s2)):
            if i == 0:
                s3 += f"{s1[0]}{s2[(len(s2) - 1)]}"
            else:
                s3 += f"{s1[i]}{s2[-i - 1]}"
        s3 += s1[len(s2):]
    elif len(s2) > len(s1):
        for i in range(len(s1)):
            if i == 0:
                s3 += f"{s1[0]}{s2[(len(s2) - 1)]}"
            else:
                s3 += f"{s1[i]}{s2[-i - 1]}"
        s3 += s2[:(len(s2) - len(s1))]
    else:
        for i in range(len(s2)):
            if i == 0:
                s3 += f"{s1[0]}{s2[(len(s2) - 1)]}"
            else:
                s3 += f"{s1[i]}{s2[-i - 1]}"
    print(s3)


# exercise 53: Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.
def balanced():
    s1 = input("write characters to check")
    s2 = input("write word to be checked if balanced")
    for i in s1:
        if i not in s2:
            return False
    else:
        return True


# exercise 54: Find all occurrences of a substring in a given string by ignoring the case
def all_occurrences():
    s1 = input("write word you want to count")
    s2 = input("write sentence where you want to count given word")
    s2.lower()
    print(s2.count(s1.lower()))


# exercise 55: Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
def sum_avarage_string():
    s1 = input("write your word")
    digits = []
    for i in s1:
        if i.isdigit():
            digits.append(int(i))
    suma = sum(digits)
    avr = suma / len(digits)
    return suma, avr


# exercise 56: Write a program to count occurrences of all characters within a string
def count_of_char_in_string():
    s1 = input("write word")
    count = dict()
    for i in s1:
        char_count = {i: s1.count(i)}
        count.update(char_count)
    print(count)


# exercise 57: reverse given string
def reverse_given_string():
    s1 = input("write string to reverse")
    rev = ""
    for i in range(len(s1)):
        rev += s1[len(s1)-i-1]
    print(rev)


# exercise 58: Find the last position of a given substring
def position_of_given_substring():
    s1 = input("write sentence where you want to find string")
    s2 = input("write string you are looking for")
    return s1.rfind(s2)


# exercise 59: Write a program to split a given string on hyphens and display each substring.
def split_on_hyphens():
    s1 = input("write string to split")
    for i in s1.split(sep="-"):
        print(i)


# exercise 60: Remove empty strings from a list of strings
def remove_empty_string():
    l1 = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    final_list = list(filter(None, l1))
    print(final_list)


# exercise 61: Slice list into 3 equal chunks and reverse each chunk
def slice_list_in_3():
    l1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    first_point = len(l1)//3
    second_point = len(l1)*2//3
    chunk1 = l1[:first_point]
    chunk2 = l1[first_point:second_point]
    chunk3 = l1[second_point:]
    chunk1.reverse()
    chunk2.reverse()
    chunk3.reverse()
    print(chunk1,chunk2,chunk3)


# exercise 62: Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
def count_of_list_element():
    l1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    count = dict()
    for i in l1:
        if i in l1:
            element_count = {i: l1.count(i)}
            count.update(element_count)
    print(count)


# exercise 63: Create a Python set such that it shows the element from both lists in a pair
def lists_to_list():
    l1 = [2, 3, 4, 5, 6, 7, 8]
    l2 = [4, 9, 16, 25, 36, 49, 64]
    l3 = []
    for i in range(len(l1)):
        l3.append((l1[i], l2[i]))
    answer = set(l3)
    print(answer)


# exercise 64: Find the intersection (common) of two sets and remove those elements from the first set
def remove_common_elements():
    first_set = {23, 42, 65, 57, 78, 83, 29}
    second_set = {57, 83, 29, 67, 73, 43, 48}
    common_values = first_set & second_set
    for i in common_values:
        first_set.remove(i)
    print(common_values)
    print(first_set)


# exercise 65: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
def subset_of_set():
    first_set = {27, 43, 34, 93, 22, 53, 48, 55, 47}
    second_set = {34, 93, 22, 27, 43, 53, 48}
    if first_set.issubset(second_set):
        print("1 set jest w 2 secie")
        first_set.clear()
    elif second_set.issubset(first_set):
        print("2 set jest w 1 secie")
        second_set.clear()
    print(first_set)
    print(second_set)


# exercise 66: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
def iter_in_dict():
    roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
    sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
    roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
    print(roll_number)


# exercise 67: Get all values from the dictionary and add them to a list but don’t add duplicates
def dict_to_list_no_duplicates():
    speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
    l1 = []
    for i in speed.values():
        if i not in l1:
            l1.append(i)
    print(l1)


# exercise 68: Remove duplicates from a list and create a tuple and find the minimum and maximum number
def remove_duplicate():
    sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
    new_list = []
    for i in sample_list:
        if i not in new_list:
            new_list.append(i)
    print(max(new_list))
    print(min(new_list))
    wynik = tuple(new_list)
    print(type(wynik))


# exercise 69: Convert two lists into a dictionary
def convert_list_to_dict():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    dictionary = dict()
    if len(keys) == len(values):
        for i in range(len(keys)):
            single_element = {keys[i]: values[i]}
            dictionary.update(single_element)
    print(dictionary)


# exercise 70: Merge two Python dictionaries into one
def merge_two_dict():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    me = {**dict1, **dict2}
    print(me)


# exercise 71: Print the value of key ‘history’ from the below dict
def print_nested_dict():
    sampledict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    print(sampledict["class"]["student"]["marks"]["history"])


# exercise 72: Initialize dictionary with given values
def create_dict_from_given():
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    dictionary = {}
    for i in employees:
        dictionary.update({i:defaults})
    print(dictionary)


# exercise 73: Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
def extract_keys():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}

    # Keys to extract
    keys = ["name", "salary"]
    dictionary = {}
    for i in keys:
        dictionary.update({i: sample_dict[i]})
    print(dictionary)


# exercise 74: Delete a list of keys from a dictionary
def del_keys_from_dict():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    # Keys to remove
    keys = ["name", "salary"]
    for i in keys:
        del sample_dict[i]
    print(sample_dict)

# exercise 75: Check if a value exists in a dictionary
def check_value_in_dict():
    value_to_check = int(input("write your number to check"))
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    flag = False
    if value_to_check in sample_dict.values():
        print(f"{value_to_check} is in dict")
    else:
        print(f"{value_to_check} is not in dict")


# exercise 76: Write a program to rename a key in the following dictionary.
def rename_key():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    key_to_rename = input("which key you want to rename?")
    new_key_name = input("give new key's name")
    if key_to_rename in sample_dict.keys():
        sample_dict.update({new_key_name: sample_dict[key_to_rename]})
        del sample_dict[key_to_rename]
    print(sample_dict)


# exercise 77: Get the key of a minimum value from the following dictionary
def min_value_from_dict():
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }
    print(min(sample_dict))


# exercise 78: Change value of a key in a nested dictionary
def change_in_nested_dict():
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }
    for i in sample_dict.keys():
        print(i)
    emp_number = int(input("write number of employee where you want to change value"))
    emp_to_change = dict(sample_dict[f"emp{emp_number}"])
    del sample_dict[f"emp{emp_number}"]
    print(emp_to_change)
    value_to_change = input("which value would you like to change")
    changed_value = input("write new value")
    emp_to_change[value_to_change] = changed_value
    sample_dict.update({f"emp{emp_number}":emp_to_change})
    print(sample_dict)


# exercise 79: Given a Python list, Write a program to add all its elements into a given set.
def add_to_set():
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]
    sample_set.update(sample_list)
    print(sample_set)


#exercise 80: Return a new set of identical items from two sets
def identical_from_both_sets():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set3 = set1.intersection(set2)
    print(set3)


# exercise 81: Write a Python program to return a new set with unique items from both sets by removing duplicates.
def unique_items_in_sets():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set3 = set1.union(set2)
    print(set3)



# exercise 82: Reverse the tuple
def rev_tuple():
    tuple1 = (10, 20, 30, 40, 50)
    reversed_tuple = []
    for i in range(len(tuple1)-1,-1,-1):
        reversed_tuple.append(tuple1[i])
    reversed_tuple = tuple(reversed_tuple)
    print(reversed_tuple)


# exercise 83: The given tuple is a nested tuple. write a Python program to print the value 20.
def value_from_nested_tuple():
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
    print(tuple1[1][1])


# exercise 84: Write a program to unpack the following tuple into 4 variables and display each variable.
def unpack_tuple():
    tuple1 = (10, 20, 30, 40)
    a,b,c,d = tuple1


# exercise 85: Swap two tuples in Python
def swap_tuples():
    tuple1 = (11, 22)
    tuple2 = (99, 88)
    temp_tuple = tuple1
    tuple1 = tuple2
    tuple2 = temp_tuple
    print(tuple1)
    print(tuple2)


# exercise 86: Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
def change_value_in_nested_tuple():
    tuple1 = (11, [22, 33], 44, 55)
    tuple1[1][0] = 222
    print(tuple1)


# exercise 87: Counts the number of occurrences of item 50 from a tuple
def count_in_tuple():
    tuple1 = (50, 10, 60, 70, 50)
    print(tuple1.count(50))


# exercise 88: Check if all items in the tuple are the same
def check_if_all_the_same():
    tuple1 = (45, 45, 45, 45)
    flag = True
    for i in tuple1:
        if tuple1[0] != i:
            return False
    else:
        return flag


# exercise 89: Print current date and time in Python
def print_date_and_time():
    print(datetime.datetime.now())


# exercise 90: Convert string into a datetime object
def convert_string_to_date():
    date_string = "Feb 25 2020 4:20PM"
    print(datetime.strptime(date_string, "%b %d %Y %I:%M%p"))


# exercise 91: Subtract a week (7 days)  from a given date in Python
def sub_week_from_date():
    given_date = datetime(2020, 2, 25)
    delta = timedelta(days=7)
    print(given_date-delta)


# exercise 92: Print a date in a the following format Day_name  Day_number  Month_name  Year
def print_date_in_format():
    given_date = datetime(2020, 2, 25)
    print(given_date.strftime("%A %d %B %Y"))


# exercise 93: Find the day of the week of a given date
def find_day_of_week():
    given_date = datetime(2020, 7, 26)
    print(given_date.strftime("%A"))


# exercise 94: Add a week (7 days) and 12 hours to a given date
def add_week_to_date():
    given_date = datetime(2020, 3, 22, 10, 0, 0)
    delta = timedelta(days=7,hours=12)
    print(given_date+delta)


# exercise 95: Convert the following datetime into a string
def convert_date_to_string():
    given_date = datetime(2020, 2, 25)
    print(given_date.strftime("%Y-%m-%d %X"))


# exercise 96: Calculate number of days between two given dates
def calculate_days():
    date_1 = datetime(2020, 2, 25)
    date_2 = datetime(2020, 9, 17)
    print(date_2-date_1)


# exercise 97: Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# exercise 98: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    pass