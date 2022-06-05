def shopping_list(number, **kwargs):
    budget = number
    items = 0
    result = []
    if number >= 100:
        for product, value in kwargs.items():

            if items < 5:
                price, quantity = float(value[0]), int(value[1])
                total_price = price * quantity
                if total_price <= budget:
                    budget -= total_price
                    items += 1
                    result.append(f'You bought {product} for {total_price:.2f} leva.')

    else:
        result.append("You do not have enough budget.")

    return '\n'.join(item for item in result)

