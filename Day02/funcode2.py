## Script for splitwise calculator

print("This is Splitwise calculator")

x = float(input("What was the total amount? $"))
y = int(input("What percentage tip did you give? 10, 12, or 15"))
z = int(input("How many people in total to divide?"))

answer = (y / 100 * x + x) / z
print(f"Each needs to contribute: {answer}")

answer = (y / 100 * x + x) / z
answer = round(answer)
print(f"Each needs to contribute: {answer}")

print(5 * 24)   # For testing the result