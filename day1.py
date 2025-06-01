#1
# def counts():
#     str = input("enter your string: ")
#     chars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     count = 0
#
#     for char in str:
#         if char in chars:
#             count += 1
#
#     print(f"count = : {count}")
#
#
# counts()


#2
# def sortArray():
#     arr = []
#     print("enter 5 numbers:")
#
#     i = 0
#     while i < 5:
#         num = int(input("enter number "))
#         arr.append(num)
#         i += 1
#
#     ascending = sorted(arr)
#     descending = sorted(arr, reverse=True)
#
#     print(f"Ascending: {ascending}")
#     print(f"Descending: {descending}")


# sortArray()


#3
# def countIt():
#     str = input("enter a string: ")
#     count = str.count('it!')
#     print(f"The string 'it!' appears {count} times.")

# countIt()


#4
# def removeVowels():
#     str = input("enter a word: ")
#     chars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     result = ""
#
#     for char in str:
#         if char not in chars:
#             result += char
#
#     print(f"Word : {result}")
#
#
# removeVowels()

#5
# def findI(str):
#     print(f"string '{str}':")
#     f = False
#     for index, char in enumerate(str):
#         if char.lower() == 'i':
#             print(f"index : {index}")
#             f = True
#
#     if not f:
#         print("nothing found")
#
#
#
# str1 = input("enter a string: ")
# findI(str1)

#6
# def gen_table(n):
#     table = []
#     for i in range(1, n + 1):
#         l = []
#         for j in range(1, i + 1):
#             l.append(i * j)
#         table.append(l)
#     return table
#
#
# num = int(input("enter number "))
# result = gen_table(num)
# print(f"table of {num}: {result}")


#7
# def pyramid (n):
#     for i in range(1, n + 1):
#         for j in range(1, i+ 1):
#             print('*', end=' ')
#
#         print('\n')
#
#
#
# num = int(input("enter number "))
# pyramid (num)


def pyramid(n):
    for i in range(1, n + 1):
        print('  ' * (n - i), end='')
        for j in range(1, i + 1):
            print('*', end=' ')
        print()

num = int(input("Enter number: "))
pyramid(num)

