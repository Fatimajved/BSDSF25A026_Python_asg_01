while True:
    password = input("Enter a Password: ")

    upper = False
    lower = False
    digit = False

    for ch in password:
        if ch.isupper():
            upper = True

    for ch in password:
        if ch.islower():
            lower = True
        if ch.isdigit():
            digit = True

    if len(password) >= 8:
        print("Length is correct")
    else:
        print("Length is not correct")

    if upper:
        print("UpperCase condition okay")
    else:
        print("UpperCase condition is missing")

    if lower:
        print("lowerCase condition is okay")
    else:
        print("lowerCase condition is missing")

    if digit:
        print("Digit condition is okay")
    else:
        print("Digit condition is missing")

    # Condition to check password
    if len(password) >= 8 and upper and lower and digit:
        print("Password acceptable !")
        break
    else:
        print("Password is not acceptable.")
        choice = input("Do you want to try again? (y/n): ")
        if choice == "n":
            break