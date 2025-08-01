from datetime import datetime

def get_current_date():
    """Gets the current date."""
    return datetime.now()

def calculate_age(birth_date):
    """Calculates the age based on a birth date."""
    today = get_current_date()
    # Subtract the years and then subtract 1 if the current month/day is before the birth month/day
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    """Main function to get user input and display the age."""
    try:
        birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")

        if birth_date > get_current_date():
            raise ValueError("Birth date cannot be in the future.")

        age = calculate_age(birth_date)
        print(f"You are {age} years old.")
    except ValueError as e:
        # Provide a more specific error for invalid date format
        if "match format" in str(e):
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
