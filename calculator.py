while True:   
 #asking user to enter the two numbers and the preffered operator 
    num1 = float(input ("Please type your first number: "))
    num2 = float(input ("Please type your second number: "))
    operator = input("Choose one: (+, -,  /, *): ").strip()
    answer = "ERROR!! DIVISION BY 0 NOT ALLOWED"
    #operation based to the users input
    if operator == "+":
        answer = num1 + num2      #addition

    elif operator == "*":
        answer = num1 * num2       #multiplication 

    # handling division by zero     
    elif operator == "/":
        if num2 == 0:
            answer = "ERROR!! DIVISION BY 0 NOT ALLOWED"
        else:
            answer = num1 / num2            #division

    elif operator == "-":
        answer = num1 - num2        #subtraction 

    # printing the answer
    print (f"{num1}  {operator}  {num2} = {answer}")

    # Ask if the user wants to calculate again
    again = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for using Erick's calculator. Goodbye!")
        break