# Prompt for a single task
task = input("Enter your task:")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case 'high':
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case 'medium':
        print(f"Reminder: '{task}' is a medium priority task. It requires your attention almost immediately.")
    case 'low':
        print(f" Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please enter high, medium or low")

#Time bound check
if time_bound == "yes":
    print("This task is time bound. Consider completing it before the deadline.")

        
    