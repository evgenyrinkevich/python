item_prices = [57.8, 0.34, 46.51, 97, 56.1, 23.45, 64, 13.45, 98.84, 71, 41.2]

# задание А
for item in item_prices:
    cur_item_price = str(item).split('.')
    if len(cur_item_price) < 2:
        print(f'{cur_item_price[0]} рублей 00 копеек')
    else:
        print(f'{cur_item_price[0]} рублей {int(cur_item_price[1]):02} копеек')

# задание B
item_prices.sort()
for item in item_prices:
    cur_item_price = str(item).split('.')
    if len(cur_item_price) < 2:
        print(f'{cur_item_price[0]} рублей 00 копеек')
    else:
        print(f'{cur_item_price[0]} рублей {int(cur_item_price[1]):02} копеек')

# задание C
item_prices_reversed = sorted(item_prices, reverse=True)
print(item_prices_reversed)

# задание D
highest_prices = sorted(item_prices_reversed[:5])

for item in highest_prices:
    cur_item_price = str(item).split('.')
    if len(cur_item_price) < 2:
        print(f'{cur_item_price[0]} рублей 00 копеек')
    else:
        print(f'{cur_item_price[0]} рублей {int(cur_item_price[1]):02} копеек')


