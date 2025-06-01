from loan_app import *

def main():
    print("🔐 Welcome to the Loan Application System")
    user_id = None

    while not user_id:
        print("\n1. Login\n2. Register\n3. Exit")
        choice = input("Select option: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            user_id = login_user(username, password)
            if user_id:
                print("✅ Login successful.")
            else:
                print("❌ Invalid credentials.")
        elif choice == '2':
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            register_user(username, password)
        elif choice == '3':
            print("👋 Goodbye!")
            return
        else:
            print("❗ Invalid choice.")

    # Main Menu
    while True:
        print("\n📋 Main Menu")
        print("1. Apply for Loan")
        print("2. Make a Payment")
        print("3. Check Balance")
        print("4. View Payment History")
        print("5. Logout")

        option = input("Select option: ")

        if option == '1':
            amount = float(input("Enter loan amount: "))
            apply_loan(user_id, amount)
        elif option == '2':
            make_payment(user_id)
        elif option == '3':
            check_balance(user_id)
        elif option == '4':
            view_payment_history(user_id)
        elif option == '5':
            print("👋 Logged out.")
            break
        else:
            print("❗ Invalid option.")

if __name__ == "__main__":
    main()
