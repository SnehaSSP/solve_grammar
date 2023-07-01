import datetime


# Define a function for setting and tracking daily habits
def set_daily_habits():
    print("Set your daily habits:")
    habits = []
    while True:
        habit = input("Enter a habit (or 'done' to finish): ")
        if habit.lower() == "done":
            break
        habits.append(habit)
    return habits


# Define a function for self-reflection and gratitude
def reflect_and_grateful():
    reflection = input("Reflect on your day: What went well? ")
    gratitude = input("Express gratitude: What are you grateful for? ")
    with open("../pandas/reflection.txt", "a") as file:
        file.write(f"\nDate: {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
        file.write(f"Reflection: {reflection}\n")
        file.write(f"Gratitude: {gratitude}\n")
        file.write("---------------------------------------------\n")


# Define a function for financial tracking
def financial_tracking():
    income = float(input("Enter your daily income: "))
    expenses = float(input("Enter your daily expenses: "))
    savings = income - expenses
    print(f"Daily savings: ${savings:.2f}")


# Define a function for daily productivity
def daily_productivity():
    tasks = input("Enter your daily tasks (separated by commas): ").split(",")
    print("Today's Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")


# Main program loop
def main():
    while True:
        print("\nDaily Habits for Success and Wealth:")
        print("1. Set Daily Habits")
        print("2. Reflect and Express Gratitude")
        print("3. Financial Tracking")
        print("4. Daily Productivity")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            habits = set_daily_habits()
            print("Daily Habits:")
            for habit in habits:
                print(f"- {habit}")
        elif choice == "2":
            reflect_and_grateful()
            print("Reflection and Gratitude recorded.")
        elif choice == "3":
            financial_tracking()
        elif choice == "4":
            daily_productivity()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the main program loop
main()
