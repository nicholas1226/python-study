# input function practice
# This line of code will take an input using the input() function
username = input("What is your name?: ")
print("Hello " + username + "!")

# len function practice
length = len(username)
print(length)

#variable practice
glass1 = "milk"
glass2 = "juice"

temp = glass2
glass2 = glass1
glass1 = temp

print(glass1, glass2)

#day 1 project
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print(f"Your band name could be {city} {pet}")