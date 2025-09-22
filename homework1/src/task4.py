# task 4 Duck typing
# Mason Andersen
# CS 4300

# calculates the final price with a discount
# python will just know what type to use

# need to accept integer or float for price and discount
def calculate_discount(price, discount):
    # assume if they type "10" for discount they mean 10% and not 1000% 
    if discount > 1:
        discount = discount/100
    # otherwise just run it normally
    finalPrice = price - (price * discount) 
    return finalPrice



