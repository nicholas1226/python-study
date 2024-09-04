# Pizza Deliveries Practice

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

# todo: work out how much they need to pay based on their size choice.
# todo: work out how much to add to their bill based on their pepperoni choice.
# todo: work out their final amount based on whether if they want extra cheese.

final_amount = 0

if size == "S":
    final_amount += 15
    if pepperoni == "Y":
        final_amount += 2
    if extra_cheese == "Y":
        final_amount += 1
if size == "M" or "L":
    if size == "M":
        final_amount += 20
    if size == "L":
        final_amount += 25
    if pepperoni == "Y":
        final_amount +=3
    if extra_cheese == "Y":
        final_amount += 1

print(f"${final_amount}")