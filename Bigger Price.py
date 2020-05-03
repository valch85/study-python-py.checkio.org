


def bigger_price(limit: int, data: list) -> list:
    #print(limit)
    b = sorted(data, key=data.get)
    print(b)
    for d in range(len(data)):
        print(data[d]['price'])



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

