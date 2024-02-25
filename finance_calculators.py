import math

while True:
    # Display the menu and prompt the user for choice
    print("""Menu:
    investment - calculate interest on investment 
    bond       - calculate home loan repayment""")
    
    user_choice = input("\nEnter 'investment' or 'bond': ").lower()

    if user_choice == "investment":
        try:
            # Input for investment calculator
            principal_amount = float(input("Enter the amount of money to deposit: "))
            interest_rate = float(input("Enter the interest rate: "))
            num_of_years = float(input("Enter the number of years to invest: "))
            
            # Validate the number of years
            if num_of_years <= 0:
                print("Invalid input. Number of years must be a positive value.")
                continue  # Restart the loop

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue  # Restart the loop

        interest_type = input("\nEnter 'simple' for simple interest or 'compound' for compound interest: ").lower()

        # Calculate interest
        interest_rate /= 100
        if interest_type == "simple":
            total_amount = principal_amount * (1 + interest_rate * num_of_years)
        elif interest_type == "compound":
            total_amount = principal_amount * math.pow((1 + interest_rate), num_of_years)
        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")
            continue  # Restart the loop

        # Display result
        print(f"\nThe total amount when {interest_type} interest is applied: {total_amount:.2f}")
        break  # Exit the loop

    elif user_choice == "bond":
        try:
            # Input for bond calculator
            house_value = float(input("Enter the present value of the house: "))
            interest_rate = float(input("Enter the interest rate: "))
            months_to_repay = float(input("Enter the number of months to repay the bond: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue  # Restart the loop

        interest_rate /= 100
        monthly_interest_rate = interest_rate / 12

        # Calculate monthly repayment
        monthly_repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)**(-months_to_repay))

        # Display result
        print(f"\nYou'll have to repay each month: {monthly_repayment:.2f}")
        break  # Exit the loop

    else:
        print("Invalid choice. Please enter 'investment' or 'bond'.")
        # Prompt user to enter a valid choice instead of restarting the loop
        user_choice = input("\nEnter 'investment' or 'bond': ").lower()
