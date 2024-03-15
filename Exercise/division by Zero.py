try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    Percentage = value / total_value * 100
    print(f"That is", str(Percentage) + '%')
except SyntaxError:
    print("Enter a Float")
except ZeroDivisionError:
    print("Your Total Value Cannot be Zero")