def stock_availability(list_, sec_param, *args):
    lst = []
    if sec_param == "delivery":
        for arg in args:
            lst.append(arg)
        return list_ + list(args)
    elif sec_param == "sell":
        if not args:
            return list_[1:]
        if isinstance(args[0], int):
            count = int(args[0])
            return list_[count:]
        sold_items = set(args)
        return [item for item in list_ if item not in sold_items]

