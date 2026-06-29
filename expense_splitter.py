# Expense Splitter

print("===== Expense Splitter =====")

friends = int(input("Enter number of friends: "))
expenses = []

for i in range(friends):
    amount = float(input(f"Enter expense paid by Friend {i + 1}: ₹"))
    expenses.append(amount)

total = sum(expenses)
share = total / friends

print("\n===== Expense Summary =====")
print("Total Expense: ₹", total)
print("Each Friend Should Pay: ₹", round(share, 2))

print("\nSettlement:")

for i in range(friends):
    difference = expenses[i] - share

    if difference > 0:
        print(f"Friend {i + 1} should receive ₹{round(difference, 2)}")
    elif difference < 0:
        print(f"Friend {i + 1} should pay ₹{round(-difference, 2)}")
    else:
        print(f"Friend {i + 1} is settled.")