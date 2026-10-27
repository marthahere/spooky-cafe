print("WELCOME TO THE SPOOKY CAFE")
print("Here is our spooky menu:")

menu = {
    "1": ("Pumpkin Latte", 5.00),
    "2": ("Witch's Brew", 4.50),
    "3": ("Vampire Hot Chocolate", 4.00)
}

# number: (drink, price)

for number, (drink, price) in menu.items():
    print(f"{number}: {drink} ${price:.2f}")

choice = input("Choose a drink (1, 2 and 3): ")

if choice in menu:
    drink, price = menu[choice]
    quantity = int(input("How many? "))

    total = price * quantity

    print("Your ordered", quantity, drink)
    print(f"Your total is ${total:.2f}")

else:
    print("CHOOSE RIGHT")