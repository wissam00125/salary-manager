# Salary Manager project
categories = ['Savings', 'Rent', 'Electricity']
categories_amount = []
categories_percentage = []

start = input('Do you want to start? (Yes/No) ')

while start == 'yes':
    while True:
        salary = input('please enter the salary: ')
        try: 
            salary = float(salary)
            if salary > 0:
                break  # exit from loop
            else: print('Salary must be greater than zero. Please try again')
        except: print('Please enter a valid salary') 
    month = input('Please enter the name of the month: ')
    start = input('Do you want to continue? (Yes/No) ')




