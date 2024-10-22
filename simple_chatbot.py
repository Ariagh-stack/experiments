import math
import random
import time

def calculation():
    n, m = input("Enter the two numbers you want an action to be performed on: ").split()
    n = int(n)
    m = int(m)
    action = input("Enter the action to be performed: ")

    while True:
        match action:
            case "+":
                print("Sum: ", m+n, "\n")
                break
            case "-":
                print("Sub: ", m-n, "\n")
                break
            case "*":
                print("Mul: ", m*n, "\n")
                break
            case "/":
                print("Div: ", m/n, "\n")
                break
            case "**":
                print("Pow: ", math.pow(n,m), "\n")
                break
            case _:
                print("wrong Input!")
                action = input("Enter the action to be performed: ")


def facts():
    facts_lst = ("The eye of an Ostrich is bigger than it's brain!\n",
                 "An Octopus has two hearts!\n",
                 "2 + 2 is equal to 4!\n",
                 "The population of planet Earth is greater than 8 billion!\n")

    print(f"The fact is: {random.choice(facts_lst)}")


def run_mad_libs():
    import mad_libs
    mad_libs.main()


def run_password():
    import password
    password.main()


def run_programming_quiz():
    import programming_quiz
    programming_quiz.main()


print("Welcome to Simple chatbot\n")
print("This is a simple chatbot taht you can send commands\nto and it will perform some action."  
      " The five recognized\ncommands are shown below:\n")

flag = True
while flag:
    print("\t1. Tell me your name\n")
    print("\t2. what is the meaning of life\n")
    print("\t3. Calculate [Expression]\n")
    print("\t4. Give me a random fact\n")
    print("\t5. play MadLibs\n")
    print("\t6. give me a strong password\n")
    print("\t7. Take me a Programming quiz\n")
    print("\t0. Exit the chatbot\n")

    user_inp = int(input("Please Enter the number of the action\nyou want to be performed: "))
    print()

    while True:
        match user_inp:
            case 0:
                print("Thanks for your precious time!\n")
                flag = False
                break
            case 1:
                print("My name is Sam chatbot\nAnd I'm designed by @Aria Ghodrati!\n")
                print("\n", "*" * 60)
                time.sleep(10)
                break
            case 2:
                print("The Life that we are living, is a Programm designed by God!\n"  
                      "So only Programmers will understand the purpose of this life!\n")
                print("\n", "*" * 60)
                time.sleep(10)
                break
            case 3:
                calculation()
                print("\n", "*" * 60)
                time.sleep(10)
                break
            case 4:
                facts()
                print("\n", "*" * 60)
                time.sleep(10)
                break
            case 5:
                run_mad_libs()
                print("\n", "*" * 60)
                time.sleep(10)
                break
            case 6:
                run_password()
                print("\n", "*" * 60)
                time.sleep(10)
                break
            case 7:
                run_programming_quiz()
                print("\n", "*" * 60)
                time.sleep(10)
                break
            case _:
                print("Wrong input!")
                user_inp = int(input("Please Enter the number of the action\nyou want to be performed: "))
                print()

print("*" * 60)
# ---------------------------------------------------------------------------

# try:
    #     # Remove any whitespace from the expression
    #     expression = expression.replace(" ", "")
    #
    #     # Use regular expressions to identify the different parts of the expression
    #     numbers = [int(num) for num in re.findall(r'\d+', expression)]
    #     operators = re.findall(r'[\+\-\*/\(\)]', expression)
    #
    #     # Evaluate the expression using a stack-based approach
    #     stack = []
    #     for token in expression:
    #         if token.isdigit():
    #             stack.append(int(token))
    #         elif token in ['+', '-', '*', '/']:
    #             while stack and stack[-1] in ['*', '/'] and token in ['+', '-']:
    #                 op = stack.pop()
    #                 b = stack.pop()
    #                 a = stack.pop()
    #                 if op == '*':
    #                     stack.append(a * b)
    #                 elif op == '/':
    #                     stack.append(a / b)
    #             stack.append(token)
    #         elif token == '(':
    #             stack.append(token)
    #         elif token == ')':
    #             while stack and stack[-1] != '(':
    #                 op = stack.pop()
    #                 if op in ['+', '-', '*', '/']:
    #                     b = stack.pop()
    #                     a = stack.pop()
    #                     if op == '+':
    #                         stack.append(a + b)
    #                     elif op == '-':
    #                         stack.append(a - b)
    #                     elif op == '*':
    #                         stack.append(a * b)
    #                     elif op == '/':
    #                         stack.append(a / b)
    #             if stack and stack[-1] == '(':
    #                 stack.pop()
    #
    #     # Evaluate the remaining operations in the stack
    #     while stack:
    #         op = stack.pop()
    #         if op in ['+', '-', '*', '/']:
    #             b = stack.pop()
    #             a = stack.pop()
    #             if op == '+':
    #                 stack.append(a + b)
    #             elif op == '-':
    #                 stack.append(a - b)
    #             elif op == '*':
    #                 stack.append(a * b)
    #             elif op == '/':
    #                 stack.append(a / b)
    #
    #     # Return the final result
    #     return stack[0]
    #
    # except (IndexError, ValueError):
    #     return "Invalid expression"

