bill = float(input("Enter total bill amount: "))
due = bill

while due > 0:
    pay = float(input("Enter payment amount: "))
    due = due - pay

    if due > 0:
        print("Remaining due:", due)
    elif due < 0:
        print("Return change:", -due)
    else:
        print("Bill fully paid!")

print("Thank you!")