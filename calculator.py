def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print('Select Operation!')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

selection = False
while selection == False:
    choice = input('Enter Choice(1/2/3/4): ')
    try:
       if int(choice)<5 and int(choice)>= 1:
          selection =int(choice)
          selection = True
       else:
           print("That's not a valid choice!")
    except ValueError:
       print("That's not even valid input!")
#Take input from the user



num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
if choice == '1':
    print(num1,'+', num2, "=", add(num1,num2))
elif choice =='2':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice =='3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice =='4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid Input")
