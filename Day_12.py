def operation(func, val1, val2):
    return func(val1, val2)
def addition(val1, val2):
    return val1 + val2
def multiplication(val1, val2):
    return val1 * val2
def substraction(val1, val2):
    return val1 - val2
def division(val1, val2):
    return val1 / val2

operations = {
    "addition" : addition,
    "multiplication" : multiplication,
    "substraction" : substraction,
    "division" : division
}

while True:
    ope = input("Enter The Operation Name:")
    if ope.title() == "Done":
        break
    val1 = float(input("Enter the first value:"))
    val2 = float(input("Enter the Second value:"))
    print(f"{ope} : {operation(operations[ope], val1, val2)}")
    
    
def greet(n):
    def greet_person(name):
        return f"{n}!, {name}"
    return greet_person

first_person = greet("Hello")
secon_person = greet("Namaste")

print(first_person('Sojan'))
print(secon_person('Hari'))

