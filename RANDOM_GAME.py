import pwinput

def generate():
    
    score = 0
    print("\033[1mInformation of the user\033[0m")

    user_age = int(pwinput.pwinput("Enter user age: ",mask="*"))
    user_fruit = pwinput.pwinput("Enter user fruit: ",mask="*").lower()
    user_ice_cream = pwinput.pwinput("Enter user ice cream: ",mask="*").lower()
    user_country = pwinput.pwinput("Enter user country: ",mask="*").lower()
    user_sport = pwinput.pwinput("Enter user sport: ",mask="*").lower()


    print("\n\033[1mGuess the user information\033[0m")

    age = int(input("Enter the age: "))
    fruit = input("Enter the fruit: ").lower()
    ice_cream = input("Enter the ice cream: ").lower()
    country = input("Enter the country: ").lower()
    sport = input("Enter the sport: ").lower()

    if age == user_age:
        score += 1
    if fruit == user_fruit:
        score += 1
    if ice_cream == user_ice_cream:
        score += 1
    if country == user_country:
        score += 1
    if sport == user_sport:
        score += 1
    print(f"Your score is: {score}")

    if score == 5:
        print("\033[1mEXCELLENT\033[0m")

    elif score < 5 and score >= 3:
        print("\033[1mGOOD\033[0m")

    elif score < 3:
        print("\033[1mBAD\033[0m")

    choose = input("Do you want to continue? (yes/no): ").strip().lower()
    if choose == "yes":
        generate()
    else:
        print("Thank you for using the program!")

generate()
