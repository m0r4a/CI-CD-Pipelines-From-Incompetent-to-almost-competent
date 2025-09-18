ITEMS = {
    "apple": 2,
    "banana": 4,
    "grape": 1
}

apples = 4
bananas = 7
grapes = 2

def final_price(apples, bananas, grapes):
    apples *= ITEMS["apple"]
    bananas *= ITEMS["banana"]
    grapes *= ITEMS["grape"]

    return apples + bananas + grapes

price = final_price(apples, bananas, grapes)

print(f"The final price is ${price}")
