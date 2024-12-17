import yfinance as yf
import pandas as pd
import csv

user_credentials = {}

def register_user(email, password):
   
    if '@' not in email:
        print("Invalid email address. Please include '@' in the email.")
        return False
    if email in user_credentials:
        print("User already exists.")
        return False
    user_credentials[email] = password
    return True

def authenticate_user(email, password):
    return user_credentials.get(email) == password

def get_closing_prices(ticker, start_date, end_date):
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        return stock_data['Close']
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None

def analyze_closing_prices(closing_prices):
    avg_price = closing_prices.mean()
    pct_change = ((closing_prices.iloc[-1] - closing_prices.iloc[0]) / closing_prices.iloc[0]) * 100
    highest_price = closing_prices.max()
    lowest_price = closing_prices.min()

    return {
        "Average Price": round(avg_price, 2),
        "Percentage Change": round(pct_change, 2),
        "Highest Price": round(highest_price, 2),
        "Lowest Price": round(lowest_price, 2),
    }

def save_to_csv(data, filename):
    try:
        file_exists = False
        try:
            pd.read_csv(filename)
            file_exists = True
        except FileNotFoundError:
            pass

        with open(filename, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def read_from_csv(filename):
    try:
        data = pd.read_csv(filename)
        print(data)
    except FileNotFoundError:
        print("No data found. Please save some analysis results first.")
    except Exception as e:
        print(f"Error reading from CSV: {e}")
