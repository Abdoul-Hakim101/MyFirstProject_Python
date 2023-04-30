# Write your code here
print("""Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80\n""")
income = 5405.0
print(f"Income: ${income}")
staff_expenses = int(input("Staff expenses:\n"))
other_expenses = int(input("Other expenses:\n"))
print(f"Net income: ${income - staff_expenses - other_expenses}")
