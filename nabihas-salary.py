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
                
                
    total_expenses = sum(categories_amount)
    total_percentage = sum(categories_percentage)
    if(total_percentage > 100):
        print("Total percentage exceeds 100, please try again")
        categories_amount.clear()
        categories_percentage.clear()
        continue    # skip the rest of current iteration and start new one(while)
    
    remainder = salary - total_expenses
    yearly_rent_cost = categories_amount[1] * 12
    yearly_electricity_cost = categories_amount[2] * 12
    
    while remainder > 0:
        extra_saving = input("Do you have extra savings? (Yes/No) ")
        if extra_saving == 'yes':
            try:
                extra_saving_amount = float(input('Enter the extra saving amount in USD: '))
                if extra_saving_amount > 0 and extra_saving_amount <= remainder:
                    remainder -= extra_saving_amount
                    total_expenses += extra_saving_amount
                    categories_amount[0] += extra_saving_amount
                    break
                else:
                    print(f'You can save an additional amount up to ${remainder}')
            except:
                print('Please enter a numerical amount')
        elif extra_saving == 'no':
            break
        else:
            print('Please enter Yes or No only')
            
    categories_amount.clear()
    categories_percentage.clear()      
    print('Total expenses: $', total_expenses)
    print('Remmainder: $', remainder)
    print('Yearly rent cost $', yearly_rent_cost)
    print('yearly electricity cost $', yearly_electricity_cost)
    
    start = input('Do you want to continue? (Yes/No) ')




