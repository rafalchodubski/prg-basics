# 23% VAT was paid from an amount. Write a program that reads an
# amount from the keyboard. Then, it calculates and prints both the amount
# and its VAT. Apply formatting with two decimal places.
amount = float(input('Amount: '))
vat = 0.23 * amount
float(vat)
print(f"Amount : {amount}")
print(f"VAT 23% : {vat:.2f}")