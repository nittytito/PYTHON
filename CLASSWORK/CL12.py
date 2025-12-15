import re

try:
    title = input("Enter book title: ").strip()
    if not re.fullmatch(r"[A-Za-z ]+", title):
        raise ValueError("Invalid book title! Only alphabets and spaces are allowed.")
    year = input("Enter publication year: ").strip()
    if not re.fullmatch(r"(19|20)\d{2}", year):
        raise ValueError("Invalid publication year! Must be a 4-digit year starting with 19 or 20.")
    print("\nBook Details Accepted ✅")
    print("Title:", title)
    print("Publication Year:", year)
except ValueError as e:
    print("\nError :", e)
except Exception:
    print("\nUnexpected error occurred!")
finally:
    print("\nProgram execution completed.")
