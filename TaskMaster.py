import random

# Initialize task list and possible random tasks
tasks = []
randomstuff = ["Sleeping", "Gaming", "Fishing", "Racing", "Resting", "Walking", "Going for a drive", "Meeting a friend", "Cooking"]

# Function to add a custom task
def customTask():
    Ntask = input("Enter the name of this task: ")
    tasks.append(Ntask)
    print("Custom Task added!")

# Function to add a random task from the predefined list
def AddRandom():
    Rtasks = random.choice(randomstuff)
    tasks.append(Rtasks)
    print("Random Task added!")

# Function to show the task list
def Showinglist():
    if tasks:
        print("Task List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")

# Function to delete a task by task number
def Deletetask():
    if tasks:
        Showinglist()
        try:
            tasknumber = int(input("Choose the task number to delete: "))
            if 1 <= tasknumber <= len(tasks):
                print(f"Task '{tasks.pop(tasknumber - 1)}' has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("No tasks to delete.")

# Function to clear all tasks from the list
def clear_list():
    if not tasks:  # Check if the list is already empty
        print("This list is already empty!!!")
        print("Redirecting......")
        main()  # Redirects to the main function or another action
    else:
        tasks.clear()  # Clears all tasks from the list
        print("All tasks have been cleared.")

# Main menu loop
def main():
    while True:
        print("\nSelect an option:")
        print("Press 1 to add a custom task")
        print("Press 2 to add a random task to list")
        print("Press 3 to view list")
        print("Press 4 to delete a task from the list")
        print("Press 5 to clear all tasks from the list")
        print("Press 6 to exit")
        
        try:
            pick = int(input("-- Please select an option (1-6): "))
            
            if pick == 1:
                customTask()
            elif pick == 2:
                AddRandom()
            elif pick == 3:
                Showinglist()
            elif pick == 4:
                Deletetask()
            elif pick == 5:
                clear_list()
            elif pick == 6:
                print("Exiting the program.")
                exit()  # Terminates the program
            else:
                print("Invalid option. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

# Run the program
main()