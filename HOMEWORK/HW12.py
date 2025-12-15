try:
    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    if not feedback:
        raise ValueError("Feedback cannot be empty.")
    print("\nThank you for your feedback! ")
    print("Customer Name:", name)
    print("Feedback:", feedback)
except ValueError as e:
    print("\nError :", e)
except Exception:
    print("\nAn unexpected error occurred!")
finally:
    print("\nFeedback system execution completed.")
