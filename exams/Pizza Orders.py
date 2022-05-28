from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employee_capacity = [int(x) for x in input().split(', ')]
pizzas_made = 0

while pizza_orders and employee_capacity:
    current_pizza = pizza_orders.popleft()
    current_employee = employee_capacity.pop()
    if current_pizza > 10 or current_pizza <= 0:
        employee_capacity.append(current_employee)
    elif current_pizza > current_employee:
        current_pizza -= current_employee
        pizzas_made += current_employee
        pizza_orders.appendleft(current_pizza)
    else:
        pizzas_made += current_pizza

if not pizza_orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    print(f'Employees: {", ".join([str(x) for x in employee_capacity])}')
else:
    print(f'Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizza_orders])}')


