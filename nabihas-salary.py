# Salary Manager project
categories = ['Savings', 'Rent', 'Electricity']
categories_amount = []
categories_percentage = []

start = input('Do you want to start? (Yes/No) ')

while start == 'yes':
    salary = input('please enter the salary: ')
    salary = float(salary)
    if type(salary)  != float or salary <= 0:
        print('Invalid salary.')
        break  # exit from loop
    month = input('Please enter the name of the month: ')
    start = input('Do you want to continue? (Yes/No) ')




