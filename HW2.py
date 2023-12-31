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

print('\n')
"""
2. Користувач вводить з клавіатури кількість метрів. 
Залежно від вибору користувача програма переводить метри милі, дюйми або ярди.
"""

meters = float(input('Enter your meters: '))

# choose miles, inches, yards
converted_meters = int(input("Please enter 1, 2 or 3: 1-miles, 2-inches or 3-yards: "))
if converted_meters == 1:
    miles = meters / 1609
    print(f'Your miles is {miles}')
elif converted_meters == 2:
    inches = meters * 39.37
    print(f'Your inches is {inches}')
elif converted_meters == 3:
    yards = meters * 1.094
    print(f'Your yards is {yards}')
else:
    print('Invalid input number. Write 1, 2 or 3 only!')
