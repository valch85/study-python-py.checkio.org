def bigger_price(limit: int, data: list) -> list:

    return sorted(data, key=lambda i: i["price"], reverse=True)[0:limit]

#    last_index = len(data) - 1
#    for i in range(0, last_index):
#        for j in range(0, last_index - i):
#            if data[j]["price"] < data[j + 1]["price"]:
#                data[j], data[j + 1] = data[j + 1], data[j]
#    return data[:limit]

bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) #== [
       # {"name": "wine", "price": 138},
       # {"name": "bread", "price": 100}
    #]

bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) #== [{"name": "whiteboard", "price": 170}]


