from functions import (
    register_user,
    authenticate_user,
    get_closing_prices,
    analyze_closing_prices,
    save_to_csv,
    read_from_csv,
)

def main():
    print("Welcome to the Stock Selection Tool!")

    # User Registration and Authentication
    while True:
        choice = input("Do you want to (R)egister or (L)ogin? ").strip().upper()
        if choice == "R":
            email = input("Enter your email: ").strip()
            password = input("Enter your password: ").strip()
            if register_user(email, password):
                print("Registration successful! Please login.")
            else:
                print("Registration failed.")
        elif choice == "L":
            email = input("Enter your email: ").strip()
            password = input("Enter your password: ").strip()
            if authenticate_user(email, password):
                print("Login successful!")
                break
            else:
                print("Invalid credentials. Please try again.")
        else:
            print("Invalid choice. Please select 'R' or 'L'.")

    # Stock Data Retrieval and Analysis
    while True:
        ticker = input("Enter the stock ticker (e.g., AAPL, 1155.KL): ").strip()
        start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
        end_date = input("Enter the end date (YYYY-MM-DD): ").strip()

        closing_prices = get_closing_prices(ticker, start_date, end_date)
        if closing_prices is not None and not closing_prices.empty:
            analysis = analyze_closing_prices(closing_prices)
            print("\nAnalysis Results:")
            print(analysis)

            # Save data
            save_to_csv({
                "email": email,
                "ticker": ticker,
                **analysis
            }, "user_data.csv")

            # Option to view stored data
            if input("Do you want to view stored data? (y/n): ").strip().lower() == 'y':
                read_from_csv("user_data.csv")
        else:
            print("Failed to retrieve stock data. Check the ticker or date range.")

        # Exit or continue
        if input("Do you want to analyze another stock? (y/n): ").strip().lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
