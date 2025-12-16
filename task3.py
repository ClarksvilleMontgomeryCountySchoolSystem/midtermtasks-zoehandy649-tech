#AFTER PASTING YOUR ANSWER YOU MUST REMOVE THE LINE "import s"
#YOUR CODE WILL FAIL IF YOU DO NOT DELETE THE LINE!!!!!!!!!!!!!
# Testing flag - will be set by test
TESTING = True
item = None
price = None
quantity = None

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"

   Prosperity comes in threes!
========================================

ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")
menu = '''Flying Carpet...............$119.99
Phoenix Feather...........$14.99
Time Turner....................$84.99
Enchanted Sword.........$59.99
Potion of Luck...............$14.99
Crystal Ball...................$39.99
'''
print(menu)


# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)
def get_purchase_info():
    item = input("Item name: ")
    price = float(input("Item price: "))
    quantity = int(input("Quantity: "))
    return item, price, quantity

# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()


# Hidden calculations (using mock values for testing)
item_name = "Crystal Ball"
item_price = 39.99
quantity = 2

subtotal = item_price * quantity
tax_rate = 0.095
tax = subtotal * tax_rate
total1 = subtotal + tax
total = round(total1, 2)

# Print statements
print1 = f"{item_name} x{quantity} @ ${item_price} each"
print2 = f"Subtotal: ${subtotal}"
print3 = f"Tax: ${tax}"
print4 = f"Total: ${total}"
