# The price of the product on the price tag is given before and after the
# discount is applied. Write a program that allows you to enter the product
# price and discount. Print the product price, discount, discounted product
# price, and the difference between the product price before and after the
# discount. Print all prices with two decimal places.

price = float(input('Enter price: '))
discount_percentage = int(input('Enter discount %: '))
reduction = price * (discount_percentage/100)
price_w_discount = price - reduction

print(f'Price with discount: {price_w_discount:.2f}')
print(f'Reduction: {reduction:.2f}')