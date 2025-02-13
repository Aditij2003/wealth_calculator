def calculate_investment_value(principal, years, rate):

    return principal * (1 + rate/100) ** years

def main():
    print("Wealth Calculator - Final investment value Estimation")
    
    # Get user input for the investment details
    try:
        principal = float(input("Enter the initial investment amount: "))
        years = int(input("Enter the number of years: "))
        rate = float(input("Enter the annual interest rate (in %): "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    # Calculate the investment value
    investment_value = calculate_investment_value(principal, years, rate)
    
    # Display the result
    print(f"\nAfter {years} years, your investment will grow to: ₹{investment_value:}")
if __name__ == '__main__':
    main()
