def main():
    print("Welcome to 'Programming Languages Quiz' app!\n")
    print("In this app, you'll be asked a series of questions about\ndifferent programming languages.\n")
    print("Please answer the questions below:\n")

    q_and_a = {"what programming language took 10 days to develop?": "java",
               "what programming language took 2 years to develop?": "python",
               "what programming language is considered the fastest?": "c",
               "what programming language is considered the slowest?": "ruby",
               "what programming language is considered the most powerfull?": "python",
               "what programming language is best for frontend?": "javascript",
               "what programming language is best for syber security?": "python",
               "what programming language is the most popular one right now?": "c#",}

    correct_answer = 0
    for question in q_and_a:
        print("_" * 40)
        print(question)
        answer = input("Enter your answer: \n")
        if answer == q_and_a[question].lower():
            print("Correct!")
            correct_answer += 1
        else:
            print("Wrong!")

    print("*" * 40)
    print(f"This is your total correct answer: {correct_answer}")

    if correct_answer == len(q_and_a):
        print("Perfect! such a PRO!")
    elif len(q_and_a)//2 <= correct_answer < len(q_and_a):
        print("Great! what a Score!")
    else:
        print("Good! try next time!")

    print("Thanks for your precious time!")

