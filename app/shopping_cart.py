from typing import List


def shopping_cart() -> List:
    '''Shopping cart using Walrus := operator'''
    cart = []
    while (item := input('Insert item to cart: ')) != 'exit':
        cart.append(item)
        print(cart)
    return cart

print(shopping_cart())