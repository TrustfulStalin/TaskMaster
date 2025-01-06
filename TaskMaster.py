import random
pick = int(input("Please select an option"))
tasks = [""];
randomstuff = ["Sleeping" , "Gaming","Fishing","Racing","Resting","Walking","Going for a drive","Meeting a friend","Cooking"]


def customTask():
    
 Ntask = str(input("Enter the name of this task---"));
 tasks.append(Ntask);
 print("Custom Task added!");
    

def AddRandom():
    Rtasks = random.choice(randomstuff)
    tasks.append(Rtasks)
    print("Random Task added!!!")

def Showinglist():
 print(tasks)

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
  

while True:
    print("\nSelect an option:")
    print("Press 1 to add a custom task")
    print("Press 2 to add a random task to list")
    print("Press 3 to view list")
    print("Press 4 to delete a task from the list")
    print("Press 5 to exit")
    
    try:
        pick = int(input("Please select an option: -- "))
        
        if pick == 1:
            customTask()
        elif pick == 2:
            AddRandom()
        elif pick == 3:
            Showinglist()
        elif pick == 4:
            Deletetask()
        elif pick == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
    
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
