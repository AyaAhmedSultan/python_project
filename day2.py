#1
# def get_range(length, start):
#
#     return [start + i for i in range(length)]
#
#
# x=int(input("enter x :"))
# y=int(input("enter y :"))
# print(get_range(x,y))

#2
# def fizzbuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "Buzz"
#     else:
#         return str(num)
#
#
# x=int(input("enter x :"))
# print(fizzbuzz(x))

#3
# def reverse_string(input_str):
#     reversed_str = ""
#     for char in input_str:
#         reversed_str = char + reversed_str
#     return reversed_str
#
# str1 = input("enter a string: ")
# print(reverse_string(str1))

#4
# def validate_email(email):
#     if '@' not in email or '.' not in email:
#         return False
#
#     at_pos = email.find('@')
#     dot_pos = email.rfind('.')
#
#     if at_pos > dot_pos:
#         return False
#
#     if email[0] == '@' or email[-1] == '.':
#         return False
#
#     return True
#
#
# def get_user_info():
#     print("Please enter your information:")
#
#     while True:
#         name = input("Your name: ").strip()
#         if (name.isdigit()==0):
#             break
#         print("Please enter a real name")
#
#     while True:
#         email = input("Your email: ").strip()
#         if validate_email(email):
#             break
#         print("Please enter a valid email ")
#
#     print("\nYour details:")
#     print(f"Name: {name}")
#     print(f"Email: {email}")
#
#
# get_user_info()


#5
def find_long(s):
    l = s[0]
    c = s[0]
#abdu lr ahm an
    for i in range(1, len(s)):
        if s[i] >= s[i - 1]:
            c += s[i]
        else:
            current = s[i]

        if len(c) > len(l):
            l = c

    return l

str2= input("enter a string: ")
print(find_long(str2))

#6
# total = 0
# count = 0
#
# print("Enter numbers below. Type 'done' to finish.")
#
# while True:
#     str5 = input("> ")
#
#     if str5.lower() == 'done':
#         break
#
#     try:
#         num = float(str5)
#         total += num
#         count += 1
#     except:
#         print("That's not a number!")
#
# if count > 0:
#     average = total / count
#     print(f"\nTotal: {total}")
#     print(f"Numbers entered: {count}")
#     print(f"Average: {average}")
# else:
#     print("\nYou didn't enter any numbers.")

#7
import random

words = ["aya","ahmed", "sultan"]
s = random.choice(words)
arr = ""
t = 7

print(f"You have {t} tries")

while t > 0:
    w = 0
    for i in s:
        if i in arr:
            print(i, end=" ")
        else:
            print("*", end=" ")
            w = 1

    if w == 0:
        print("You won")
        break

    x = input("enter x :").lower()

    arr += x

    if x not in s:
        t -= 1
        print(f"Wrong! You have {t} tries")

    if t == 0:
        print("\nGame over")


















# arr=["aya","ahmed","sultan"]
# s=arr[1]
# str2=''
# t=7
# l=len(s)
# for i in range(l):
#     str2+='*'
# # print(str2)
# # while t>0:
# x = input("enter x :").lower()
# for index, char in enumerate(str):
#   if char== x:
#     print(index, end=' ')
#       str2[index]=x
#     # print(i)
#     # str2[i]=x
#
#
#
#
#
#     print(x , end=' ')
# else:
#     print('*', end=' ')




#
# import random
#
# arr = ["aya", "ahmed", "sultan"]
# s = random.choice(arr)
# t = 7
# l = len(s)
#
# str2 = ['*'] * l
#
# print(f"You have {t} tries")
#
# while t > 0:
#     x = input("Enter a letter: ").lower()
#     found = False
#
#     for index, char in enumerate(s):
#         if char == x:
#             str2[index] = x
#             found = True
#
#     print("".join(str2))
#
#     if found:
#         print(f"Good! '{x}' is in the word.")
#     else:
#         t -= 1
#         print(f"Wrong you have {t} tries")
#
#     if ''.join(str2) == s:
#         print(f"\nYou won!")
#         break
#
# if t == 0:
#     print(f"\nGame over!")
























