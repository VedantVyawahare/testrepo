#addition
def add(n1 , n2):
    return n1+ n2
#subtraction
def subtract(n1 , n2):
    return n1 - n2
#multiply
def multiply(n1 , n2):
    return n1 * n2
#division
def divide(n1 , n2):
    return n1/n2

operations = {"+": add , "-": subtract , "*" : multiply , "/" : divide}
should_continue = True

num1 = int(input("Enter the first number: "))
operation_symbol = input("choose from the above operation to perform that task: ")
while should_continue:    
    num2 = int(input("Enter the second number: "))
    for sign in operations:
        print(sign)


    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1 , num2)

    print(answer)
    operation_2 = (input("enter the operation : "))
    num3 = int(input("enter the number for calculation: "))
    calculation_function = operations[operation_2]
    answer_2 = calculation_function(answer, num3)

    if input("do you want to continue with answer:type yes or  no")  == "yes":
        num1 = answer
    else:
        should_continue = False


