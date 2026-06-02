'''
GCIS 123.607: Software Development and Problem Solving I
Assignment 3: Problem-Solving Acitivty 3 - Food Ordering System
Group Members:
HAYYA SABOOR - 434000367
DHEERAJ SHIJUKUMAR - 433008033
SAMIYAH SIDDIQUI - 433001732
Manifesto:
Hayya Saboor: Did Task 1 and Task 3
Samiyah Siddique: Completed Task 2
Dheeraj Shijukumar: Completed Task 4 wrote main function, handled the debugging and testing of the code along with adding
comments and docstrings. 
All participated in discussion of the code and logic, did problem solving 
and reviewed the code.
This script implements:
- A menu dictionary (Task 1)
- Combo and Order classes with usage of __slots__ and methods (Task 2 & 3)
- User interaction for order creation and display (Task 4)
Every step/code block is explained with comments and docstrings.

'''
# ----------------------------------------------------------------------------
# Task 1: Menu Dictionary
# ----------------------------------------------------------------------------
'''We define a menu with three categories. Each category contains items and their prices.'''
menu = {
    "Drinks": {
        "Cola" : 5.0,
        "Juice" : 7.0
    },
    "Entrees":{
        "Burger" : 20.0,
        "Pizza" : 25.0
    },
    "Sides": {
        "Fries" : 8.0,
        "Salad" : 10.0
    }
}

# ------------------------------------------------------------
# Task 2: Combo Class
# --------------------------------------------------------------

class Combo:
     """

    Represents a single combo order including a drink, an entree, and a side dish.
    Attributes:
        drink (str): Selected drink item.
        entree (str): Selected main dish.
        side (str): Selected side item.
        totalprice (float): Total price for the combo.

    We use __slots__ for attributes: drink, entree, side, and total_price.
    Then use a constructor to initialize all fields and calculate the total combo price using the menu dictionary.
    We assumed that at most one item from each menu category can be accepted.
    Combo items must be received in order (but not all of them need to be provided)
    We defined a method get_total() to return the calculated total combo price as a number.
    We defined a method display_combo() to print combo details.

    """
     __slots__=["drink", "entree", "side", "total_price"]

     def __init__(self, drink, entree, side, menu):
        """
        We will Initialize a combo with the drink, entree, side.
        Non-existent or empty items are ignored.
        Calculates the total combo price based on the menu.
        """
        # Accept only valid items; otherwise, set as None
        # Validate drink
        if drink in menu["Drinks"]:
            self.drink=drink
        else:
            self.drink= None
        
        # Validate entree
        if entree in menu["Entrees"]:
            self.entree=entree
        else:
            self.entree= None
        # Validate side
        if side in menu["Sides"]:
            self.side=side 
        else:
            self.side= None
        
        self.total_price=0.0
        # Calculate total price based on valid selections
        if self.drink:
            self.total_price+=menu["Drinks"][self.drink]
        if self.entree:
            self.total_price+=menu["Entrees"][self.entree]
        if self.side:
            self.total_price+=menu["Sides"][self.side]
    
     def get_total(self):
        """
        Returns the total combo price as a float number.
        """
        return self.total_price
    
     def display_combo(self):
        """
        Prints the details of the combo in a user-friendly format.
        It includes the selected drink, entree, side, and total price.
        It does not return anything.
        It handles cases where some items may not be selected.
        """
        print("Combo Details:")
        print(f"Drink: {self.drink or 'None'} | Entrée: {self.entree or 'None'} | Side: {self.side or 'None'}")
        print(f"Total Combo Price: {self.total_price} AED\n")

# ---------------------------------------------------------------------------
# Task 3: Order Class
# ---------------------------------------------------------------------------

class Order:
    """
     Represents a full order which may contain multiple combos.
     Attributes:
         order_id (str): Unique identifier for this order.
         combos (list): List of Combo objects.
         total_amount (float): Total price for all combos in this order.
     Then we initialize them in __init__():
     The combos → empty list
     The total_amount → 0
    
     After that we will define methods:
     add_combo(combo) → adds a Combo object and updates total (by calling the Combos get_total() method).
    display_receipt() → prints all combo details and final total
"""
    __slots__ = ['order_id', 'combos', 'total_amount']
    def __init__(self, order_id): #Constructor to initialize order with ID, empty list of combos and total amount 0.
        self.order_id=order_id
        self.combos=[]
        self.total_amount=0.0

    def add_combo(self, combo):
        '''
        Method to add a combo to the order and update the total amount.
        '''
        self.combos.append(combo)
        self.total_amount+=combo.get_total()
    
    def display_receipt(self): 
        '''
        Method to print the receipt with all combo details and the final total amount.
        '''
        print(f"\nReceipt for Order ID: {self.order_id}")
        print("-----------------------------------")

        for i, combo in enumerate(self.combos, 1): #enumerate to number the combos in the receipt
            print(f"Combo {i}: ")
            print(f"Drink: {combo.drink or 'None'} | Entrée: {combo.entree or 'None'} | Side: {combo.side or 'None'} | Combo Price: {combo.get_total()} AED\n")
            print("-----------------------------------")
        
        print(f"Total Amount: {self.total_amount} AED\n") #Print the final total amount for the order.
# ------------------------------------------------------------------------------
# Task 4: Menu Display User Interaction
# ------------------------------------------------------------------------------
def print_menu(menu):
    '''
    Function to display the menu in the terminal for the user to refer to while placing the order
    '''
    print("\n--- Welcome to Eat and Drink ---")
    print("Today's Menu:")
    for category, items in menu.items(): #iterate through each category and its items
        for item, price in items.items(): #iterate through each item and its price
            print(f"{item} - {price} AED")
print("-" * 34)

def valid_input(prompt, category):
    '''
    Function to get valid user input for drink, entree, and side.
    '''
    while True:  #Loop until valid input is received
        try:
            user_input = input(prompt).strip().title() #Get user input and format it
            if user_input == '': #Allow empty input to skip an item
                return None
            if user_input in menu[category]: #Check if input is valid
                return user_input
            print(f"Invalid {category[:-1]}! Please choose from the menu or leave blank.")
        except Exception as e:
           print(f"Error: {e}. Please try again")
def main(): 
    '''Main function to run the ordering system'''
    print_menu(menu)  #Calling the print_menu function so that it works when you run the code      
    print("\nCreate your combo:")
    d = valid_input("Enter Drink: ", "Drinks")
    e = valid_input("Enter Entrée: ", "Entrees")
    s = valid_input("Enter Side: ", "Sides")

# Create Combo and Order
    combo1 = Combo(d, e, s, menu)
    order1 = Order(order_id=101) 
    if combo1.get_total() == 0.0:
        print("No valid items selected. Unable to create combo.")
    else:
        order1.add_combo(combo1)
        print("\nCombo successfully created!")
        combo1.display_combo()
        order1.display_receipt()
        print("Thank you for ordering with Eat and Drink!") 

if __name__ == "__main__":
    main()

