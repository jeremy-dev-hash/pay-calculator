def calculate_pay(rate, hours_1, hours_2, tax_rate):
    gross_pay = (hours_1 + hours_2) * rate

    if hours_1 > 40:
        overtime_hours_1 = hours_1 - 40
        overtime_pay_1 = (rate * .5) * overtime_hours_1
        gross_pay += overtime_pay_1

    if hours_2 > 40:
        overtime_hours_2 = hours_2 -  40
        overtime_pay_2 = (rate * .5) * overtime_hours_2
        gross_pay += overtime_pay_2


    tax = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - tax

    return net_pay



rate = float(input("Enter hourly rate:"))
hours_1 = float(input("Enter hours worked in week one:"))
hours_2 = float(input("Enter hours worked in week two:"))
tax_rate = float(input("Enter tax rate:"))

result = calculate_pay(rate, hours_1, hours_2, tax_rate)
print(f"Your take home pay is {result}!")
