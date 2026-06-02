'''
GCIS 123.607: Software Development and Problem Solving I
Assignment 3: Problem-Solving Acitivty 3 - Food Ordering System
Group Members:
HAYYA SABOOR - 434000367
DHEERAJ SHIJUKUMAR - 433008033
SAMIYAH SIDDIQUI - 433001732
Manifesto:
Hayya Saboor: did task 1 and task 2
Samiyah Siddique
Dheeraj Shijukumar
'''
#Task 1: Create a Menu using Constructor, Dictionary

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
#Task 2: Create class called Combo
class Combo:

   """
   Represents a single food combo consisting a drink, an entree and a side 
   and using these to calculate the total price based on the menu. 
   """
   #Using slots to restrict and optimize atribute management
   __slots__ = ['drink', 'entree', 'side', 'total_price']
   def __init__(self, drink, entree, side, menu_dict):
        self.drink = drink if drink in menu_dict["Drinks"] else None
        self.entree = entree if entree in menu_dict["Entrees"] else None
        self.side = side if side in menu_dict["Sides"] else None
        self.total_price = 0.0
        if self.drink:
          self.total_price += menu_dict["Drinks"][self.drink]
        if self.entree:
         self.total_price += menu_dict["Entrees"][self.entree]
        if self.side:
          self.total_price += menu_dict["Sides"][self.side]

   def get_total(self):
      return self.total_price
   def display_combo(self):
      print("Combo Details: ")
      print(f"Drink: {self.drink or 'None'} | Entrée: {self.entree or 'None'} | Side: {self.side or 'None'}")
      print(f"Total Combo Price: {self.total_price: .1f} AED\n")
#task 3
class Order:
    __slots__ = ['order_od', 'combos', 'total_amount']
    def __init__(self, order_id):
       self.order_id = order_id
       self.combos = []
       self.total_amount = 0.0

    def add_combo(self, combo):
       self.combo.append(combo)
       self.total_amount += combo.get_total()

    def display_receipt(self):
       print(f"\nReceipt for Order ID: {self.order_id}")
       print("---------------------------------")
       for i, combo in enumerate(self.combo, 1):
             print(f"Combo {i}:")
             print(f"Drink: {combo.drink or 'None'} | Entree: {combo.entree or 'None'} | Sides: {combo.side or 'None'} | Combo Price: {combo.get_total(): .1f} AED")
             print("--------------------------------")
       print(f"Total Amount: {self.total_amount: .1f} AED\n")

#Task 4: Menu Display and User Interaction
def print_menu(menu_dict):
   print("---Welcome to the Restaurant---")
   print("Today's Menu")
   for category, items in menu_dict.items():
       for item, price in items.items():
           print(f"{item} - {price:.1f} AED")
print("-" * 34)

def get_valid_input(prompt, category):
   while True: 
      user_input = input(prompt).strip().title()
      if user_input == '':
         return None
      if user_input in menu [category]:
         return user_input
      print(f"Invalid {category[:-1]}! Please choose from the menu or leave blank.")
def main():
   print_menu(menu)
   order_id = input("Enter your Order ID: ").strip()
   order = Order(order_id)  

   while True:
      print("\nCreate your Combo: ")
      drink = get_valid_input("Enter drink: ",)    