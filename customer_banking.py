# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    #pay = float(input('How much were you paid this week? '))
    print("Welcome to your customer banking app.  Hope your day is going well. We are ready & willing to serve you.")
    savings_balance = float(input("How much money is in your savings? "))
    savings_interest = float(input("What is your current savings account interest rate? "))
    savings_maturity = int(input("How many months have you had the savings account? "))
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your savings account earned interest is a fantastic ${interest_earned:.2f}! And your incredible, updated savings account balance is ${updated_savings_balance:.2f}!")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('How much money is in your CD? '))
    cd_interest = float(input('What is your current CD account interest rate? '))
    cd_maturity = int(input('How many months have you had the CD account? '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your CD account earned interest is a whopping ${interest_earned:.2f}! And your outrageous, updated CD account balance is ${updated_cd_balance:.2f}!")
          
if __name__ == "__main__":
    # Call the main function.
    main()