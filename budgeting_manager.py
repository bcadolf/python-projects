



import json
import os
from datetime import datetime as dt


def main():
    """Path of functions:
        user open program, program asks if they would like to create a newbudget or pull up and old one. find old budget or begin to build new one
        New:
        Have them enter the goals and associated information

        New and Old:
        Menu option for the use to select different options

        save all the current updates to file. close program
        """


    #intial welcome and user choice
    print("Welcome to the Budget Manager.")
    new_old = str(input("Would you like to create a new budget or use an old one? (new/old) "))
    
    #format the usesr reply and read string to decided intial path
    new_old = new_old.lower()
    if new_old == "new":
        name = str(input("Please enter the budget name: ")) 
    
    #user input will allow for creation or reading of the files
        budget_file_name = name_budget(name)
        goals = int(input("Please enter number of desired goals: "))
        budget_file = budget_goals(goals)
        goals_dict = form_goals_dict(budget_file)
        view_budget(goals_dict)
    elif new_old == "old":
        goals_dict, budget_file_name = open_old_file()
        view_budget(goals_dict)


    
    # next step is to display a menu option for the user
    menu = {
        1 : "View All Goals",
        2 : "Deposit Paycheck",
        3 : "Withdraw From Goal", #does not currently work
        4 : "Save and Exit"
    }
    end = "n"
    while end.lower() != "y":
        for i in menu:
            print(f"{i}. {menu[i]}")
        path = int(input("Enter a number from above: "))
        if path == 1:
            view_budget(goals_dict)
        elif path == 2:
            paycheck = float(input("Enter paycheck amount: $ "))
            goals_dict = run_budget(paycheck, goals_dict)
        elif path == 3:
            print("Not Currently An Option Check Back Later")
        else:
            create_storage_files(budget_file_name, goals_dict)
            end = input("File Saved Please Confirm To End The Program (y/n): ")

# ============================================= 
def view_budget(goals_dict):
        """Call the calculations of the budget goals file and diplay them for the user. 
            Parameters:
                stored budget file 
            Return:
                the budget goals in a printed format"""
        # asthetics spacing
        print("")
        # declare 
        print(f"Here is your list of goals:")
        for goal in goals_dict:
            name = goal
            print(name)
            for x, y in goals_dict.get(name).items():
                print(f"{x}: {y}")

def open_old_file():
    print(f"Please find your Budget in the list and type the name as it appears below:")
    for i in os.listdir():
        if i.endswith(".json"):
            print(i)
    name = str(input("Enter Filename: "))
    with open(name) as budget:
        budget_file = json.load(budget)
    return budget_file, name

def budget_goals(goals_num):
    goals_list = []
    for i in range(0, goals_num):
        print(f"For goal number {i+1}.")
        name = input("Please enter the name of goal: ")
        qty = float(input("Please enter the percentage of paycheck alloted (Keep in mind total should be 100% with all the goals): %"))
        account = input("Please enter the account it is stored in: ")
        current_balance = float(input("Please enter the current balance: "))
        last_update = time_stamp()
        list = [name, qty, account, current_balance, last_update]
        goals_list.append(list)
    return goals_list

def time_stamp():
    """Collect and format the current date and time for easy of use"""
    current_date_and_time = dt.now()
    format_date_and_time = f"{current_date_and_time:%A %b %d %I:%M %p}"

    return format_date_and_time

def name_budget(title):
    """Gather the user input for the budget title and turn it into a filename.
        Parameters:
            user input of title
        Return: 
            filename"""
    formated_title = title.strip().lower().replace(" ", "_")
    budget_filename = f"{formated_title}.json"
    return budget_filename


def form_goals_dict(goals_list):
    """Gather the goals desired and create the dictionary related to each goal.
        Parameters:
            goals list
        Return:
            budget goal in dictionary
        """
    goals_dict= {}

    for i in range(len(goals_list)):
        inner_list = goals_list[i]
        name = inner_list[0]
        qty = inner_list[1]
        account = inner_list[2]
        current_balance = inner_list[3]
        time = inner_list[4]
        goals_dict.update({name : {
            "Percentage" : qty,
            "Account" : account,
            "Current Balance" : current_balance,
            "Time" : time
        }})
    
    return goals_dict

def run_budget(paycheck, goals_dict):
    """Call all of the current budget goals, calulate the dispertion of the new funds added. Update all balances.
        Parameters:
            current goals
            qty calulations
            new paycheck or qty to add
            current balance
        Formulas:
            new balance = new paycheck divided into the qty calulations + the current balance
        Return: 
            New balances
            """
    qty_list = []
    balance_list = []
    dict = goals_dict
    i = 0
    for goal in goals_dict:
        qty = goals_dict.get(goal).get("Percentage")
        qty_list.append(qty)
        balance = goals_dict.get(goal).get("Current Balance")
        balance_list.append(balance)
        new_balance = (qty_list[i] / 100) * paycheck + balance_list[i]
        balance_list[i] = new_balance
        goals_dict[goal].update({"Current Balance" : balance_list[i]})
        i += 1
    return dict

def create_storage_files(filename, goals_dict):
    """"""
    with open(filename, "w") as budget:
        json.dump(goals_dict, budget, indent = 6)


if __name__ == "__main__":
    main()














"""Ideas for later or code to reference, retired functions"""
# with open("final_project/budget_sheet.csv", "at") as budget_sheet_file:
#     print(current_paycheck(), file=budget_sheet_file)
# def intial_path(path):
#     """Function to define the intial path of the program"""
#     if path == "new":
#         new = str(input("Please enter the new budget name: "))
#         budget_file_name, calculations_file_name = name_budget(new)
#     elif path == "old":
#         old = str(input("Please enter the old budget name: "))
#         budget_file_name, calculations_file_name = name_budget(old)
#     return budget_file_name, calculations_file_name
# function for collecting paycheck amount
# def current_paycheck(paycheck):
#     """Collect the current paycheck information and put it into a value with the date for recording in the textfile."""
#     deposit_date = dt.today()
#     deposit = (f"{paycheck: .2f}")
#     return deposit
# def retrieve_current_balance(filename):
#     """Pull the information of the budget from the file it is stored in.
#         Parameters:
#             file name
#         Return:
#             the budget stored in a list or dictionary
#         """
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv('filename')

#     # Convert the DataFrame to a list of dictionaries (one per row)
#     csv_to_dict = df.to_dict('records')

#     # Print the resulting list of dictionaries
#     current_balance = csv_to_dict[LAST_UPDATED]
#     return current_balance
# def change_budget_goals():
#     """Change previous budget goals.
#         Parameters:
#             old goal name
#             what you want to do (delete goal, update name, update qty distribution)
#         Return:
#             new/changed goal
#         """

    




    
# def select_goal_balance_view():
#     """parse the budget for a specifed budget goals calculation
#         Parameters:
#             file name of budget calcuations
#             file name of budget balance sheet
#             name of goal to check.
#         Return:
#             selected goal calculation"""
    
# def withdraw_from_goal():
#     """Parse for goal, and alter the balance to remove the qty specified.
#         Parameters:
#             filename
#             goal name
#             qty to change
#         Return:
#             new balance
#         """
    
# def deposit_to_goal(): # Consider merging withdraw by adding new parameter.
#     """Parse for goal, and alter the balance to add the qty specified.
#         Parameters:
#             filename
#             goal name
#             qty to change
#         Return:
#             new balance"""