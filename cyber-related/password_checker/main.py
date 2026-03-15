from password_checker import check_password_strength

def main():
    while True:
        password = input("Enter a password to check: ")

        strength, feedback = check_password_strength(password)

        print(f"\nPassword Strength: {strength}")

        if feedback:
            print("Suggestions to improve:")
            for item in feedback:
                print("-", item)
        else:
            print("Great password!")

        # Ask user if they want to try again
        again = input("\nDo you want to check another password? (y/n): ").lower()

        if again != "y":
            print("Goodbye! 👋")
            break


if __name__ == "__main__":
    main()