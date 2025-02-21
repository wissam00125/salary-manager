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
    
    for i in range(3):
        while True:
            try:
                percentage = float(input(f'Enter the percentage of {categories[i]}: '))
                if percentage >= 0 and percentage <= 100:
                    categories_percentage.append(percentage)
                    amount = (percentage * salary) / 100
                    categories_amount.append(amount)
                    break # exit from loop
                else:
                    print("Percentage should be between 0 and 100")
            except:
                print("Please enter a numerical value")
    start = input('Do you want to continue? (Yes/No) ')




