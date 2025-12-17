# TESTING must = False!!!!!!
ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")

menu ='''
Flying Carpet...............$119.99
Pheonix Feather ...............$14.99
Time Turner...............$84.99
Enchanted Sword...............$65.99
Potion of Luck...............$11.99
Crystal Ball...............$39.99
'''
print(menu)

# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)

def get_purchase_info(): # Convert input when necessary
    item = input("What is the name of your item?")
    price = input(float("How much did your item cost?"))
    quantity = input(int("How many items did you get?"))
    return item, price, quantity

# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()

# Calculate using the input values (NOT hardcoded!)
subtotal = price*quantity
tax_rate = 0.095 #This is slightly different from the review. The tax multiplier is stored into a variable.
tax = subtotal*tax_rate
total = subtotal+tax
total = input(round(total, 2))

# Print statements
print("--------------------------")
print("Invisibility Cloak x5 @ $45.00 each")
print("--------------------------")
print(f"Subtotal: {subtotal}")
print(f"Tax: {tax}")/nprint(f"Total: {total}")
print("\nThank you for shopping at\nThe Peculiar Emporium!")
