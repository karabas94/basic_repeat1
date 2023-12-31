print("Please enter ONLY number!!!")

"""
1. Користувач вводить три цифри з клавіатури. Необхідно знайти суму чисел, добуток чисел.
Результат обчислень вивести на екран.
"""
first_number = int(input("Please enter first number: "))
second_number = int(input("Please enter second number: "))
third_number = int(input("Please enter third number: "))
sum_numbers = first_number + second_number + third_number
multiple_numbers = first_number * second_number * third_number
print(f'The sum of numbers: {sum_numbers}')
print(f'The multiplication of numbers: {multiple_numbers}')

print('\n')
"""
2. Напишіть програму, яка обчислює площу ромба. Користувач із клавіатури вводить довжину двох його діагоналей.
Площа ромба дорівнює половині добутку його діагоналей: S = (AC · BD)/2.
"""

first_number = int(input("Please enter first length: "))
second_number = int(input("Please enter second length: "))
square_rhombus = (first_number * second_number) / 2
print(f'The square of rhombus: {square_rhombus}')

print('\n')
"""
3. Користувач вводить з клавіатури число, що складається із чотирьох цифр. Потрібно знайти добуток цифр.
Наприклад, якщо з клавіатури введено 1324 тоді результат буде - 1*3*2*4 = 24.
"""
number = int(input("Please enter four digit number: "))
first_number = number // 1000
second_number = number // 100 % 10
third_number = number % 100 // 10
fourth_number = number % 10
multiple_numbers = first_number * second_number * third_number * fourth_number
print(f'The multiplication of four digit number {multiple_numbers}')
