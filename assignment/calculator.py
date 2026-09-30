name = input('Enter your Name: ')
price = int(input('Enter the Price: '))
quantity = int(input('Enter the Quantity: '))
tax = 0.13
amt = price*quantity
print('Name:',name , '\nPrice: Rs',price , '\nQuantity:',quantity , '\nTax rate (%):',tax*100 , '\nTotal Price: Rs',(amt + tax*amt))

