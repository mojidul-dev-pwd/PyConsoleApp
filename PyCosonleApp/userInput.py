userName = input("Please enter your user name:")
print("Username is ",userName)
txt = f"The price is 49 dollars"
print(txt)
price = 59
txt = f"The price is {price} dollars"
print(txt)
#Display the price with 2 decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)
#comma separated value
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)