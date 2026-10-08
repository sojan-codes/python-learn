VAT = 0.13

def subtotal(price, qty):
    return price * qty

def add_vat(amount):
    with_vat = amount + amount * VAT
    return VAT, with_vat

price = int(input('Enter the Price: '))
qty = int(input('Enter the Quantity: '))
amount = subtotal(price, qty)
vat, total = add_vat(amount)

print('Price: ',price)
print('Quantity: ',qty)
print('Subtotal: ',amount)
print('VAT: ',VAT)
print('Total: ',total)
