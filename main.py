from calc_func import add, subtract, multiply, divide, power

def main():
    print("Welcome to the Calculator App")
    print('''Select the function from the given option:-
          1. Add 
          2. Subtract 
          3. Multiply 
          4. Divide
          5. Power''')
    
    choice = input("Enter choice: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
        
    elif choice == '2':
        print("Result:", subtract(num1, num2))
        
    elif choice == '3':
        print("Result:", multiply(num1, num2))
        
    elif choice == '4':
        print("Result:", divide(num1, num2))
        
    elif choice == '5':
        print("Result:", power(num1, num2))
        
    else:
        print("Invalid input!!!")

if __name__ == "__main__":
    main()