import time
import pandas as pd
import random
import matplotlib.pyplot as plt
print("Welcome to CPFC Transfer SIM.")


#Menu
#time.sleep(2)


#Cleaning the csv file
def clean():
    """Cleans dataframe to remove rows with empty fields"""
    df = pd.read_csv('players.csv')
    mask = df['Name'] != ""
    df = df[mask]
    return df

#Min + Max Checker
def is_int_in_bounds(ip, min, max):
    """Check if input integer within min and max """
    try:
        ip_int = int(ip)   # try converting to int

        if ip_int >=min and ip_int <= max:
            return True
        else:
            return False
    except:
        return False

#Responses
good_responses = [
    "Yes,Pleasure doing business",
    "We can agree to that. Lets sort the paperwork",
    "Brilliant!, hope we can do more together in the future"
]
good_selected_responses = random.choice(good_responses)

bad_responses = [
    "This feels like an insult.",
    "Sorry this offer is not to standard.",
    "Are you wasting my time?"
]

bad_selected_responses = random.choice(bad_responses)

#Main Negotiation Function
def negotiation():
    """This Function will be in charge of the main negotiation with the user"""
    print("------Position Menu------")
    print("""Please enter one of the following:
          attacker
          midfielder
          defender
          keeper""")
    data = pd.read_csv('players.csv')
    position = input("Player Position: ")
    filter_condition =(data['Position'] == position)
    selected_rows = data[filter_condition]
    print(selected_rows)

    player = input("Which player would you like to transfer?")
    mask = data['Name'] == player
    data = data[mask]
    sell_value = data.iloc[0,1]

    while True:
        user_value = float(input(f"Enter offer for {player}: "))
        #print(sell_value)
        if user_value >= float(sell_value):
            print(good_selected_responses)
            break
        else:
            print(bad_selected_responses)

def graph():
    """Plot a graph to show most valuble players"""
    df = pd.read_csv('players.csv')

    
    # x = df['Name']
    # y = df['Value']
    # plt.bar(x,y)
    # plt.title("Player Value")
    # plt.xlabel("Player Names")
    # plt.ylabel("Values")
    # plt.show()


def main_menu():
    """Main Menu function for every part of the program"""
    flag = True

    while flag:
        print("------Main Menu------")
        print("1.Position Menu")
        print("2.Clean Database Rows")
        print("3.Value Graph")
        print("4.Exit")
    

        menu_choice = input("Please enter the number of your choice (1-4): ")

        if (is_int_in_bounds (menu_choice, 1, 4) ):
            return int(menu_choice)
        else:
             print("Sorry, you entered an invalid choice.")
             flag = True

             #Cleaning the csv file

def process_menu_choice():
    """Determines what to execute based on users choice"""

    if  main_menu_choice == 1:
        negotiation()
    elif main_menu_choice == 2:
        clean()
        print("Cleaning Complete")
    elif main_menu_choice == 3:
        graph()
    elif main_menu_choice == 4:
        print("Exiting")
        exit
    else:
        print("ERROR - Invalid option provided")

#Main Code
main_menu_choice = main_menu()
process_menu_choice()