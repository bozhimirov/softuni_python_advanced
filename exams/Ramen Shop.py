from collections import deque

bowls_ramen = [int(x) for x in (input().split(', '))]
customers = deque(int(x) for x in (input().split(', ')))

while bowls_ramen and customers:
    current_ramen = bowls_ramen.pop()
    current_customer = customers.popleft()
    if current_ramen >= current_customer:
        if current_ramen > current_customer:
            current_ramen -= current_customer
            bowls_ramen.append(current_ramen)
    elif current_customer > current_ramen:
        current_customer -= current_ramen
        customers.appendleft(current_customer)

if not customers:
    print(f'Great job! You served all the customers.')
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
