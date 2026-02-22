def calculate_pay(rate, hours, tax_rate):
    if hours > 80:
        regular_pay = 80 * rate
        overtime_hours = hours - 80
        overtime_pay = (rate * 1.5) * overtime_hours
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours * rate
    tax = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - tax

    return net_pay



rate = float(input("Enter hourly rate:"))
hours = float(input("Enter hours worked:"))
tax_rate = float(input("Enter tax rate:"))

result = calculate_pay(rate, hours, tax_rate)
print(result)
