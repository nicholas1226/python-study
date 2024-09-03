# tip calculator practice
print("Welcome to the tip calculator")
total_bill = input("What was the total bill?: ")
tip = int(input("How much tip would you like to give? 10, 12, 15"))
people = int(input("How many people to split the bill?: "))

# replace
total = float(total_bill.replace('$', ''))
# print(total)
tip_percentage = float(1 + 0.01 * tip)
# print(tip_percentage)
total_add_tip = total * tip_percentage
pay_per_person = total_add_tip / people

print(f"Each person should pay: ${pay_per_person:.2f}")

# 소수점 반올림, 버림, 올림 함수
import math
number = 3.14159

formatted_number = f"{number:.2f}"
print(formatted_number)  # "3.14"

ceil_number = math.ceil(number)
print(ceil_number)  # 3.15

rounded_number = round(number, 2)
print(rounded_number)  # 3.14

floor_number = math.floor(number * 100) / 100
print(floor_number)  # 3.14

# 출처: https://splayer.tistory.com/31 [S Player:티스토리]