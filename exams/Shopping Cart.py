def shopping_cart(*args):
    soup_capacity = 3
    pizza_capacity = 4
    dessert_capacity = 2
    meals = {}
    result = ''
    for arg in args:
        if arg == 'Stop':
            break
        else:
            if not meals:
                meals["Soup"] = set()
                meals['Pizza'] = set()
                meals['Dessert'] = set()
                meal, product = arg[0], arg[1]
                if meal == "Soup":
                    if soup_capacity > 0:
                        meals["Soup"].add(product)
                        soup_capacity -= 1
                elif meal == "Pizza":
                    if pizza_capacity > 0:
                        meals["Pizza"].add(product)
                        pizza_capacity -= 1
                elif meal == "Dessert":
                    if dessert_capacity > 0:
                        meals["Dessert"].add(product)
                        dessert_capacity -= 1
            else:
                meal, product = arg[0], arg[1]
                if meal == "Soup":
                    if soup_capacity > 0:
                        meals["Soup"].add(product)
                        soup_capacity -= 1
                elif meal == "Pizza":
                    if pizza_capacity > 0:
                        meals["Pizza"].add(product)
                        pizza_capacity -= 1
                elif meal == "Dessert":
                    if dessert_capacity > 0:
                        meals["Dessert"].add(product)
                        dessert_capacity -= 1

    if not meals:
        return "No products in the cart!"
    else:
        sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
        for tuple_ in sorted_meals:
            type_meals = tuple_[0]
            list_of_products = tuple_[1]
            sorted_list_of_products = sorted(list_of_products)
            result += f"{type_meals}:\n"
            for obj in sorted_list_of_products:
                result += f" - {obj}\n"
        return result.strip()


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
#
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
