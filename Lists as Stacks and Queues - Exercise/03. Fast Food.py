from collections import deque

quantity = int(input())

order_queue = deque([int(q) for q in input().split()])
print(max(order_queue))

while order_queue:
    first_order = order_queue[0]
    if quantity - first_order >= 0:
        quantity -= order_queue.popleft()
    else:
        break

if not order_queue:
    print('Orders complete')
else:
    remaining_orders = ' '.join([str(x) for x in order_queue])
    print(f'Orders left: {remaining_orders}')

