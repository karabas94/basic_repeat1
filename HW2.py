"""
При виконанні дз використовувати Git (робити комміти,
працювати в develop гілці, для кожного завдання окрема feature/<назва_гілки> гілка з develop гілки,
після завершення роботи над завданням - робити merge feature гілки в dev гілку,
після виконання всіх завдань зробити merge develop в master)
"""
"""
1. Користувач вводить три цифри з клавіатури. 
Залежно від вибору користувача програма виводить на екран максимум із трьох, 
мінімум із трьох або середньоарифметичне трьох чисел.
"""


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

# choose MAX, MIN, AVG
choose = int(input("Enter 1, 2 or 3: 1-MAX of three numbers, 2-MIN of three numbers, 3-AVG of three numbers: "))
if choose == 1:
    if first_number < second_number > third_number:
        print(f'The maximum number is {second_number}')
    elif second_number < first_number > third_number:
        print(f'The maximum number is {first_number}')
    else:
        print(f'The maximum number is {third_number}')
elif choose == 2:
    if first_number > second_number < third_number:
        print(f'The minimum number is {second_number}')
    elif second_number > first_number < third_number:
        print(f'The minimum number is {first_number}')
    else:
        print(f'The minimum number is {third_number}')
elif choose == 3:
    avg_number = (first_number + second_number + third_number) / 3
    print(f'The average number is {avg_number}')
else:
    print('Invalid input number. Write 1, 2 or 3 only!')
