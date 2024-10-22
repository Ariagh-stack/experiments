def main():
    def princess():
        adjective = input("Adjective: ")
        persons_name = input("Persons name: ")
        country = input("Country: ")
        kingdom = input("Kingdom: ")
        plural_noun = input("Plural noun: ")
        verb = input("Verb: ")
        color = input("Color: ")
        print("_" * 50)

        the_princess = (f"Once upon a time, there was a {adjective} princess named {persons_name}"
                       f"she was from\n{country} she lived in a beautiful kingdom on the hills called {kingdom} she\nhad "
                       f"five {plural_noun} while she was {verb} the horse she fell off of the horse and her\ndress had a {color} "
                       f"stain on it when she got back to the kingdom she quickly changed\nto she could wash her dress her\n")

        print(the_princess)


    def rainy():
        adjective = input("Adjective: ")
        color = input("Color: ")
        noun = input("Noun: ")
        plural_noun = input("Plural noun: ")
        persons_name = input("Persons name: ")
        place = input("Place: ")
        print("_"*50)

        a_rainy_day = (f"One {adjective} day, I was walking my {color} pet {noun} when {plural_noun} started flying"
                       f"\nfrom the sky! I called my friend {persons_name}"
                       f" and she said one just\nlanded right on her {place} !\n")

        print(a_rainy_day)


    print("Hi! Welcome to MadLibs!\n")
    subjects = {1: "a_rainy_day", 2: "the_princess"}
    inp_subject = int(input(f"Please Enter your subject between\nthese subjects {subjects}\n(Plaese enter a number): "))

    while True:
        match inp_subject:
            case 1:
                rainy()
                break
            case 2:
                princess()
                break
            case _:
                print("Wrong input!")
                inp_subject = int(input(
                    f"Please Enter your subject between\nthese subjects {subjects}\n(Plaese enter a number): "))

    print("\nThanks for your precious time!")